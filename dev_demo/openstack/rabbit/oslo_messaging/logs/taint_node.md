# Taint Node

## With **10.2.0** oslo.messagin

### Serverside

```log
ERROR:oslo.messaging._drivers.impl_rabbit:[7decd41a-76e7-421f-8b3c-cc317183ac93] AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672 is unreachable: connection already closed. Trying again in 1 seconds.
DEBUG:amqp:Start from server, version: 0.9, properties: {'information': 'Licensed under the MPL.  See http://www.rabbitmq.com/', 'product': 'RabbitMQ', 'copyright': 'Copyright (C) 2007-2019 Pivotal Software, Inc.', 'capabilities': {'exchange_exchange_bindings': True, 'connection.blocked': True, 'authentication_failure_close': True, 'direct_reply_to': True, 'basic.nack': True, 'per_consumer_qos': True, 'consumer_priorities': True, 'consumer_cancel_notify': True, 'publisher_confirms': True}, 'cluster_name': 'rabbit@rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local', 'platform': 'Erlang/OTP 21.3.2', 'version': '3.7.13'}, mechanisms: ['PLAIN', 'AMQPLAIN'], locales: [u'en_US']
DEBUG:amqp:using channel_id: 1
DEBUG:amqp:Channel open
DEBUG:oslo.messaging._drivers.impl_rabbit:[7decd41a-76e7-421f-8b3c-cc317183ac93] Queue.declare: test_fanout_b94310a60d254c528cb262d73b195628
DEBUG:amqp:Channel open
DEBUG:amqp:Channel open
ERROR:oslo.messaging._drivers.impl_rabbit:Failed to consume message from queue: Queue.declare: (404) NOT_FOUND - queue 'test_fanout_b94310a60d254c528cb262d73b195628' in vhost 'neutron' process is stopped by supervisor
DEBUG:amqp:Closed channel #1
ERROR:oslo.messaging._drivers.impl_rabbit:Unable to connect to AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672 after inf tries: Queue.declare: (404) NOT_FOUND - queue 'test_fanout_b94310a60d254c528cb262d73b195628' in vhost 'neutron' process is stopped by supervisor
DEBUG:oslo.messaging._drivers.impl_rabbit:[7decd41a-76e7-421f-8b3c-cc317183ac93] Received recoverable error from kombu:
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
ERROR:oslo.messaging._drivers.impl_rabbit:[7decd41a-76e7-421f-8b3c-cc317183ac93] AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672 is unreachable: connection already closed. Trying again in 1 seconds.
DEBUG:amqp:heartbeat_tick : for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 6/8, now - 7/8, monotonic - 1278005.3437, last_heartbeat_sent - 1278005.34369, heartbeat int. - 60 for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:Start from server, version: 0.9, properties: {'information': 'Licensed under the MPL.  See http://www.rabbitmq.com/', 'product': 'RabbitMQ', 'copyright': 'Copyright (C) 2007-2019 Pivotal Software, Inc.', 'capabilities': {'exchange_exchange_bindings': True, 'connection.blocked': True, 'authentication_failure_close': True, 'direct_reply_to': True, 'basic.nack': True, 'per_consumer_qos': True, 'consumer_priorities': True, 'consumer_cancel_notify': True, 'publisher_confirms': True}, 'cluster_name': 'rabbit@rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local', 'platform': 'Erlang/OTP 21.3.2', 'version': '3.7.13'}, mechanisms: ['PLAIN', 'AMQPLAIN'], locales: [u'en_US']
DEBUG:amqp:using channel_id: 1
DEBUG:amqp:Channel open
DEBUG:oslo.messaging._drivers.impl_rabbit:[7decd41a-76e7-421f-8b3c-cc317183ac93] Queue.declare: test_fanout_b94310a60d254c528cb262d73b195628
DEBUG:amqp:Channel open
DEBUG:amqp:Channel open
ERROR:oslo.messaging._drivers.impl_rabbit:Failed to consume message from queue: Queue.declare: (404) NOT_FOUND - queue 'test_fanout_b94310a60d254c528cb262d73b195628' in vhost 'neutron' process is stopped by supervisor
DEBUG:amqp:Closed channel #1
ERROR:oslo.messaging._drivers.impl_rabbit:Unable to connect to AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672 after inf tries: Queue.declare: (404) NOT_FOUND - queue 'test_fanout_b94310a60d254c528cb262d73b195628' in vhost 'neutron' process is stopped by supervisor
DEBUG:oslo.messaging._drivers.impl_rabbit:[7decd41a-76e7-421f-8b3c-cc317183ac93] Received recoverable error from kombu:
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
ERROR:oslo.messaging._drivers.impl_rabbit:[7decd41a-76e7-421f-8b3c-cc317183ac93] AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672 is unreachable: connection already closed. Trying again in 1 seconds.
DEBUG:amqp:Start from server, version: 0.9, properties: {'information': 'Licensed under the MPL.  See http://www.rabbitmq.com/', 'product': 'RabbitMQ', 'copyright': 'Copyright (C) 2007-2019 Pivotal Software, Inc.', 'capabilities': {'exchange_exchange_bindings': True, 'connection.blocked': True, 'authentication_failure_close': True, 'direct_reply_to': True, 'basic.nack': True, 'per_consumer_qos': True, 'consumer_priorities': True, 'consumer_cancel_notify': True, 'publisher_confirms': True}, 'cluster_name': 'rabbit@rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local', 'platform': 'Erlang/OTP 21.3.2', 'version': '3.7.13'}, mechanisms: ['PLAIN', 'AMQPLAIN'], locales: [u'en_US']
DEBUG:amqp:using channel_id: 1
DEBUG:amqp:Channel open
DEBUG:oslo.messaging._drivers.impl_rabbit:[7decd41a-76e7-421f-8b3c-cc317183ac93] Queue.declare: test_fanout_b94310a60d254c528cb262d73b195628
DEBUG:amqp:Channel open
DEBUG:amqp:Channel open
ERROR:oslo.messaging._drivers.impl_rabbit:Failed to consume message from queue: Queue.declare: (404) NOT_FOUND - queue 'test_fanout_b94310a60d254c528cb262d73b195628' in vhost 'neutron' process is stopped by supervisor
DEBUG:amqp:Closed channel #1
ERROR:oslo.messaging._drivers.impl_rabbit:Unable to connect to AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672 after inf tries: Queue.declare: (404) NOT_FOUND - queue 'test_fanout_b94310a60d254c528cb262d73b195628' in vhost 'neutron' process is stopped by supervisor
DEBUG:oslo.messaging._drivers.impl_rabbit:[7decd41a-76e7-421f-8b3c-cc317183ac93] Received recoverable error from kombu:
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
ERROR:oslo.messaging._drivers.impl_rabbit:[7decd41a-76e7-421f-8b3c-cc317183ac93] AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672 is unreachable: connection already closed. Trying again in 1 seconds.
DEBUG:amqp:Start from server, version: 0.9, properties: {'information': 'Licensed under the MPL.  See http://www.rabbitmq.com/', 'product': 'RabbitMQ', 'copyright': 'Copyright (C) 2007-2019 Pivotal Software, Inc.', 'capabilities': {'exchange_exchange_bindings': True, 'connection.blocked': True, 'authentication_failure_close': True, 'direct_reply_to': True, 'basic.nack': True, 'per_consumer_qos': True, 'consumer_priorities': True, 'consumer_cancel_notify': True, 'publisher_confirms': True}, 'cluster_name': 'rabbit@rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local', 'platform': 'Erlang/OTP 21.3.2', 'version': '3.7.13'}, mechanisms: ['PLAIN', 'AMQPLAIN'], locales: [u'en_US']
DEBUG:amqp:using channel_id: 1
DEBUG:amqp:Channel open
DEBUG:oslo.messaging._drivers.impl_rabbit:[7decd41a-76e7-421f-8b3c-cc317183ac93] Queue.declare: test_fanout_b94310a60d254c528cb262d73b195628
DEBUG:oslo.messaging._drivers.impl_rabbit:[7decd41a-76e7-421f-8b3c-cc317183ac93] Queue.declare: test
DEBUG:oslo.messaging._drivers.impl_rabbit:[7decd41a-76e7-421f-8b3c-cc317183ac93] Queue.declare: test.master1
INFO:oslo.messaging._drivers.impl_rabbit:[7decd41a-76e7-421f-8b3c-cc317183ac93] Reconnected to AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672 via [amqp] client with port 56444.
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: None/None, now - 17/17, monotonic - 1278009.81309, last_heartbeat_sent - 1278009.81307, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:oslo_messaging._drivers.amqpdriver:received message msg_id: c94c5bf7095f4f68a67cd4ba1fa0a085 reply to reply_b06348a714374597962c50fa04c957d5
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 17/17, now - 18/20, monotonic - 1278017.16872, last_heartbeat_sent - 1278017.16871, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:oslo_messaging._drivers.amqpdriver:sending reply msg_id: c94c5bf7095f4f68a67cd4ba1fa0a085 reply queue: reply_b06348a714374597962c50fa04c957d5 time elapsed: 0.00173312309198s
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 18/20, now - 18/20, monotonic - 1278017.17196, last_heartbeat_sent - 1278017.16871, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 18/20, now - 18/20, monotonic - 1278018.1737, last_heartbeat_sent - 1278017.16871, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:oslo_messaging._drivers.amqpdriver:received message msg_id: 29fa9d0ff2004555be99047a481b6e28 reply to reply_4e873ef3184f414088e9592b50f100d7
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 18/20, now - 19/23, monotonic - 1278018.92867, last_heartbeat_sent - 1278018.92865, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:oslo_messaging._drivers.amqpdriver:sending reply msg_id: 29fa9d0ff2004555be99047a481b6e28 reply queue: reply_4e873ef3184f414088e9592b50f100d7 time elapsed: 0.00208879797719s
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 19/23, now - 19/23, monotonic - 1278018.93259, last_heartbeat_sent - 1278018.92865, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 19/23, now - 19/23, monotonic - 1278019.9341, last_heartbeat_sent - 1278018.92865, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 7/8, now - 9/11, monotonic - 1278020.34605, last_heartbeat_sent - 1278020.34604, heartbeat int. - 60 for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 19/23, now - 19/23, monotonic - 1278021.93581, last_heartbeat_sent - 1278018.92865, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 19/23, now - 19/23, monotonic - 1278025.93757, last_heartbeat_sent - 1278018.92865, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 19/23, now - 19/23, monotonic - 1278033.93951, last_heartbeat_sent - 1278018.92865, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 9/11, now - 9/11, monotonic - 1278035.34861, last_heartbeat_sent - 1278020.34604, heartbeat int. - 60 for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 9/11, now - 9/11, monotonic - 1278050.351, last_heartbeat_sent - 1278020.34604, heartbeat int. - 60 for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 19/23, now - 19/24, monotonic - 1278054.44169, last_heartbeat_sent - 1278018.92865, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 9/11, now - 9/11, monotonic - 1278065.35321, last_heartbeat_sent - 1278020.34604, heartbeat int. - 60 for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 9/11, now - 9/12, monotonic - 1278080.35655, last_heartbeat_sent - 1278020.34604, heartbeat int. - 60 for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick: sending heartbeat for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 19/24, now - 19/25, monotonic - 1278084.15687, last_heartbeat_sent - 1278018.92865, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick: sending heartbeat for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 19/25, now - 20/25, monotonic - 1278086.44313, last_heartbeat_sent - 1278086.44312, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 9/12, now - 10/12, monotonic - 1278095.35916, last_heartbeat_sent - 1278095.35915, heartbeat int. - 60 for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 10/12, now - 10/13, monotonic - 1278110.36151, last_heartbeat_sent - 1278095.35915, heartbeat int. - 60 for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 20/25, now - 20/26, monotonic - 1278113.87262, last_heartbeat_sent - 1278086.44312, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 10/13, now - 10/13, monotonic - 1278125.36387, last_heartbeat_sent - 1278095.35915, heartbeat int. - 60 for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 10/13, now - 10/14, monotonic - 1278140.36629, last_heartbeat_sent - 1278095.35915, heartbeat int. - 60 for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 20/26, now - 20/27, monotonic - 1278143.58847, last_heartbeat_sent - 1278086.44312, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 20/27, now - 20/27, monotonic - 1278150.44462, last_heartbeat_sent - 1278086.44312, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick: sending heartbeat for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 10/14, now - 10/14, monotonic - 1278155.36864, last_heartbeat_sent - 1278095.35915, heartbeat int. - 60 for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick: sending heartbeat for connection 747c793d22c14063bdd095f30af52e05
DEBUG:oslo_messaging._drivers.amqpdriver:received message msg_id: e0d0960cc02548d0bc2c7bbfba15309d reply to reply_8e5837758fab4aa59cf818c0b72e55f5
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 20/27, now - 22/31, monotonic - 1278166.52533, last_heartbeat_sent - 1278166.52531, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:oslo_messaging._drivers.amqpdriver:sending reply msg_id: e0d0960cc02548d0bc2c7bbfba15309d reply queue: reply_8e5837758fab4aa59cf818c0b72e55f5 time elapsed: 0.00216655991971s
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 22/31, now - 22/31, monotonic - 1278166.52927, last_heartbeat_sent - 1278166.52531, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 22/31, now - 22/31, monotonic - 1278167.5309, last_heartbeat_sent - 1278166.52531, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:oslo_messaging._drivers.amqpdriver:received message msg_id: 151a169d8bb747eaab3fe39d9f000d83 reply to reply_9aa43e763a9f45ac9bd0726a624b896a
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 22/31, now - 23/34, monotonic - 1278168.14775, last_heartbeat_sent - 1278168.14772, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:oslo_messaging._drivers.amqpdriver:sending reply msg_id: 151a169d8bb747eaab3fe39d9f000d83 reply queue: reply_9aa43e763a9f45ac9bd0726a624b896a time elapsed: 0.0022603708785s
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 23/34, now - 23/34, monotonic - 1278168.15166, last_heartbeat_sent - 1278168.14772, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 23/34, now - 23/34, monotonic - 1278169.15337, last_heartbeat_sent - 1278168.14772, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:oslo_messaging._drivers.amqpdriver:received message msg_id: 39b1fa0593ce4a6086977ed96080186c reply to reply_b06068817bac4ec195016f20aedd1a82
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 23/34, now - 24/37, monotonic - 1278169.72457, last_heartbeat_sent - 1278169.72455, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:oslo_messaging._drivers.amqpdriver:sending reply msg_id: 39b1fa0593ce4a6086977ed96080186c reply queue: reply_b06068817bac4ec195016f20aedd1a82 time elapsed: 0.0021160969045s
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 24/37, now - 24/37, monotonic - 1278169.72866, last_heartbeat_sent - 1278169.72455, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 10/14, now - 14/18, monotonic - 1278170.37169, last_heartbeat_sent - 1278170.37166, heartbeat int. - 60 for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 24/37, now - 24/37, monotonic - 1278170.73018, last_heartbeat_sent - 1278169.72455, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 24/37, now - 24/37, monotonic - 1278172.73232, last_heartbeat_sent - 1278169.72455, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 24/37, now - 24/37, monotonic - 1278176.73402, last_heartbeat_sent - 1278169.72455, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 24/37, now - 24/37, monotonic - 1278184.73576, last_heartbeat_sent - 1278169.72455, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 14/18, now - 14/18, monotonic - 1278185.37422, last_heartbeat_sent - 1278170.37166, heartbeat int. - 60 for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 24/37, now - 24/37, monotonic - 1278199.73711, last_heartbeat_sent - 1278169.72455, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 14/18, now - 14/18, monotonic - 1278200.37623, last_heartbeat_sent - 1278170.37166, heartbeat int. - 60 for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 24/37, now - 24/37, monotonic - 1278200.73711, last_heartbeat_sent - 1278169.72455, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 14/18, now - 14/18, monotonic - 1278215.37854, last_heartbeat_sent - 1278170.37166, heartbeat int. - 60 for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 24/37, now - 24/37, monotonic - 1278215.73816, last_heartbeat_sent - 1278169.72455, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 14/18, now - 14/19, monotonic - 1278230.38128, last_heartbeat_sent - 1278170.37166, heartbeat int. - 60 for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick: sending heartbeat for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 24/37, now - 24/38, monotonic - 1278232.73745, last_heartbeat_sent - 1278169.72455, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick: sending heartbeat for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 14/19, now - 15/19, monotonic - 1278245.38468, last_heartbeat_sent - 1278245.38467, heartbeat int. - 60 for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 15/19, now - 15/20, monotonic - 1278260.38746, last_heartbeat_sent - 1278245.38467, heartbeat int. - 60 for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 24/38, now - 25/39, monotonic - 1278262.45529, last_heartbeat_sent - 1278262.45529, heartbeat int. - 60 for connection 2f103198244c44c184f5525347722108
DEBUG:amqp:heartbeat_tick : for connection 747c793d22c14063bdd095f30af52e05
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 15/20, now - 15/20, monotonic - 1278275.3897, last_heartbeat_sent - 1278245.38467, heartbeat int. - 60 for connection 747c793d22c14063bdd095f30af52e05
^CStopping server
^CTraceback (most recent call last):
  File "rpc_server.py", line 92, in <module>
    main()
  File "rpc_server.py", line 87, in main
    server.stop()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/server.py", line 269, in wrapper
    log_after, timeout_timer)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/server.py", line 189, in run_once
    post_fn = fn()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/server.py", line 268, in <lambda>
    states[state].run_once(lambda: fn(self, *args, **kwargs),
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/server.py", line 429, in stop
    self.listener.stop()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/base.py", line 323, in stop
    self._poll_style_listener.stop()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/amqpdriver.py", line 335, in stop
    self._shutoff.wait()
  File "/usr/lib/python2.7/threading.py", line 614, in wait
    self.__cond.wait(timeout)
  File "/usr/lib/python2.7/threading.py", line 340, in wait
    waiter.acquire()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/eventlet/semaphore.py", line 113, in acquire
    hubs.get_hub().switch()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/eventlet/hubs/hub.py", line 294, in switch
    return self.greenlet.switch()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/eventlet/hubs/hub.py", line 346, in run
    self.wait(sleep_time)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/eventlet/hubs/poll.py", line 85, in wait
    presult = self.do_poll(seconds)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/eventlet/hubs/epolls.py", line 62, in do_poll
    return self.poll.poll(seconds)
KeyboardInterrupt
```

