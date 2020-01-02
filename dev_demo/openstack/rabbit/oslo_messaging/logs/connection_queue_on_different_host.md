# Connection & Queue on Different Host

## Serverside

```log
(test) root@master1:/tmp/sjt/dev-demo/dev_demo/openstack/rabbit/oslo_messaging# python rpc_server.py --config-file ./config
DEBUG:stevedore.extension:found extension EntryPoint.parse('kombu = oslo_messaging._drivers.impl_rabbit:RabbitDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('kafka = oslo_messaging._drivers.impl_kafka:KafkaDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('amqp = oslo_messaging._drivers.impl_amqp1:ProtonDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('rabbit = oslo_messaging._drivers.impl_rabbit:RabbitDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('fake = oslo_messaging._drivers.impl_fake:FakeDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('threading = futurist:ThreadPoolExecutor')
DEBUG:stevedore.extension:found extension EntryPoint.parse('blocking = futurist:SynchronousExecutor')
DEBUG:stevedore.extension:found extension EntryPoint.parse('eventlet = futurist:GreenThreadPoolExecutor')
starting
DEBUG:oslo.messaging._drivers.pool:Pool creating new connection
DEBUG:oslo.messaging._drivers.impl_rabbit:[5b326e3c-d00c-4fd6-96ec-05d055b09cc5] Connecting to AMQP server on rabbitmq-rabbitmq-1.rabbitmq.openstack.svc.cluster.local:5672
DEBUG:amqp:Start from server, version: 0.9, properties: {'information': 'Licensed under the MPL.  See http://www.rabbitmq.com/', 'product': 'RabbitMQ', 'copyright': 'Copyright (C) 2007-2019 Pivotal Software, Inc.', 'capabilities': {'exchange_exchange_bindings': True, 'connection.blocked': True, 'authentication_failure_close': True, 'direct_reply_to': True, 'basic.nack': True, 'per_consumer_qos': True, 'consumer_priorities': True, 'consumer_cancel_notify': True, 'publisher_confirms': True}, 'cluster_name': 'rabbit@rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local', 'platform': 'Erlang/OTP 21.3.2', 'version': '3.7.13'}, mechanisms: ['PLAIN', 'AMQPLAIN'], locales: [u'en_US']
DEBUG:amqp:using channel_id: 1
DEBUG:amqp:Channel open
DEBUG:oslo.messaging._drivers.impl_rabbit:[5b326e3c-d00c-4fd6-96ec-05d055b09cc5] Connected to AMQP server on rabbitmq-rabbitmq-1.rabbitmq.openstack.svc.cluster.local:5672 via [amqp] client with port 45810.
DEBUG:oslo.messaging._drivers.impl_rabbit:[5b326e3c-d00c-4fd6-96ec-05d055b09cc5] Queue.declare: test
DEBUG:oslo.messaging._drivers.impl_rabbit:[5b326e3c-d00c-4fd6-96ec-05d055b09cc5] Queue.declare: test.master1
DEBUG:oslo.messaging._drivers.impl_rabbit:[5b326e3c-d00c-4fd6-96ec-05d055b09cc5] Queue.declare: test_fanout_2e8cc995a68a4ef89835b8b23f60c0ba
DEBUG:amqp:heartbeat_tick : for connection 4edf0925d87b45eabd1d5b435ef04063
DEBUG:amqp:heartbeat_tick : Prev sent/recv: None/None, now - 17/17, monotonic - 1266736.26741, last_heartbeat_sent - 1266736.26739, heartbeat int. - 60 for connection 4edf0925d87b45eabd1d5b435ef04063
DEBUG:amqp:heartbeat_tick : for connection 4edf0925d87b45eabd1d5b435ef04063
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 17/17, now - 17/17, monotonic - 1266736.26967, last_heartbeat_sent - 1266736.26739, heartbeat int. - 60 for connection 4edf0925d87b45eabd1d5b435ef04063
DEBUG:amqp:heartbeat_tick : for connection 4edf0925d87b45eabd1d5b435ef04063
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 17/17, now - 17/17, monotonic - 1266737.27119, last_heartbeat_sent - 1266736.26739, heartbeat int. - 60 for connection 4edf0925d87b45eabd1d5b435ef04063
DEBUG:oslo_messaging._drivers.amqpdriver:received message msg_id: 7faeea9d9f744d2cafae95cc79bc1e9a reply to reply_c4a295b4b2354cf7847e7365e7d67368
DEBUG:amqp:heartbeat_tick : for connection 4edf0925d87b45eabd1d5b435ef04063
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 17/17, now - 18/20, monotonic - 1266738.76609, last_heartbeat_sent - 1266738.76607, heartbeat int. - 60 for connection 4edf0925d87b45eabd1d5b435ef04063
DEBUG:oslo.messaging._drivers.pool:Pool creating new connection
DEBUG:oslo.messaging._drivers.impl_rabbit:[4887a02e-a51d-448e-8ab8-6dddf2eb2dee] Connecting to AMQP server on rabbitmq-rabbitmq-1.rabbitmq.openstack.svc.cluster.local:5672
DEBUG:amqp:heartbeat_tick : for connection 4edf0925d87b45eabd1d5b435ef04063
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 18/20, now - 18/20, monotonic - 1266738.78029, last_heartbeat_sent - 1266738.76607, heartbeat int. - 60 for connection 4edf0925d87b45eabd1d5b435ef04063
DEBUG:amqp:Start from server, version: 0.9, properties: {'information': 'Licensed under the MPL.  See http://www.rabbitmq.com/', 'product': 'RabbitMQ', 'copyright': 'Copyright (C) 2007-2019 Pivotal Software, Inc.', 'capabilities': {'exchange_exchange_bindings': True, 'connection.blocked': True, 'authentication_failure_close': True, 'direct_reply_to': True, 'basic.nack': True, 'per_consumer_qos': True, 'consumer_priorities': True, 'consumer_cancel_notify': True, 'publisher_confirms': True}, 'cluster_name': 'rabbit@rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local', 'platform': 'Erlang/OTP 21.3.2', 'version': '3.7.13'}, mechanisms: ['PLAIN', 'AMQPLAIN'], locales: [u'en_US']
DEBUG:amqp:using channel_id: 1
DEBUG:amqp:Channel open
DEBUG:amqp:heartbeat_tick : for connection fe22ad8675ae4222b306033dd7cf4a28
DEBUG:amqp:heartbeat_tick : Prev sent/recv: None/None, now - 4/4, monotonic - 1266738.79135, last_heartbeat_sent - 1266738.79133, heartbeat int. - 60 for connection fe22ad8675ae4222b306033dd7cf4a28
DEBUG:oslo.messaging._drivers.impl_rabbit:[4887a02e-a51d-448e-8ab8-6dddf2eb2dee] Connected to AMQP server on rabbitmq-rabbitmq-1.rabbitmq.openstack.svc.cluster.local:5672 via [amqp] client with port 45826.
DEBUG:oslo_messaging._drivers.amqpdriver:sending reply msg_id: 7faeea9d9f744d2cafae95cc79bc1e9a reply queue: reply_c4a295b4b2354cf7847e7365e7d67368 time elapsed: 0.0275907129981s
DEBUG:amqp:heartbeat_tick : for connection 4edf0925d87b45eabd1d5b435ef04063
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 18/20, now - 18/20, monotonic - 1266739.78159, last_heartbeat_sent - 1266738.76607, heartbeat int. - 60 for connection 4edf0925d87b45eabd1d5b435ef04063
DEBUG:amqp:heartbeat_tick : for connection 4edf0925d87b45eabd1d5b435ef04063
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 18/20, now - 18/20, monotonic - 1266741.78292, last_heartbeat_sent - 1266738.76607, heartbeat int. - 60 for connection 4edf0925d87b45eabd1d5b435ef04063
DEBUG:amqp:heartbeat_tick : for connection 4edf0925d87b45eabd1d5b435ef04063
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 18/20, now - 18/20, monotonic - 1266745.78431, last_heartbeat_sent - 1266738.76607, heartbeat int. - 60 for connection 4edf0925d87b45eabd1d5b435ef04063
DEBUG:amqp:Closed channel #1
DEBUG:oslo.messaging._drivers.impl_rabbit:[5b326e3c-d00c-4fd6-96ec-05d055b09cc5] Received recoverable error from kombu:
Traceback (most recent call last):
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 518, in _ensured
    return fun(*args, **kwargs)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 594, in __call__
    return fun(*args, channel=channels[0], **kwargs), channels[0]
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/impl_rabbit.py", line 798, in execute_method
    method()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/impl_rabbit.py", line 1097, in _consume
    self.connection.drain_events(timeout=poll_timeout)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 323, in drain_events
    return self.transport.drain_events(self.connection, **kwargs)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/transport/pyamqp.py", line 103, in drain_events
    return connection.drain_events(**kwargs)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/connection.py", line 505, in drain_events
    while not self.blocking_read(timeout):
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/connection.py", line 511, in blocking_read
    return self.on_inbound_frame(frame)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/method_framing.py", line 55, in on_frame
    callback(channel, method_sig, buf, None)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/connection.py", line 518, in on_inbound_method
    method_sig, payload, content,
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/abstract_channel.py", line 145, in dispatch_method
    listener(*args)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/channel.py", line 1453, in _on_basic_cancel
    raise ConsumerCancelled(consumer_tag, spec.Basic.Cancel)
ConsumerCancelled: Basic.cancel: (0) 1
ERROR:oslo.messaging._drivers.impl_rabbit:[5b326e3c-d00c-4fd6-96ec-05d055b09cc5] AMQP server on rabbitmq-rabbitmq-1.rabbitmq.openstack.svc.cluster.local:5672 is unreachable: Basic.cancel: (0) 1. Trying again in 1 seconds.
DEBUG:amqp:Start from server, version: 0.9, properties: {'information': 'Licensed under the MPL.  See http://www.rabbitmq.com/', 'product': 'RabbitMQ', 'copyright': 'Copyright (C) 2007-2019 Pivotal Software, Inc.', 'capabilities': {'exchange_exchange_bindings': True, 'connection.blocked': True, 'authentication_failure_close': True, 'direct_reply_to': True, 'basic.nack': True, 'per_consumer_qos': True, 'consumer_priorities': True, 'consumer_cancel_notify': True, 'publisher_confirms': True}, 'cluster_name': 'rabbit@rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local', 'platform': 'Erlang/OTP 21.3.2', 'version': '3.7.13'}, mechanisms: ['PLAIN', 'AMQPLAIN'], locales: [u'en_US']
DEBUG:amqp:using channel_id: 1
DEBUG:amqp:Channel open
DEBUG:oslo.messaging._drivers.impl_rabbit:[5b326e3c-d00c-4fd6-96ec-05d055b09cc5] Queue.declare: test_fanout_2e8cc995a68a4ef89835b8b23f60c0ba
DEBUG:oslo.messaging._drivers.impl_rabbit:[5b326e3c-d00c-4fd6-96ec-05d055b09cc5] Queue.declare: test
DEBUG:amqp:Channel open
DEBUG:amqp:Channel open
ERROR:oslo.messaging._drivers.impl_rabbit:Failed to consume message from queue: Queue.declare: (404) NOT_FOUND - queue 'test' in vhost 'neutron' process is stopped by supervisor
DEBUG:amqp:Closed channel #1
ERROR:oslo.messaging._drivers.impl_rabbit:Unable to connect to AMQP server on rabbitmq-rabbitmq-1.rabbitmq.openstack.svc.cluster.local:5672 after inf tries: Queue.declare: (404) NOT_FOUND - queue 'test' in vhost 'neutron' process is stopped by supervisor
ERROR:root:Unexpected exception occurred 1 time(s)... retrying.
Traceback (most recent call last):
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_utils/excutils.py", line 250, in wrapper
    return infunc(*args, **kwargs)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/base.py", line 306, in _runner
    batch_size=self.batch_size, batch_timeout=self.batch_timeout)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/base.py", line 53, in wrapper
    message = func(in_self, timeout=watch.leftover(True))
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/amqpdriver.py", line 317, in poll
    self.conn.consume(timeout=min(self._current_timeout, left))
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/impl_rabbit.py", line 1112, in consume
    error_callback=_error_callback)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/impl_rabbit.py", line 831, in ensure
    raise exceptions.MessageDeliveryFailure(msg)
MessageDeliveryFailure: Unable to connect to AMQP server on rabbitmq-rabbitmq-1.rabbitmq.openstack.svc.cluster.local:5672 after inf tries: Queue.declare: (404) NOT_FOUND - queue 'test' in vhost 'neutron' process is stopped by supervisor
DEBUG:oslo.messaging._drivers.impl_rabbit:[5b326e3c-d00c-4fd6-96ec-05d055b09cc5] Received recoverable error from kombu:
Traceback (most recent call last):
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 518, in _ensured
    return fun(*args, **kwargs)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 594, in __call__
    return fun(*args, channel=channels[0], **kwargs), channels[0]
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/impl_rabbit.py", line 797, in execute_method
    self._set_current_channel(channel)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/impl_rabbit.py", line 855, in _set_current_channel
    self._set_qos(new_channel)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/impl_rabbit.py", line 866, in _set_qos
    False)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/channel.py", line 1853, in basic_qos
    wait=spec.Basic.QosOk,
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/abstract_channel.py", line 56, in send_method
    raise RecoverableConnectionError('connection already closed')
RecoverableConnectionError: connection already closed
ERROR:oslo.messaging._drivers.impl_rabbit:[5b326e3c-d00c-4fd6-96ec-05d055b09cc5] AMQP server on rabbitmq-rabbitmq-1.rabbitmq.openstack.svc.cluster.local:5672 is unreachable: connection already closed. Trying again in 1 seconds.
DEBUG:amqp:Start from server, version: 0.9, properties: {'information': 'Licensed under the MPL.  See http://www.rabbitmq.com/', 'product': 'RabbitMQ', 'copyright': 'Copyright (C) 2007-2019 Pivotal Software, Inc.', 'capabilities': {'exchange_exchange_bindings': True, 'connection.blocked': True, 'authentication_failure_close': True, 'direct_reply_to': True, 'basic.nack': True, 'per_consumer_qos': True, 'consumer_priorities': True, 'consumer_cancel_notify': True, 'publisher_confirms': True}, 'cluster_name': 'rabbit@rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local', 'platform': 'Erlang/OTP 21.3.2', 'version': '3.7.13'}, mechanisms: ['PLAIN', 'AMQPLAIN'], locales: [u'en_US']
DEBUG:amqp:using channel_id: 1
DEBUG:amqp:Channel open
DEBUG:oslo.messaging._drivers.impl_rabbit:[5b326e3c-d00c-4fd6-96ec-05d055b09cc5] Queue.declare: test_fanout_2e8cc995a68a4ef89835b8b23f60c0ba
DEBUG:oslo.messaging._drivers.impl_rabbit:[5b326e3c-d00c-4fd6-96ec-05d055b09cc5] Queue.declare: test
DEBUG:amqp:Channel open
DEBUG:amqp:Channel open
ERROR:oslo.messaging._drivers.impl_rabbit:Failed to consume message from queue: Queue.declare: (404) NOT_FOUND - queue 'test' in vhost 'neutron' process is stopped by supervisor
DEBUG:amqp:Closed channel #1
ERROR:oslo.messaging._drivers.impl_rabbit:Unable to connect to AMQP server on rabbitmq-rabbitmq-1.rabbitmq.openstack.svc.cluster.local:5672 after inf tries: Queue.declare: (404) NOT_FOUND - queue 'test' in vhost 'neutron' process is stopped by supervisor
DEBUG:oslo.messaging._drivers.impl_rabbit:[5b326e3c-d00c-4fd6-96ec-05d055b09cc5] Received recoverable error from kombu:
Traceback (most recent call last):
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 518, in _ensured
    return fun(*args, **kwargs)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 594, in __call__
    return fun(*args, channel=channels[0], **kwargs), channels[0]
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/impl_rabbit.py", line 797, in execute_method
    self._set_current_channel(channel)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/impl_rabbit.py", line 855, in _set_current_channel
    self._set_qos(new_channel)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/impl_rabbit.py", line 866, in _set_qos
    False)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/channel.py", line 1853, in basic_qos
    wait=spec.Basic.QosOk,
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/abstract_channel.py", line 56, in send_method
    raise RecoverableConnectionError('connection already closed')
RecoverableConnectionError: connection already closed
ERROR:oslo.messaging._drivers.impl_rabbit:[5b326e3c-d00c-4fd6-96ec-05d055b09cc5] AMQP server on rabbitmq-rabbitmq-1.rabbitmq.openstack.svc.cluster.local:5672 is unreachable: connection already closed. Trying again in 1 seconds.
DEBUG:amqp:Start from server, version: 0.9, properties: {'information': 'Licensed under the MPL.  See http://www.rabbitmq.com/', 'product': 'RabbitMQ', 'copyright': 'Copyright (C) 2007-2019 Pivotal Software, Inc.', 'capabilities': {'exchange_exchange_bindings': True, 'connection.blocked': True, 'authentication_failure_close': True, 'direct_reply_to': True, 'basic.nack': True, 'per_consumer_qos': True, 'consumer_priorities': True, 'consumer_cancel_notify': True, 'publisher_confirms': True}, 'cluster_name': 'rabbit@rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local', 'platform': 'Erlang/OTP 21.3.2', 'version': '3.7.13'}, mechanisms: ['PLAIN', 'AMQPLAIN'], locales: [u'en_US']
DEBUG:amqp:using channel_id: 1
DEBUG:amqp:Channel open
DEBUG:oslo.messaging._drivers.impl_rabbit:[5b326e3c-d00c-4fd6-96ec-05d055b09cc5] Queue.declare: test_fanout_2e8cc995a68a4ef89835b8b23f60c0ba
DEBUG:oslo.messaging._drivers.impl_rabbit:[5b326e3c-d00c-4fd6-96ec-05d055b09cc5] Queue.declare: test
DEBUG:oslo.messaging._drivers.impl_rabbit:[5b326e3c-d00c-4fd6-96ec-05d055b09cc5] Queue.declare: test.master1
INFO:oslo.messaging._drivers.impl_rabbit:[5b326e3c-d00c-4fd6-96ec-05d055b09cc5] Reconnected to AMQP server on rabbitmq-rabbitmq-1.rabbitmq.openstack.svc.cluster.local:5672 via [amqp] client with port 45904.
DEBUG:amqp:heartbeat_tick : for connection 154a312d313341f982e95ef5db217b34
DEBUG:amqp:heartbeat_tick : Prev sent/recv: None/None, now - 17/17, monotonic - 1266752.96422, last_heartbeat_sent - 1266752.9642, heartbeat int. - 60 for connection 154a312d313341f982e95ef5db217b34
DEBUG:amqp:heartbeat_tick : for connection fe22ad8675ae4222b306033dd7cf4a28
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 4/4, now - 6/6, monotonic - 1266753.79392, last_heartbeat_sent - 1266753.7939, heartbeat int. - 60 for connection fe22ad8675ae4222b306033dd7cf4a28
DEBUG:amqp:heartbeat_tick : for connection 154a312d313341f982e95ef5db217b34
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 17/17, now - 17/17, monotonic - 1266760.96563, last_heartbeat_sent - 1266752.9642, heartbeat int. - 60 for connection 154a312d313341f982e95ef5db217b34
DEBUG:amqp:heartbeat_tick : for connection fe22ad8675ae4222b306033dd7cf4a28
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 6/6, now - 6/6, monotonic - 1266768.79613, last_heartbeat_sent - 1266753.7939, heartbeat int. - 60 for connection fe22ad8675ae4222b306033dd7cf4a28
DEBUG:amqp:heartbeat_tick : for connection 154a312d313341f982e95ef5db217b34
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 17/17, now - 17/17, monotonic - 1266775.96675, last_heartbeat_sent - 1266752.9642, heartbeat int. - 60 for connection 154a312d313341f982e95ef5db217b34
DEBUG:amqp:heartbeat_tick : for connection 154a312d313341f982e95ef5db217b34
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 17/17, now - 17/17, monotonic - 1266776.96691, last_heartbeat_sent - 1266752.9642, heartbeat int. - 60 for connection 154a312d313341f982e95ef5db217b34
DEBUG:amqp:heartbeat_tick : for connection fe22ad8675ae4222b306033dd7cf4a28
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 6/6, now - 6/7, monotonic - 1266783.79911, last_heartbeat_sent - 1266753.7939, heartbeat int. - 60 for connection fe22ad8675ae4222b306033dd7cf4a28
DEBUG:amqp:heartbeat_tick : for connection 154a312d313341f982e95ef5db217b34
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 17/17, now - 17/18, monotonic - 1266797.62839, last_heartbeat_sent - 1266752.9642, heartbeat int. - 60 for connection 154a312d313341f982e95ef5db217b34
DEBUG:amqp:heartbeat_tick : for connection fe22ad8675ae4222b306033dd7cf4a28
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 6/7, now - 6/7, monotonic - 1266798.80117, last_heartbeat_sent - 1266753.7939, heartbeat int. - 60 for connection fe22ad8675ae4222b306033dd7cf4a28
DEBUG:amqp:heartbeat_tick : for connection 154a312d313341f982e95ef5db217b34
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 17/18, now - 17/18, monotonic - 1266808.96848, last_heartbeat_sent - 1266752.9642, heartbeat int. - 60 for connection 154a312d313341f982e95ef5db217b34
DEBUG:amqp:heartbeat_tick : for connection fe22ad8675ae4222b306033dd7cf4a28
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 6/7, now - 6/8, monotonic - 1266813.80334, last_heartbeat_sent - 1266753.7939, heartbeat int. - 60 for connection fe22ad8675ae4222b306033dd7cf4a28
DEBUG:amqp:heartbeat_tick: sending heartbeat for connection fe22ad8675ae4222b306033dd7cf4a28
DEBUG:amqp:heartbeat_tick : for connection 154a312d313341f982e95ef5db217b34
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 17/18, now - 17/19, monotonic - 1266827.63108, last_heartbeat_sent - 1266752.9642, heartbeat int. - 60 for connection 154a312d313341f982e95ef5db217b34
DEBUG:amqp:heartbeat_tick: sending heartbeat for connection 154a312d313341f982e95ef5db217b34
DEBUG:amqp:heartbeat_tick : for connection fe22ad8675ae4222b306033dd7cf4a28
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 6/8, now - 7/8, monotonic - 1266828.80589, last_heartbeat_sent - 1266828.80587, heartbeat int. - 60 for connection fe22ad8675ae4222b306033dd7cf4a28
^CStopping server
DEBUG:oslo.messaging._drivers.impl_rabbit:[connection close] Deleting fanout queue: test_fanout_2e8cc995a68a4ef89835b8b23f60c0ba
WARNING:amqp:Received method (60, 30) during closing channel 1. This method will be ignored
DEBUG:amqp:Closed channel #1
```

