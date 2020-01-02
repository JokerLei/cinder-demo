from oslo_messaging._drivers import impl_rabbit
import oslo_messaging as messaging
from oslo_config import cfg
import time
import kombu


def monkey_patch():

    def mandatory_publish(self, *args):
        """workaround to pass a mandatory flag"""

        logger = impl_rabbit.LOG

        if len(args) == 4:
            exchange, msg, routing_key, timeout = args
        else:
            exchange, msg, routing_key, timeout, _ = args

        print("Mandatory publisher got called")
        if not (exchange.passive or exchange.name in self._declared_exchanges):
                exchange(self.channel).declare()
                self._declared_exchanges.add(exchange.name)

        log_info = {'msg': msg,
                    'who': exchange or 'default',
                    'key': routing_key}
        logger.trace('Connection._publish: sending message %(msg)s to'
                  ' %(who)s with routing key %(key)s', log_info)

        # NOTE(sileht): no need to wait more, caller expects
        # a answer before timeout is reached
        with self._transport_socket_timeout(timeout):
            self._producer.publish(msg,
                                   # mandatory flag is added only for master
                                   mandatory=True,
                                   exchange=exchange,
                                   routing_key=routing_key,
                                   expiration=timeout,
                                   compression=self.kombu_compression)

    prev_impl = impl_rabbit.Connection._publish  # noqa
    impl_rabbit.Connection._publish = mandatory_publish


def init_config():
    """
    do not mix argparse with oslo_config
    :return:
    """

    cfg.CONF.register_cli_opt(cfg.StrOpt('topic', default='test'))
    cfg.CONF.register_cli_opt(cfg.StrOpt('exchange', default='test'))
    cfg.CONF(project='test')

    messaging.set_transport_defaults(
        control_exchange=cfg.CONF.exchange)


if __name__ == '__main__':
    monkey_patch()
    init_config()
    transport = messaging.get_rpc_transport(cfg.CONF)
    target = messaging.Target(topic=cfg.CONF.topic)

    client = messaging.RPCClient(transport, target)
    now = time.time()
    ctx = None
    try:
        ctx = client.prepare()
        print ctx.call(dict(), 'stop')
    except messaging.exceptions.MessageDeliveryFailure as e:
        msg = str(e)
        if "NO_ROUTE" in msg:
            print("message cannot be routed may imply MQ dysfunction")
            if ctx:
                # oslo.messaging does not right now provide `delete`
                # here it is a workaround, of course following code
                # is implementation dependent
                drv = ctx.transport._driver
                with drv._get_connection('send') as conn:
                    channel = conn.connection.connection.channel()
                    queue = kombu.entity.Queue(
                        channel=channel,
                        exchange=cfg.CONF.exchange,
                        name=cfg.CONF.topic,
                        routing_key=cfg.CONF.topic
                    )

                    # to avoid a potential racing
                    # use an exclusive queue as a lock
                    queue_lock = kombu.entity.Queue(
                        channel=channel,
                        exchange=cfg.CONF.exchange,
                        name=cfg.CONF.topic + ".lock"
                    )
                    queue_lock.declare()

                    # verify if queue exists
                    queue.queue_declare(passive=True)

                    # delete dysfunctional queue, but assume exchange is correct  # noqa
                    queue.delete()

    print time.time() - now