### Clientside

```log
DEBUG:stevedore.extension:found extension EntryPoint.parse('kombu = oslo_messaging._drivers.impl_rabbit:RabbitDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('kafka = oslo_messaging._drivers.impl_kafka:KafkaDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('amqp = oslo_messaging._drivers.impl_amqp1:ProtonDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('rabbit = oslo_messaging._drivers.impl_rabbit:RabbitDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('fake = oslo_messaging._drivers.impl_fake:FakeDriver')
DEBUG:oslo.messaging._drivers.pool:Pool creating new connection
DEBUG:oslo.messaging._drivers.impl_rabbit:[2d7acfd2-efa8-472c-88d2-7e3aac63fcde] Connecting to AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672
DEBUG:amqp:Start from server, version: 0.9, properties: {'information': 'Licensed under the MPL.  See http://www.rabbitmq.com/', 'product': 'RabbitMQ', 'copyright': 'Copyright (C) 2007-2019 Pivotal Software, Inc.', 'capabilities': {'exchange_exchange_bindings': True, 'connection.blocked': True, 'authentication_failure_close': True, 'direct_reply_to': True, 'basic.nack': True, 'per_consumer_qos': True, 'consumer_priorities': True, 'consumer_cancel_notify': True, 'publisher_confirms': True}, 'cluster_name': 'rabbit@rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local', 'platform': 'Erlang/OTP 21.3.2', 'version': '3.7.13'}, mechanisms: ['PLAIN', 'AMQPLAIN'], locales: [u'en_US']
DEBUG:amqp:using channel_id: 1
DEBUG:amqp:Channel open
DEBUG:oslo.messaging._drivers.impl_rabbit:[2d7acfd2-efa8-472c-88d2-7e3aac63fcde] Connected to AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672 via [amqp] client with port 57294.
DEBUG:oslo.messaging._drivers.impl_rabbit:[2d7acfd2-efa8-472c-88d2-7e3aac63fcde] Queue.declare: reply_b06068817bac4ec195016f20aedd1a82
DEBUG:oslo.messaging._drivers.pool:Pool creating new connection
DEBUG:oslo.messaging._drivers.impl_rabbit:[3c9afb00-13b5-4694-970f-f719afef648e] Connecting to AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672
DEBUG:amqp:heartbeat_tick : for connection 1bbdc77b10834cfab6766783b018274e
DEBUG:amqp:heartbeat_tick : Prev sent/recv: None/None, now - 7/7, monotonic - 1278169.70082, last_heartbeat_sent - 1278169.7008, heartbeat int. - 60 for connection 1bbdc77b10834cfab6766783b018274e
DEBUG:amqp:heartbeat_tick : for connection 1bbdc77b10834cfab6766783b018274e
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 7/7, now - 7/7, monotonic - 1278169.70297, last_heartbeat_sent - 1278169.7008, heartbeat int. - 60 for connection 1bbdc77b10834cfab6766783b018274e
DEBUG:amqp:Start from server, version: 0.9, properties: {'information': 'Licensed under the MPL.  See http://www.rabbitmq.com/', 'product': 'RabbitMQ', 'copyright': 'Copyright (C) 2007-2019 Pivotal Software, Inc.', 'capabilities': {'exchange_exchange_bindings': True, 'connection.blocked': True, 'authentication_failure_close': True, 'direct_reply_to': True, 'basic.nack': True, 'per_consumer_qos': True, 'consumer_priorities': True, 'consumer_cancel_notify': True, 'publisher_confirms': True}, 'cluster_name': 'rabbit@rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local', 'platform': 'Erlang/OTP 21.3.2', 'version': '3.7.13'}, mechanisms: ['PLAIN', 'AMQPLAIN'], locales: [u'en_US']
DEBUG:amqp:using channel_id: 1
DEBUG:amqp:Channel open
DEBUG:amqp:heartbeat_tick : for connection cc95e2569bc54f3f9756da51c6fafc86
DEBUG:oslo.messaging._drivers.impl_rabbit:[3c9afb00-13b5-4694-970f-f719afef648e] Connected to AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672 via [amqp] client with port 57296.
DEBUG:amqp:heartbeat_tick : Prev sent/recv: None/None, now - 4/4, monotonic - 1278169.71562, last_heartbeat_sent - 1278169.71556, heartbeat int. - 60 for connection cc95e2569bc54f3f9756da51c6fafc86
DEBUG:oslo_messaging._drivers.amqpdriver:CALL msg_id: 39b1fa0593ce4a6086977ed96080186c exchange 'test' topic 'test'
DEBUG:oslo_messaging._drivers.amqpdriver:received reply msg_id: 39b1fa0593ce4a6086977ed96080186c
DEBUG:amqp:heartbeat_tick : for connection 1bbdc77b10834cfab6766783b018274e
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 7/7, now - 8/10, monotonic - 1278169.73076, last_heartbeat_sent - 1278169.73074, heartbeat int. - 60 for connection 1bbdc77b10834cfab6766783b018274e
DEBUG:amqp:heartbeat_tick : for connection 1bbdc77b10834cfab6766783b018274e
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 8/10, now - 8/10, monotonic - 1278169.73271, last_heartbeat_sent - 1278169.73074, heartbeat int. - 60 for connection 1bbdc77b10834cfab6766783b018274e
hello
```