## Clientside

```log
(test) root@master1:/tmp/sjt/dev-demo/dev_demo/openstack/rabbit/oslo_messaging# python rpc_client.py --config-file ./config
DEBUG:stevedore.extension:found extension EntryPoint.parse('kombu = oslo_messaging._drivers.impl_rabbit:RabbitDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('kafka = oslo_messaging._drivers.impl_kafka:KafkaDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('amqp = oslo_messaging._drivers.impl_amqp1:ProtonDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('rabbit = oslo_messaging._drivers.impl_rabbit:RabbitDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('fake = oslo_messaging._drivers.impl_fake:FakeDriver')
DEBUG:oslo.messaging._drivers.pool:Pool creating new connection
DEBUG:oslo.messaging._drivers.impl_rabbit:[e41efb6e-9247-4ff5-b0b8-60e51f14fc23] Connecting to AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672
DEBUG:amqp:Start from server, version: 0.9, properties: {'information': 'Licensed under the MPL.  See http://www.rabbitmq.com/', 'product': 'RabbitMQ', 'copyright': 'Copyright (C) 2007-2019 Pivotal Software, Inc.', 'capabilities': {'exchange_exchange_bindings': True, 'connection.blocked': True, 'authentication_failure_close': True, 'direct_reply_to': True, 'basic.nack': True, 'per_consumer_qos': True, 'consumer_priorities': True, 'consumer_cancel_notify': True, 'publisher_confirms': True}, 'cluster_name': 'rabbit@rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local', 'platform': 'Erlang/OTP 21.3.2', 'version': '3.7.13'}, mechanisms: ['PLAIN', 'AMQPLAIN'], locales: [u'en_US']
DEBUG:amqp:using channel_id: 1
DEBUG:amqp:Channel open
DEBUG:oslo.messaging._drivers.impl_rabbit:[e41efb6e-9247-4ff5-b0b8-60e51f14fc23] Connected to AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672 via [amqp] client with port 59472.
DEBUG:oslo.messaging._drivers.impl_rabbit:[e41efb6e-9247-4ff5-b0b8-60e51f14fc23] Queue.declare: reply_33d8560d350e41d2a38e6f23a6306364
DEBUG:oslo.messaging._drivers.pool:Pool creating new connection
DEBUG:oslo.messaging._drivers.impl_rabbit:[52c12cae-1f03-4d4b-8fec-717a07ba8be5] Connecting to AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672
DEBUG:amqp:heartbeat_tick : for connection cea2e6fde5d04c53af1a99c928986a45
DEBUG:amqp:heartbeat_tick : Prev sent/recv: None/None, now - 7/7, monotonic - 1266667.66672, last_heartbeat_sent - 1266667.66669, heartbeat int. - 60 for connection cea2e6fde5d04c53af1a99c928986a45
DEBUG:amqp:heartbeat_tick : for connection cea2e6fde5d04c53af1a99c928986a45
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 7/7, now - 7/7, monotonic - 1266667.66908, last_heartbeat_sent - 1266667.66669, heartbeat int. - 60 for connection cea2e6fde5d04c53af1a99c928986a45
DEBUG:amqp:Start from server, version: 0.9, properties: {'information': 'Licensed under the MPL.  See http://www.rabbitmq.com/', 'product': 'RabbitMQ', 'copyright': 'Copyright (C) 2007-2019 Pivotal Software, Inc.', 'capabilities': {'exchange_exchange_bindings': True, 'connection.blocked': True, 'authentication_failure_close': True, 'direct_reply_to': True, 'basic.nack': True, 'per_consumer_qos': True, 'consumer_priorities': True, 'consumer_cancel_notify': True, 'publisher_confirms': True}, 'cluster_name': 'rabbit@rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local', 'platform': 'Erlang/OTP 21.3.2', 'version': '3.7.13'}, mechanisms: ['PLAIN', 'AMQPLAIN'], locales: [u'en_US']
DEBUG:amqp:using channel_id: 1
DEBUG:amqp:Channel open
DEBUG:amqp:heartbeat_tick : for connection 7aadf889af9b45b68a9c4711919f45ac
DEBUG:oslo.messaging._drivers.impl_rabbit:[52c12cae-1f03-4d4b-8fec-717a07ba8be5] Connected to AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672 via [amqp] client with port 59474.
DEBUG:amqp:heartbeat_tick : Prev sent/recv: None/None, now - 4/4, monotonic - 1266667.68017, last_heartbeat_sent - 1266667.68014, heartbeat int. - 60 for connection 7aadf889af9b45b68a9c4711919f45ac
DEBUG:oslo_messaging._drivers.amqpdriver:CALL msg_id: 8b8f46ce95f54986a68fd5a028855e37 exchange 'test' topic 'test'
DEBUG:oslo_messaging._drivers.amqpdriver:received reply msg_id: 8b8f46ce95f54986a68fd5a028855e37
DEBUG:amqp:heartbeat_tick : for connection cea2e6fde5d04c53af1a99c928986a45
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 7/7, now - 8/10, monotonic - 1266667.69897, last_heartbeat_sent - 1266667.69895, heartbeat int. - 60 for connection cea2e6fde5d04c53af1a99c928986a45
DEBUG:amqp:heartbeat_tick : for connection cea2e6fde5d04c53af1a99c928986a45
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 8/10, now - 8/10, monotonic - 1266667.70093, last_heartbeat_sent - 1266667.69895, heartbeat int. - 60 for connection cea2e6fde5d04c53af1a99c928986a45
hello
(test) root@master1:/tmp/sjt/dev-demo/dev_demo/openstack/rabbit/oslo_messaging# python rpc_client.py --config-file ./config
DEBUG:stevedore.extension:found extension EntryPoint.parse('kombu = oslo_messaging._drivers.impl_rabbit:RabbitDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('kafka = oslo_messaging._drivers.impl_kafka:KafkaDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('amqp = oslo_messaging._drivers.impl_amqp1:ProtonDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('rabbit = oslo_messaging._drivers.impl_rabbit:RabbitDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('fake = oslo_messaging._drivers.impl_fake:FakeDriver')
DEBUG:oslo.messaging._drivers.pool:Pool creating new connection
DEBUG:oslo.messaging._drivers.impl_rabbit:[aa1eefa2-4af5-406d-8a46-c84a7fa2090c] Connecting to AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672
DEBUG:amqp:Start from server, version: 0.9, properties: {'information': 'Licensed under the MPL.  See http://www.rabbitmq.com/', 'product': 'RabbitMQ', 'copyright': 'Copyright (C) 2007-2019 Pivotal Software, Inc.', 'capabilities': {'exchange_exchange_bindings': True, 'connection.blocked': True, 'authentication_failure_close': True, 'direct_reply_to': True, 'basic.nack': True, 'per_consumer_qos': True, 'consumer_priorities': True, 'consumer_cancel_notify': True, 'publisher_confirms': True}, 'cluster_name': 'rabbit@rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local', 'platform': 'Erlang/OTP 21.3.2', 'version': '3.7.13'}, mechanisms: ['PLAIN', 'AMQPLAIN'], locales: [u'en_US']
DEBUG:amqp:using channel_id: 1
DEBUG:amqp:Channel open
DEBUG:oslo.messaging._drivers.impl_rabbit:[aa1eefa2-4af5-406d-8a46-c84a7fa2090c] Connected to AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672 via [amqp] client with port 59498.
DEBUG:oslo.messaging._drivers.impl_rabbit:[aa1eefa2-4af5-406d-8a46-c84a7fa2090c] Queue.declare: reply_455b7ecfed614bcd83368e95c4faf873
DEBUG:oslo.messaging._drivers.pool:Pool creating new connection
DEBUG:oslo.messaging._drivers.impl_rabbit:[9e89c52d-e446-4cc3-a1b0-465480a6e9f6] Connecting to AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672
DEBUG:amqp:heartbeat_tick : for connection 43a18a30bf1445a1b5287712b4c9ed34
DEBUG:amqp:heartbeat_tick : Prev sent/recv: None/None, now - 7/7, monotonic - 1266673.44496, last_heartbeat_sent - 1266673.44494, heartbeat int. - 60 for connection 43a18a30bf1445a1b5287712b4c9ed34
DEBUG:amqp:heartbeat_tick : for connection 43a18a30bf1445a1b5287712b4c9ed34
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 7/7, now - 7/7, monotonic - 1266673.44708, last_heartbeat_sent - 1266673.44494, heartbeat int. - 60 for connection 43a18a30bf1445a1b5287712b4c9ed34
DEBUG:amqp:Start from server, version: 0.9, properties: {'information': 'Licensed under the MPL.  See http://www.rabbitmq.com/', 'product': 'RabbitMQ', 'copyright': 'Copyright (C) 2007-2019 Pivotal Software, Inc.', 'capabilities': {'exchange_exchange_bindings': True, 'connection.blocked': True, 'authentication_failure_close': True, 'direct_reply_to': True, 'basic.nack': True, 'per_consumer_qos': True, 'consumer_priorities': True, 'consumer_cancel_notify': True, 'publisher_confirms': True}, 'cluster_name': 'rabbit@rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local', 'platform': 'Erlang/OTP 21.3.2', 'version': '3.7.13'}, mechanisms: ['PLAIN', 'AMQPLAIN'], locales: [u'en_US']
DEBUG:amqp:using channel_id: 1
DEBUG:amqp:Channel open
DEBUG:oslo.messaging._drivers.impl_rabbit:[9e89c52d-e446-4cc3-a1b0-465480a6e9f6] Connected to AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672 via [amqp] client with port 59500.
DEBUG:amqp:heartbeat_tick : for connection 512950062c8645db9bcfbb354e265146
DEBUG:oslo_messaging._drivers.amqpdriver:CALL msg_id: fb2d839849a742e38eb6c9e07da250b5 exchange 'test' topic 'test'
DEBUG:amqp:heartbeat_tick : Prev sent/recv: None/None, now - 4/4, monotonic - 1266673.45886, last_heartbeat_sent - 1266673.45876, heartbeat int. - 60 for connection 512950062c8645db9bcfbb354e265146
DEBUG:oslo_messaging._drivers.amqpdriver:received reply msg_id: fb2d839849a742e38eb6c9e07da250b5
DEBUG:amqp:heartbeat_tick : for connection 43a18a30bf1445a1b5287712b4c9ed34
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 7/7, now - 8/10, monotonic - 1266673.4807, last_heartbeat_sent - 1266673.48069, heartbeat int. - 60 for connection 43a18a30bf1445a1b5287712b4c9ed34
hello
(test) root@master1:/tmp/sjt/dev-demo/dev_demo/openstack/rabbit/oslo_messaging# python rpc_client.py --config-file ./config
DEBUG:stevedore.extension:found extension EntryPoint.parse('kombu = oslo_messaging._drivers.impl_rabbit:RabbitDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('kafka = oslo_messaging._drivers.impl_kafka:KafkaDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('amqp = oslo_messaging._drivers.impl_amqp1:ProtonDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('rabbit = oslo_messaging._drivers.impl_rabbit:RabbitDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('fake = oslo_messaging._drivers.impl_fake:FakeDriver')
DEBUG:oslo.messaging._drivers.pool:Pool creating new connection
DEBUG:oslo.messaging._drivers.impl_rabbit:[ecb493a4-16f8-417b-a4f8-c682bc303b08] Connecting to AMQP server on rabbitmq-rabbitmq-1.rabbitmq.openstack.svc.cluster.local:5672
DEBUG:amqp:Start from server, version: 0.9, properties: {'information': 'Licensed under the MPL.  See http://www.rabbitmq.com/', 'product': 'RabbitMQ', 'copyright': 'Copyright (C) 2007-2019 Pivotal Software, Inc.', 'capabilities': {'exchange_exchange_bindings': True, 'connection.blocked': True, 'authentication_failure_close': True, 'direct_reply_to': True, 'basic.nack': True, 'per_consumer_qos': True, 'consumer_priorities': True, 'consumer_cancel_notify': True, 'publisher_confirms': True}, 'cluster_name': 'rabbit@rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local', 'platform': 'Erlang/OTP 21.3.2', 'version': '3.7.13'}, mechanisms: ['PLAIN', 'AMQPLAIN'], locales: [u'en_US']
DEBUG:amqp:using channel_id: 1
DEBUG:amqp:Channel open
DEBUG:oslo.messaging._drivers.impl_rabbit:[ecb493a4-16f8-417b-a4f8-c682bc303b08] Connected to AMQP server on rabbitmq-rabbitmq-1.rabbitmq.openstack.svc.cluster.local:5672 via [amqp] client with port 45822.
DEBUG:oslo.messaging._drivers.impl_rabbit:[ecb493a4-16f8-417b-a4f8-c682bc303b08] Queue.declare: reply_c4a295b4b2354cf7847e7365e7d67368
DEBUG:oslo.messaging._drivers.pool:Pool creating new connection
DEBUG:oslo.messaging._drivers.impl_rabbit:[82af5eb2-7b0a-4808-a00a-70079b756c84] Connecting to AMQP server on rabbitmq-rabbitmq-1.rabbitmq.openstack.svc.cluster.local:5672
DEBUG:amqp:heartbeat_tick : for connection d973c92a5dd945b691a63255d290f0c5
DEBUG:amqp:heartbeat_tick : Prev sent/recv: None/None, now - 7/7, monotonic - 1266738.73748, last_heartbeat_sent - 1266738.73745, heartbeat int. - 60 for connection d973c92a5dd945b691a63255d290f0c5
DEBUG:amqp:heartbeat_tick : for connection d973c92a5dd945b691a63255d290f0c5
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 7/7, now - 7/7, monotonic - 1266738.74019, last_heartbeat_sent - 1266738.73745, heartbeat int. - 60 for connection d973c92a5dd945b691a63255d290f0c5
DEBUG:amqp:Start from server, version: 0.9, properties: {'information': 'Licensed under the MPL.  See http://www.rabbitmq.com/', 'product': 'RabbitMQ', 'copyright': 'Copyright (C) 2007-2019 Pivotal Software, Inc.', 'capabilities': {'exchange_exchange_bindings': True, 'connection.blocked': True, 'authentication_failure_close': True, 'direct_reply_to': True, 'basic.nack': True, 'per_consumer_qos': True, 'consumer_priorities': True, 'consumer_cancel_notify': True, 'publisher_confirms': True}, 'cluster_name': 'rabbit@rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local', 'platform': 'Erlang/OTP 21.3.2', 'version': '3.7.13'}, mechanisms: ['PLAIN', 'AMQPLAIN'], locales: [u'en_US']
DEBUG:amqp:using channel_id: 1
DEBUG:amqp:Channel open
DEBUG:amqp:heartbeat_tick : for connection 45a02638e174476897871802a2106521
DEBUG:oslo.messaging._drivers.impl_rabbit:[82af5eb2-7b0a-4808-a00a-70079b756c84] Connected to AMQP server on rabbitmq-rabbitmq-1.rabbitmq.openstack.svc.cluster.local:5672 via [amqp] client with port 45824.
DEBUG:amqp:heartbeat_tick : Prev sent/recv: None/None, now - 4/4, monotonic - 1266738.75375, last_heartbeat_sent - 1266738.75372, heartbeat int. - 60 for connection 45a02638e174476897871802a2106521
DEBUG:oslo_messaging._drivers.amqpdriver:CALL msg_id: 7faeea9d9f744d2cafae95cc79bc1e9a exchange 'test' topic 'test'
DEBUG:oslo_messaging._drivers.amqpdriver:received reply msg_id: 7faeea9d9f744d2cafae95cc79bc1e9a
DEBUG:amqp:heartbeat_tick : for connection d973c92a5dd945b691a63255d290f0c5
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 7/7, now - 8/10, monotonic - 1266738.80746, last_heartbeat_sent - 1266738.80744, heartbeat int. - 60 for connection d973c92a5dd945b691a63255d290f0c5
DEBUG:amqp:heartbeat_tick : for connection d973c92a5dd945b691a63255d290f0c5
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 8/10, now - 8/10, monotonic - 1266738.80943, last_heartbeat_sent - 1266738.80744, heartbeat int. - 60 for connection d973c92a5dd945b691a63255d290f0c5
hello
(test) root@master1:/tmp/sjt/dev-demo/dev_demo/openstack/rabbit/oslo_messaging# python rpc_client.py --config-file ./config
DEBUG:stevedore.extension:found extension EntryPoint.parse('kombu = oslo_messaging._drivers.impl_rabbit:RabbitDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('kafka = oslo_messaging._drivers.impl_kafka:KafkaDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('amqp = oslo_messaging._drivers.impl_amqp1:ProtonDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('rabbit = oslo_messaging._drivers.impl_rabbit:RabbitDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('fake = oslo_messaging._drivers.impl_fake:FakeDriver')
DEBUG:oslo.messaging._drivers.pool:Pool creating new connection
DEBUG:oslo.messaging._drivers.impl_rabbit:[73662ee5-91dc-4cad-a145-f36abcfb4a72] Connecting to AMQP server on rabbitmq-rabbitmq-1.rabbitmq.openstack.svc.cluster.local:5672
DEBUG:amqp:Start from server, version: 0.9, properties: {'information': 'Licensed under the MPL.  See http://www.rabbitmq.com/', 'product': 'RabbitMQ', 'copyright': 'Copyright (C) 2007-2019 Pivotal Software, Inc.', 'capabilities': {'exchange_exchange_bindings': True, 'connection.blocked': True, 'authentication_failure_close': True, 'direct_reply_to': True, 'basic.nack': True, 'per_consumer_qos': True, 'consumer_priorities': True, 'consumer_cancel_notify': True, 'publisher_confirms': True}, 'cluster_name': 'rabbit@rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local', 'platform': 'Erlang/OTP 21.3.2', 'version': '3.7.13'}, mechanisms: ['PLAIN', 'AMQPLAIN'], locales: [u'en_US']
DEBUG:amqp:using channel_id: 1
DEBUG:amqp:Channel open
DEBUG:oslo.messaging._drivers.impl_rabbit:[73662ee5-91dc-4cad-a145-f36abcfb4a72] Connected to AMQP server on rabbitmq-rabbitmq-1.rabbitmq.openstack.svc.cluster.local:5672 via [amqp] client with port 45928.
DEBUG:oslo.messaging._drivers.impl_rabbit:[73662ee5-91dc-4cad-a145-f36abcfb4a72] Queue.declare: reply_c7fa6973899d4edb89cd49759ec6f493
DEBUG:oslo.messaging._drivers.pool:Pool creating new connection
DEBUG:oslo.messaging._drivers.impl_rabbit:[549fc2c4-ea05-43bc-9a70-1af596f03815] Connecting to AMQP server on rabbitmq-rabbitmq-1.rabbitmq.openstack.svc.cluster.local:5672
DEBUG:amqp:heartbeat_tick : for connection ed8fcfd9f31c450fb1ed60b871d60b2e
DEBUG:amqp:heartbeat_tick : Prev sent/recv: None/None, now - 7/7, monotonic - 1266756.28571, last_heartbeat_sent - 1266756.28569, heartbeat int. - 60 for connection ed8fcfd9f31c450fb1ed60b871d60b2e
DEBUG:amqp:heartbeat_tick : for connection ed8fcfd9f31c450fb1ed60b871d60b2e
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 7/7, now - 7/7, monotonic - 1266756.28786, last_heartbeat_sent - 1266756.28569, heartbeat int. - 60 for connection ed8fcfd9f31c450fb1ed60b871d60b2e
DEBUG:amqp:Start from server, version: 0.9, properties: {'information': 'Licensed under the MPL.  See http://www.rabbitmq.com/', 'product': 'RabbitMQ', 'copyright': 'Copyright (C) 2007-2019 Pivotal Software, Inc.', 'capabilities': {'exchange_exchange_bindings': True, 'connection.blocked': True, 'authentication_failure_close': True, 'direct_reply_to': True, 'basic.nack': True, 'per_consumer_qos': True, 'consumer_priorities': True, 'consumer_cancel_notify': True, 'publisher_confirms': True}, 'cluster_name': 'rabbit@rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local', 'platform': 'Erlang/OTP 21.3.2', 'version': '3.7.13'}, mechanisms: ['PLAIN', 'AMQPLAIN'], locales: [u'en_US']
DEBUG:amqp:using channel_id: 1
DEBUG:amqp:Channel open
DEBUG:amqp:heartbeat_tick : for connection 204877207e9a403ba9698c82984aee5f
DEBUG:oslo.messaging._drivers.impl_rabbit:[549fc2c4-ea05-43bc-9a70-1af596f03815] Connected to AMQP server on rabbitmq-rabbitmq-1.rabbitmq.openstack.svc.cluster.local:5672 via [amqp] client with port 45930.
DEBUG:amqp:heartbeat_tick : Prev sent/recv: None/None, now - 4/4, monotonic - 1266756.29867, last_heartbeat_sent - 1266756.29864, heartbeat int. - 60 for connection 204877207e9a403ba9698c82984aee5f
DEBUG:oslo_messaging._drivers.amqpdriver:CALL msg_id: dccb1d4c350446818e1e7fdd655398ca exchange 'test' topic 'test'
DEBUG:amqp:heartbeat_tick : for connection ed8fcfd9f31c450fb1ed60b871d60b2e
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 7/7, now - 7/7, monotonic - 1266757.28952, last_heartbeat_sent - 1266756.28569, heartbeat int. - 60 for connection ed8fcfd9f31c450fb1ed60b871d60b2e
DEBUG:amqp:heartbeat_tick : for connection ed8fcfd9f31c450fb1ed60b871d60b2e
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 7/7, now - 7/7, monotonic - 1266759.29286, last_heartbeat_sent - 1266756.28569, heartbeat int. - 60 for connection ed8fcfd9f31c450fb1ed60b871d60b2e
DEBUG:amqp:heartbeat_tick : for connection ed8fcfd9f31c450fb1ed60b871d60b2e
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 7/7, now - 7/7, monotonic - 1266763.29824, last_heartbeat_sent - 1266756.28569, heartbeat int. - 60 for connection ed8fcfd9f31c450fb1ed60b871d60b2e
DEBUG:amqp:heartbeat_tick : for connection 204877207e9a403ba9698c82984aee5f
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 4/4, now - 7/7, monotonic - 1266771.30098, last_heartbeat_sent - 1266771.30097, heartbeat int. - 60 for connection 204877207e9a403ba9698c82984aee5f
DEBUG:amqp:heartbeat_tick : for connection ed8fcfd9f31c450fb1ed60b871d60b2e
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 7/7, now - 7/7, monotonic - 1266771.30491, last_heartbeat_sent - 1266756.28569, heartbeat int. - 60 for connection ed8fcfd9f31c450fb1ed60b871d60b2e
DEBUG:amqp:heartbeat_tick : for connection 204877207e9a403ba9698c82984aee5f
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 7/7, now - 7/7, monotonic - 1266786.30304, last_heartbeat_sent - 1266771.30097, heartbeat int. - 60 for connection 204877207e9a403ba9698c82984aee5f
DEBUG:amqp:heartbeat_tick : for connection ed8fcfd9f31c450fb1ed60b871d60b2e
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 7/7, now - 7/8, monotonic - 1266801.25462, last_heartbeat_sent - 1266756.28569, heartbeat int. - 60 for connection ed8fcfd9f31c450fb1ed60b871d60b2e
DEBUG:amqp:heartbeat_tick : for connection 204877207e9a403ba9698c82984aee5f
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 7/7, now - 7/8, monotonic - 1266801.30542, last_heartbeat_sent - 1266771.30097, heartbeat int. - 60 for connection 204877207e9a403ba9698c82984aee5f
DEBUG:amqp:heartbeat_tick : for connection 204877207e9a403ba9698c82984aee5f
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 7/8, now - 7/8, monotonic - 1266816.30756, last_heartbeat_sent - 1266771.30097, heartbeat int. - 60 for connection 204877207e9a403ba9698c82984aee5f
DEBUG:amqp:heartbeat_tick : for connection ed8fcfd9f31c450fb1ed60b871d60b2e
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 7/8, now - 7/9, monotonic - 1266831.25755, last_heartbeat_sent - 1266756.28569, heartbeat int. - 60 for connection ed8fcfd9f31c450fb1ed60b871d60b2e
DEBUG:amqp:heartbeat_tick: sending heartbeat for connection ed8fcfd9f31c450fb1ed60b871d60b2e
DEBUG:amqp:heartbeat_tick : for connection 204877207e9a403ba9698c82984aee5f
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 7/8, now - 7/9, monotonic - 1266831.30981, last_heartbeat_sent - 1266771.30097, heartbeat int. - 60 for connection 204877207e9a403ba9698c82984aee5f
DEBUG:amqp:heartbeat_tick: sending heartbeat for connection 204877207e9a403ba9698c82984aee5f
DEBUG:amqp:heartbeat_tick : for connection ed8fcfd9f31c450fb1ed60b871d60b2e
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 7/9, now - 8/9, monotonic - 1266833.25622, last_heartbeat_sent - 1266833.25621, heartbeat int. - 60 for connection ed8fcfd9f31c450fb1ed60b871d60b2e
Traceback (most recent call last):
  File "rpc_client.py", line 68, in <module>
    main()
  File "rpc_client.py", line 64, in main
    print client.call(dict(), 'hello')
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/rpc/client.py", line 511, in call
    return self.prepare().call(ctxt, method, **kwargs)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/rpc/client.py", line 181, in call
    transport_options=self.transport_options)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/transport.py", line 129, in _send
    transport_options=transport_options)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/amqpdriver.py", line 646, in send
    transport_options=transport_options)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/amqpdriver.py", line 634, in _send
    call_monitor_timeout)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/amqpdriver.py", line 523, in wait
    message = self.waiters.get(msg_id, timeout=timeout)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/amqpdriver.py", line 401, in get
    'to message ID %s' % msg_id)
oslo_messaging.exceptions.MessagingTimeout: Timed out waiting for a reply to message ID dccb1d4c350446818e1e7fdd655398ca
```