### Tainit Node & Force Clear

```console
root@master1:~# kubectl taint node slave4 rabbitmq=test:NoSchedule
node/slave4 tainted
root@master1:~# kubectl taint node slave5 rabbitmq=test:NoSchedule
node/slave5 tainted
root@master1:~# kubectl taint node slave6 rabbitmq=test:NoSchedule
node/slave6 tainted
root@master1:~# kubectl delete pod -n openstack rabbitmq-rabbitmq-2
```


## With Oslo.messaging **8.1.3**

### Serverside

```log
(test) root@master1:/tmp/sjt/dev-demo/dev_demo/openstack/rabbit/oslo_messaging# python rpc_server.py --config-file ./config
DEBUG:stevedore.extension:found extension EntryPoint.parse('amqp = oslo_messaging._drivers.impl_amqp1:ProtonDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('kafka = oslo_messaging._drivers.impl_kafka:KafkaDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('kombu = oslo_messaging._drivers.impl_rabbit:RabbitDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('rabbit = oslo_messaging._drivers.impl_rabbit:RabbitDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('fake = oslo_messaging._drivers.impl_fake:FakeDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('zmq = oslo_messaging._drivers.impl_zmq:ZmqDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('threading = futurist:ThreadPoolExecutor')
DEBUG:stevedore.extension:found extension EntryPoint.parse('blocking = futurist:SynchronousExecutor')
DEBUG:stevedore.extension:found extension EntryPoint.parse('eventlet = futurist:GreenThreadPoolExecutor')
starting
DEBUG:oslo.messaging._drivers.pool:Pool creating new connection
DEBUG:oslo.messaging._drivers.impl_rabbit:[7049682c-fe38-428f-aef4-5f24023db291] Connecting to AMQP server on rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local:5672
DEBUG:amqp:Start from server, version: 0.9, properties: {'information': 'Licensed under the MPL.  See http://www.rabbitmq.com/', 'product': 'RabbitMQ', 'copyright': 'Copyright (C) 2007-2019 Pivotal Software, Inc.', 'capabilities': {'exchange_exchange_bindings': True, 'connection.blocked': True, 'authentication_failure_close': True, 'direct_reply_to': True, 'basic.nack': True, 'per_consumer_qos': True, 'consumer_priorities': True, 'consumer_cancel_notify': True, 'publisher_confirms': True}, 'cluster_name': 'rabbit@rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local', 'platform': 'Erlang/OTP 21.3.2', 'version': '3.7.13'}, mechanisms: ['PLAIN', 'AMQPLAIN'], locales: [u'en_US']
DEBUG:amqp:using channel_id: 1
DEBUG:amqp:Channel open
DEBUG:oslo.messaging._drivers.impl_rabbit:[7049682c-fe38-428f-aef4-5f24023db291] Connected to AMQP server on rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local:5672 via [amqp] client with port 50626.
DEBUG:oslo.messaging._drivers.impl_rabbit:[7049682c-fe38-428f-aef4-5f24023db291] Queue.declare: test
DEBUG:oslo.messaging._drivers.impl_rabbit:[7049682c-fe38-428f-aef4-5f24023db291] Queue.declare: test.master1
DEBUG:oslo.messaging._drivers.impl_rabbit:[7049682c-fe38-428f-aef4-5f24023db291] Queue.declare: test_fanout_3be24e8dc0ac4b91b90c843d89146d2a
DEBUG:amqp:heartbeat_tick : for connection 18fed046b49e4dab9a2952a9609ce039
DEBUG:amqp:heartbeat_tick : Prev sent/recv: None/None, now - 17/17, monotonic - 1280194.14654, last_heartbeat_sent - 1280194.14652, heartbeat int. - 60 for connection 18fed046b49e4dab9a2952a9609ce039
DEBUG:amqp:heartbeat_tick : for connection 18fed046b49e4dab9a2952a9609ce039
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 17/17, now - 17/17, monotonic - 1280194.1488, last_heartbeat_sent - 1280194.14652, heartbeat int. - 60 for connection 18fed046b49e4dab9a2952a9609ce039
DEBUG:amqp:heartbeat_tick : for connection 18fed046b49e4dab9a2952a9609ce039
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 17/17, now - 17/17, monotonic - 1280195.15035, last_heartbeat_sent - 1280194.14652, heartbeat int. - 60 for connection 18fed046b49e4dab9a2952a9609ce039
DEBUG:amqp:heartbeat_tick : for connection 18fed046b49e4dab9a2952a9609ce039
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 17/17, now - 17/17, monotonic - 1280197.15137, last_heartbeat_sent - 1280194.14652, heartbeat int. - 60 for connection 18fed046b49e4dab9a2952a9609ce039
DEBUG:oslo_messaging._drivers.amqpdriver:received message msg_id: 53fb2fce39274242a76d60a685ba98d3 reply to reply_21e465af00c5445f9fc2731aae89d3ce
DEBUG:amqp:heartbeat_tick : for connection 18fed046b49e4dab9a2952a9609ce039
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 17/17, now - 17/20, monotonic - 1280197.27957, last_heartbeat_sent - 1280194.14652, heartbeat int. - 60 for connection 18fed046b49e4dab9a2952a9609ce039
DEBUG:oslo.messaging._drivers.pool:Pool creating new connection
DEBUG:oslo.messaging._drivers.impl_rabbit:[194ebf5e-22ce-4952-ab3e-095ebec93c8e] Connecting to AMQP server on rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local:5672
DEBUG:amqp:heartbeat_tick : for connection 18fed046b49e4dab9a2952a9609ce039
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 17/20, now - 18/20, monotonic - 1280197.29419, last_heartbeat_sent - 1280197.29418, heartbeat int. - 60 for connection 18fed046b49e4dab9a2952a9609ce039
DEBUG:amqp:Start from server, version: 0.9, properties: {'information': 'Licensed under the MPL.  See http://www.rabbitmq.com/', 'product': 'RabbitMQ', 'copyright': 'Copyright (C) 2007-2019 Pivotal Software, Inc.', 'capabilities': {'exchange_exchange_bindings': True, 'connection.blocked': True, 'authentication_failure_close': True, 'direct_reply_to': True, 'basic.nack': True, 'per_consumer_qos': True, 'consumer_priorities': True, 'consumer_cancel_notify': True, 'publisher_confirms': True}, 'cluster_name': 'rabbit@rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local', 'platform': 'Erlang/OTP 21.3.2', 'version': '3.7.13'}, mechanisms: ['PLAIN', 'AMQPLAIN'], locales: [u'en_US']
DEBUG:amqp:using channel_id: 1
DEBUG:amqp:Channel open
DEBUG:amqp:heartbeat_tick : for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : Prev sent/recv: None/None, now - 4/4, monotonic - 1280197.30465, last_heartbeat_sent - 1280197.30464, heartbeat int. - 60 for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:oslo.messaging._drivers.impl_rabbit:[194ebf5e-22ce-4952-ab3e-095ebec93c8e] Connected to AMQP server on rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local:5672 via [amqp] client with port 50654.
DEBUG:oslo_messaging._drivers.amqpdriver:sending reply msg_id: 53fb2fce39274242a76d60a685ba98d3 reply queue: reply_21e465af00c5445f9fc2731aae89d3ce time elapsed: 0.0266919699498s
DEBUG:amqp:heartbeat_tick : for connection 18fed046b49e4dab9a2952a9609ce039
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 18/20, now - 18/20, monotonic - 1280198.29535, last_heartbeat_sent - 1280197.29418, heartbeat int. - 60 for connection 18fed046b49e4dab9a2952a9609ce039
DEBUG:oslo_messaging._drivers.amqpdriver:received message msg_id: 79aafd372d454ce4a6cf7578780e69fb reply to reply_f07a41ba214b432bbdfbf1c48f29788a
DEBUG:amqp:heartbeat_tick : for connection 18fed046b49e4dab9a2952a9609ce039
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 18/20, now - 18/23, monotonic - 1280199.08366, last_heartbeat_sent - 1280197.29418, heartbeat int. - 60 for connection 18fed046b49e4dab9a2952a9609ce039
DEBUG:oslo_messaging._drivers.amqpdriver:sending reply msg_id: 79aafd372d454ce4a6cf7578780e69fb reply queue: reply_f07a41ba214b432bbdfbf1c48f29788a time elapsed: 0.00184379797429s
DEBUG:amqp:heartbeat_tick : for connection 18fed046b49e4dab9a2952a9609ce039
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 18/23, now - 19/23, monotonic - 1280199.08742, last_heartbeat_sent - 1280199.08741, heartbeat int. - 60 for connection 18fed046b49e4dab9a2952a9609ce039
DEBUG:amqp:heartbeat_tick : for connection 18fed046b49e4dab9a2952a9609ce039
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 19/23, now - 19/23, monotonic - 1280200.08996, last_heartbeat_sent - 1280199.08741, heartbeat int. - 60 for connection 18fed046b49e4dab9a2952a9609ce039
DEBUG:amqp:heartbeat_tick : for connection 18fed046b49e4dab9a2952a9609ce039
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 19/23, now - 19/23, monotonic - 1280202.0919, last_heartbeat_sent - 1280199.08741, heartbeat int. - 60 for connection 18fed046b49e4dab9a2952a9609ce039
DEBUG:amqp:heartbeat_tick : for connection 18fed046b49e4dab9a2952a9609ce039
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 19/23, now - 19/23, monotonic - 1280206.09362, last_heartbeat_sent - 1280199.08741, heartbeat int. - 60 for connection 18fed046b49e4dab9a2952a9609ce039
DEBUG:amqp:heartbeat_tick : for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 4/4, now - 7/7, monotonic - 1280212.30694, last_heartbeat_sent - 1280212.30692, heartbeat int. - 60 for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : for connection 18fed046b49e4dab9a2952a9609ce039
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 19/23, now - 19/23, monotonic - 1280214.09599, last_heartbeat_sent - 1280199.08741, heartbeat int. - 60 for connection 18fed046b49e4dab9a2952a9609ce039
DEBUG:amqp:heartbeat_tick : for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 7/7, now - 7/7, monotonic - 1280227.30919, last_heartbeat_sent - 1280212.30692, heartbeat int. - 60 for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:Closed channel #1
DEBUG:oslo.messaging._drivers.impl_rabbit:[7049682c-fe38-428f-aef4-5f24023db291] Received recoverable error from kombu:
Traceback (most recent call last):
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 518, in _ensured
    return fun(*args, **kwargs)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 594, in __call__
    return fun(*args, channel=channels[0], **kwargs), channels[0]
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/impl_rabbit.py", line 803, in execute_method
    method()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/impl_rabbit.py", line 1075, in _consume
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
DEBUG:oslo.messaging._drivers.impl_rabbit:[7049682c-fe38-428f-aef4-5f24023db291] Received recoverable error from kombu:
Traceback (most recent call last):
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 518, in _ensured
    return fun(*args, **kwargs)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 594, in __call__
    return fun(*args, channel=channels[0], **kwargs), channels[0]
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/impl_rabbit.py", line 803, in execute_method
    method()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/impl_rabbit.py", line 1057, in _consume
    raise self.connection.recoverable_connection_errors[0]
RecoverableConnectionError: <RecoverableConnectionError: unknown error>
ERROR:oslo.messaging._drivers.impl_rabbit:[7049682c-fe38-428f-aef4-5f24023db291] AMQP server on rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local:5672 is unreachable: <RecoverableConnectionError: unknown error>. Trying again in 1 seconds.
DEBUG:amqp:Start from server, version: 0.9, properties: {'information': 'Licensed under the MPL.  See http://www.rabbitmq.com/', 'product': 'RabbitMQ', 'copyright': 'Copyright (C) 2007-2019 Pivotal Software, Inc.', 'capabilities': {'exchange_exchange_bindings': True, 'connection.blocked': True, 'authentication_failure_close': True, 'direct_reply_to': True, 'basic.nack': True, 'per_consumer_qos': True, 'consumer_priorities': True, 'consumer_cancel_notify': True, 'publisher_confirms': True}, 'cluster_name': 'rabbit@rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local', 'platform': 'Erlang/OTP 21.3.2', 'version': '3.7.13'}, mechanisms: ['PLAIN', 'AMQPLAIN'], locales: [u'en_US']
DEBUG:amqp:using channel_id: 1
DEBUG:amqp:Channel open
DEBUG:oslo.messaging._drivers.impl_rabbit:[7049682c-fe38-428f-aef4-5f24023db291] Queue.declare: test
DEBUG:amqp:Channel open
DEBUG:amqp:Channel open
ERROR:oslo.messaging._drivers.impl_rabbit:Failed to consume message from queue: Queue.declare: (404) NOT_FOUND - queue 'test' in vhost 'neutron' process is stopped by supervisor
DEBUG:amqp:Closed channel #1
ERROR:oslo.messaging._drivers.impl_rabbit:Unable to connect to AMQP server on rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local:5672 after None tries: Queue.declare: (404) NOT_FOUND - queue 'test' in vhost 'neutron' process is stopped by supervisor
ERROR:root:Unexpected exception occurred 1 time(s)... retrying.
Traceback (most recent call last):
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_utils/excutils.py", line 250, in wrapper
    return infunc(*args, **kwargs)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/base.py", line 304, in _runner
    batch_size=self.batch_size, batch_timeout=self.batch_timeout)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/base.py", line 53, in wrapper
    message = func(in_self, timeout=watch.leftover(True))
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/amqpdriver.py", line 287, in poll
    self.conn.consume(timeout=min(self._current_timeout, left))
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/impl_rabbit.py", line 1090, in consume
    error_callback=_error_callback)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/impl_rabbit.py", line 832, in ensure
    raise exceptions.MessageDeliveryFailure(msg)
MessageDeliveryFailure: Unable to connect to AMQP server on rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local:5672 after None tries: Queue.declare: (404) NOT_FOUND - queue 'test' in vhost 'neutron' process is stopped by supervisor
DEBUG:oslo.messaging._drivers.impl_rabbit:[7049682c-fe38-428f-aef4-5f24023db291] Received recoverable error from kombu:
Traceback (most recent call last):
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 518, in _ensured
    return fun(*args, **kwargs)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 594, in __call__
    return fun(*args, channel=channels[0], **kwargs), channels[0]
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/impl_rabbit.py", line 802, in execute_method
    self._set_current_channel(channel)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/impl_rabbit.py", line 851, in _set_current_channel
    self._set_qos(new_channel)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/impl_rabbit.py", line 861, in _set_qos
    False)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/channel.py", line 1853, in basic_qos
    wait=spec.Basic.QosOk,
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/abstract_channel.py", line 56, in send_method
    raise RecoverableConnectionError('connection already closed')
RecoverableConnectionError: connection already closed
ERROR:oslo.messaging._drivers.impl_rabbit:[7049682c-fe38-428f-aef4-5f24023db291] AMQP server on rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local:5672 is unreachable: connection already closed. Trying again in 1 seconds.
DEBUG:amqp:Start from server, version: 0.9, properties: {'information': 'Licensed under the MPL.  See http://www.rabbitmq.com/', 'product': 'RabbitMQ', 'copyright': 'Copyright (C) 2007-2019 Pivotal Software, Inc.', 'capabilities': {'exchange_exchange_bindings': True, 'connection.blocked': True, 'authentication_failure_close': True, 'direct_reply_to': True, 'basic.nack': True, 'per_consumer_qos': True, 'consumer_priorities': True, 'consumer_cancel_notify': True, 'publisher_confirms': True}, 'cluster_name': 'rabbit@rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local', 'platform': 'Erlang/OTP 21.3.2', 'version': '3.7.13'}, mechanisms: ['PLAIN', 'AMQPLAIN'], locales: [u'en_US']
DEBUG:amqp:using channel_id: 1
DEBUG:amqp:Channel open
DEBUG:oslo.messaging._drivers.impl_rabbit:[7049682c-fe38-428f-aef4-5f24023db291] Queue.declare: test
DEBUG:oslo.messaging._drivers.impl_rabbit:[7049682c-fe38-428f-aef4-5f24023db291] Queue.declare: test_fanout_3be24e8dc0ac4b91b90c843d89146d2a
DEBUG:oslo.messaging._drivers.impl_rabbit:[7049682c-fe38-428f-aef4-5f24023db291] Queue.declare: test.master1
INFO:oslo.messaging._drivers.impl_rabbit:[7049682c-fe38-428f-aef4-5f24023db291] Reconnected to AMQP server on rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local:5672 via [amqp] client with port 50896.
DEBUG:amqp:heartbeat_tick : for connection 0495e82ccbab42638192f8e0d2e56de4
DEBUG:amqp:heartbeat_tick : Prev sent/recv: None/None, now - 17/17, monotonic - 1280240.55588, last_heartbeat_sent - 1280240.55586, heartbeat int. - 60 for connection 0495e82ccbab42638192f8e0d2e56de4
DEBUG:amqp:heartbeat_tick : for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 7/7, now - 7/8, monotonic - 1280242.3114, last_heartbeat_sent - 1280212.30692, heartbeat int. - 60 for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : for connection 0495e82ccbab42638192f8e0d2e56de4
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 17/17, now - 17/17, monotonic - 1280255.55709, last_heartbeat_sent - 1280240.55586, heartbeat int. - 60 for connection 0495e82ccbab42638192f8e0d2e56de4
DEBUG:amqp:heartbeat_tick : for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 7/8, now - 7/8, monotonic - 1280257.31361, last_heartbeat_sent - 1280212.30692, heartbeat int. - 60 for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 7/8, now - 7/9, monotonic - 1280272.31607, last_heartbeat_sent - 1280212.30692, heartbeat int. - 60 for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick: sending heartbeat for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : for connection 0495e82ccbab42638192f8e0d2e56de4
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 17/17, now - 17/18, monotonic - 1280283.91866, last_heartbeat_sent - 1280240.55586, heartbeat int. - 60 for connection 0495e82ccbab42638192f8e0d2e56de4
DEBUG:amqp:heartbeat_tick : for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 7/9, now - 8/9, monotonic - 1280287.31886, last_heartbeat_sent - 1280287.31885, heartbeat int. - 60 for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : for connection 0495e82ccbab42638192f8e0d2e56de4
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 17/18, now - 17/18, monotonic - 1280298.91997, last_heartbeat_sent - 1280240.55586, heartbeat int. - 60 for connection 0495e82ccbab42638192f8e0d2e56de4
DEBUG:amqp:heartbeat_tick : for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 8/9, now - 8/10, monotonic - 1280302.32143, last_heartbeat_sent - 1280287.31885, heartbeat int. - 60 for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : for connection 0495e82ccbab42638192f8e0d2e56de4
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 17/18, now - 17/19, monotonic - 1280314.45289, last_heartbeat_sent - 1280240.55586, heartbeat int. - 60 for connection 0495e82ccbab42638192f8e0d2e56de4
DEBUG:amqp:heartbeat_tick: sending heartbeat for connection 0495e82ccbab42638192f8e0d2e56de4
DEBUG:amqp:heartbeat_tick : for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 8/10, now - 8/10, monotonic - 1280317.3236, last_heartbeat_sent - 1280287.31885, heartbeat int. - 60 for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 8/10, now - 8/11, monotonic - 1280332.32629, last_heartbeat_sent - 1280287.31885, heartbeat int. - 60 for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : for connection 0495e82ccbab42638192f8e0d2e56de4
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 17/19, now - 18/20, monotonic - 1280344.44407, last_heartbeat_sent - 1280344.44398, heartbeat int. - 60 for connection 0495e82ccbab42638192f8e0d2e56de4
DEBUG:amqp:heartbeat_tick : for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 8/11, now - 8/11, monotonic - 1280347.32857, last_heartbeat_sent - 1280287.31885, heartbeat int. - 60 for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick: sending heartbeat for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : for connection 0495e82ccbab42638192f8e0d2e56de4
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 18/20, now - 18/20, monotonic - 1280347.92094, last_heartbeat_sent - 1280344.44398, heartbeat int. - 60 for connection 0495e82ccbab42638192f8e0d2e56de4
DEBUG:amqp:heartbeat_tick : for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 8/11, now - 9/12, monotonic - 1280362.33132, last_heartbeat_sent - 1280362.3313, heartbeat int. - 60 for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : for connection 0495e82ccbab42638192f8e0d2e56de4
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 18/20, now - 18/21, monotonic - 1280374.43514, last_heartbeat_sent - 1280344.44398, heartbeat int. - 60 for connection 0495e82ccbab42638192f8e0d2e56de4
DEBUG:amqp:heartbeat_tick : for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 9/12, now - 9/12, monotonic - 1280377.33363, last_heartbeat_sent - 1280362.3313, heartbeat int. - 60 for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 9/12, now - 9/13, monotonic - 1280392.33614, last_heartbeat_sent - 1280362.3313, heartbeat int. - 60 for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : for connection 0495e82ccbab42638192f8e0d2e56de4
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 18/21, now - 18/22, monotonic - 1280404.42594, last_heartbeat_sent - 1280344.44398, heartbeat int. - 60 for connection 0495e82ccbab42638192f8e0d2e56de4
DEBUG:amqp:heartbeat_tick : for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 9/13, now - 9/13, monotonic - 1280407.33826, last_heartbeat_sent - 1280362.3313, heartbeat int. - 60 for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 9/13, now - 9/14, monotonic - 1280422.34062, last_heartbeat_sent - 1280362.3313, heartbeat int. - 60 for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick: sending heartbeat for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : for connection 0495e82ccbab42638192f8e0d2e56de4
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 18/22, now - 18/23, monotonic - 1280434.41954, last_heartbeat_sent - 1280344.44398, heartbeat int. - 60 for connection 0495e82ccbab42638192f8e0d2e56de4
DEBUG:amqp:heartbeat_tick: sending heartbeat for connection 0495e82ccbab42638192f8e0d2e56de4
DEBUG:amqp:heartbeat_tick : for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 9/14, now - 10/14, monotonic - 1280437.34334, last_heartbeat_sent - 1280437.34333, heartbeat int. - 60 for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : for connection 0495e82ccbab42638192f8e0d2e56de4
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 18/23, now - 19/23, monotonic - 1280449.42111, last_heartbeat_sent - 1280449.4211, heartbeat int. - 60 for connection 0495e82ccbab42638192f8e0d2e56de4
DEBUG:amqp:heartbeat_tick : for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 10/14, now - 10/15, monotonic - 1280452.34576, last_heartbeat_sent - 1280437.34333, heartbeat int. - 60 for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : for connection 0495e82ccbab42638192f8e0d2e56de4
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 19/23, now - 19/24, monotonic - 1280464.43227, last_heartbeat_sent - 1280449.4211, heartbeat int. - 60 for connection 0495e82ccbab42638192f8e0d2e56de4
DEBUG:amqp:heartbeat_tick : for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 10/15, now - 10/15, monotonic - 1280467.34807, last_heartbeat_sent - 1280437.34333, heartbeat int. - 60 for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : for connection 0495e82ccbab42638192f8e0d2e56de4
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 19/24, now - 19/24, monotonic - 1280475.92229, last_heartbeat_sent - 1280449.4211, heartbeat int. - 60 for connection 0495e82ccbab42638192f8e0d2e56de4
DEBUG:amqp:heartbeat_tick : for connection 2e5868880b6f421095b0905eddf8ca47
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 10/15, now - 10/16, monotonic - 1280482.3504, last_heartbeat_sent - 1280437.34333, heartbeat int. - 60 for connection 2e5868880b6f421095b0905eddf8ca47
```

### Clientside Log

```log
(test) root@master1:/tmp/sjt/dev-demo/dev_demo/openstack/rabbit/oslo_messaging# python rpc_client.py --config-file ./config
DEBUG:stevedore.extension:found extension EntryPoint.parse('amqp = oslo_messaging._drivers.impl_amqp1:ProtonDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('kafka = oslo_messaging._drivers.impl_kafka:KafkaDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('kombu = oslo_messaging._drivers.impl_rabbit:RabbitDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('rabbit = oslo_messaging._drivers.impl_rabbit:RabbitDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('fake = oslo_messaging._drivers.impl_fake:FakeDriver')
DEBUG:stevedore.extension:found extension EntryPoint.parse('zmq = oslo_messaging._drivers.impl_zmq:ZmqDriver')
DEBUG:oslo.messaging._drivers.pool:Pool creating new connection
DEBUG:oslo.messaging._drivers.impl_rabbit:[8cd5ef24-a7c9-435c-801a-2224fe2adb44] Connecting to AMQP server on rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local:5672
DEBUG:amqp:Start from server, version: 0.9, properties: {'information': 'Licensed under the MPL.  See http://www.rabbitmq.com/', 'product': 'RabbitMQ', 'copyright': 'Copyright (C) 2007-2019 Pivotal Software, Inc.', 'capabilities': {'exchange_exchange_bindings': True, 'connection.blocked': True, 'authentication_failure_close': True, 'direct_reply_to': True, 'basic.nack': True, 'per_consumer_qos': True, 'consumer_priorities': True, 'consumer_cancel_notify': True, 'publisher_confirms': True}, 'cluster_name': 'rabbit@rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local', 'platform': 'Erlang/OTP 21.3.2', 'version': '3.7.13'}, mechanisms: ['PLAIN', 'AMQPLAIN'], locales: [u'en_US']
DEBUG:amqp:using channel_id: 1
DEBUG:amqp:Channel open
DEBUG:oslo.messaging._drivers.impl_rabbit:[8cd5ef24-a7c9-435c-801a-2224fe2adb44] Connected to AMQP server on rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local:5672 via [amqp] client with port 50930.
DEBUG:oslo.messaging._drivers.impl_rabbit:[8cd5ef24-a7c9-435c-801a-2224fe2adb44] Queue.declare: reply_1941f911a51c4cf3b20204e47695a7c7
DEBUG:oslo.messaging._drivers.pool:Pool creating new connection
DEBUG:oslo.messaging._drivers.impl_rabbit:[b740a764-e026-4ee8-87e6-c6cd22ffacf3] Connecting to AMQP server on rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local:5672
DEBUG:amqp:heartbeat_tick : for connection eb95f7d368d348d6954c2b233cf3beb9
DEBUG:amqp:heartbeat_tick : Prev sent/recv: None/None, now - 9/9, monotonic - 1280245.78746, last_heartbeat_sent - 1280245.78743, heartbeat int. - 60 for connection eb95f7d368d348d6954c2b233cf3beb9
DEBUG:amqp:heartbeat_tick : for connection eb95f7d368d348d6954c2b233cf3beb9
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 9/9, now - 9/9, monotonic - 1280245.79, last_heartbeat_sent - 1280245.78743, heartbeat int. - 60 for connection eb95f7d368d348d6954c2b233cf3beb9
DEBUG:amqp:Start from server, version: 0.9, properties: {'information': 'Licensed under the MPL.  See http://www.rabbitmq.com/', 'product': 'RabbitMQ', 'copyright': 'Copyright (C) 2007-2019 Pivotal Software, Inc.', 'capabilities': {'exchange_exchange_bindings': True, 'connection.blocked': True, 'authentication_failure_close': True, 'direct_reply_to': True, 'basic.nack': True, 'per_consumer_qos': True, 'consumer_priorities': True, 'consumer_cancel_notify': True, 'publisher_confirms': True}, 'cluster_name': 'rabbit@rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local', 'platform': 'Erlang/OTP 21.3.2', 'version': '3.7.13'}, mechanisms: ['PLAIN', 'AMQPLAIN'], locales: [u'en_US']
DEBUG:amqp:using channel_id: 1
DEBUG:amqp:Channel open
DEBUG:oslo.messaging._drivers.impl_rabbit:[b740a764-e026-4ee8-87e6-c6cd22ffacf3] Connected to AMQP server on rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local:5672 via [amqp] client with port 50932.
DEBUG:amqp:heartbeat_tick : for connection bf5289f628a04f76b3af30311d771aa7
DEBUG:oslo_messaging._drivers.amqpdriver:CALL msg_id: a94cb116335942f989e958e923dbe729 exchange 'test' topic 'test'
DEBUG:amqp:heartbeat_tick : Prev sent/recv: None/None, now - 4/4, monotonic - 1280245.8007, last_heartbeat_sent - 1280245.80065, heartbeat int. - 60 for connection bf5289f628a04f76b3af30311d771aa7
DEBUG:amqp:heartbeat_tick : for connection eb95f7d368d348d6954c2b233cf3beb9
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 9/9, now - 9/9, monotonic - 1280246.79252, last_heartbeat_sent - 1280245.78743, heartbeat int. - 60 for connection eb95f7d368d348d6954c2b233cf3beb9
DEBUG:amqp:heartbeat_tick : for connection eb95f7d368d348d6954c2b233cf3beb9
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 9/9, now - 9/9, monotonic - 1280248.79596, last_heartbeat_sent - 1280245.78743, heartbeat int. - 60 for connection eb95f7d368d348d6954c2b233cf3beb9
DEBUG:amqp:heartbeat_tick : for connection eb95f7d368d348d6954c2b233cf3beb9
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 9/9, now - 9/9, monotonic - 1280252.79936, last_heartbeat_sent - 1280245.78743, heartbeat int. - 60 for connection eb95f7d368d348d6954c2b233cf3beb9
DEBUG:amqp:heartbeat_tick : for connection eb95f7d368d348d6954c2b233cf3beb9
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 9/9, now - 9/9, monotonic - 1280260.8021, last_heartbeat_sent - 1280245.78743, heartbeat int. - 60 for connection eb95f7d368d348d6954c2b233cf3beb9
DEBUG:amqp:heartbeat_tick : for connection bf5289f628a04f76b3af30311d771aa7
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 4/4, now - 7/7, monotonic - 1280260.80333, last_heartbeat_sent - 1280260.80331, heartbeat int. - 60 for connection bf5289f628a04f76b3af30311d771aa7
DEBUG:amqp:heartbeat_tick : for connection bf5289f628a04f76b3af30311d771aa7
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 7/7, now - 7/7, monotonic - 1280275.80534, last_heartbeat_sent - 1280260.80331, heartbeat int. - 60 for connection bf5289f628a04f76b3af30311d771aa7
DEBUG:amqp:heartbeat_tick : for connection eb95f7d368d348d6954c2b233cf3beb9
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 9/9, now - 9/10, monotonic - 1280290.7583, last_heartbeat_sent - 1280245.78743, heartbeat int. - 60 for connection eb95f7d368d348d6954c2b233cf3beb9
DEBUG:amqp:heartbeat_tick : for connection bf5289f628a04f76b3af30311d771aa7
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 7/7, now - 7/8, monotonic - 1280290.80746, last_heartbeat_sent - 1280260.80331, heartbeat int. - 60 for connection bf5289f628a04f76b3af30311d771aa7
DEBUG:amqp:heartbeat_tick : for connection bf5289f628a04f76b3af30311d771aa7
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 7/8, now - 7/8, monotonic - 1280305.80969, last_heartbeat_sent - 1280260.80331, heartbeat int. - 60 for connection bf5289f628a04f76b3af30311d771aa7
DEBUG:amqp:heartbeat_tick : for connection eb95f7d368d348d6954c2b233cf3beb9
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 9/10, now - 9/11, monotonic - 1280320.74877, last_heartbeat_sent - 1280245.78743, heartbeat int. - 60 for connection eb95f7d368d348d6954c2b233cf3beb9
DEBUG:amqp:heartbeat_tick: sending heartbeat for connection eb95f7d368d348d6954c2b233cf3beb9
DEBUG:amqp:heartbeat_tick : for connection bf5289f628a04f76b3af30311d771aa7
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 7/8, now - 7/9, monotonic - 1280320.81214, last_heartbeat_sent - 1280260.80331, heartbeat int. - 60 for connection bf5289f628a04f76b3af30311d771aa7
DEBUG:amqp:heartbeat_tick: sending heartbeat for connection bf5289f628a04f76b3af30311d771aa7
DEBUG:amqp:heartbeat_tick : for connection eb95f7d368d348d6954c2b233cf3beb9
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 9/11, now - 10/11, monotonic - 1280322.75995, last_heartbeat_sent - 1280322.75993, heartbeat int. - 60 for connection eb95f7d368d348d6954c2b233cf3beb9
```

## Tables

| tainit node  | Successes | Failures |
|---|-------|---|
| 8.1.3 |    4   |  6/5 |
| 10.2.0 |      |   |

| immediate comeback without taint  | Successes | Failures |
|---|-------|---|
| 8.1.3 |   4    | 6/2(*) |
| 10.2.0 |  4   |  4/3 |

* Even if new queue is created on the same node as connection, still it could be unresponsive
* `list_unresponsive_queues` yields an **empty** list
* `node_health_check` also correctly returns.
* restart rpc server does not alleviate problem (see failures colume)

## Observation

Interestingly, this time rpc calls are successfully made by rpc client, if oslo.messaging is using **10.2.0**