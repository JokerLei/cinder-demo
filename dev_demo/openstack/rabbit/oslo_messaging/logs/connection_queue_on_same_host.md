# Connection & Queue On Same Host

## Setup

* Queue and Connection are on different host
* Rpc server runs on one rabbit node (rabbitmq-rabbitmq-0)
* Manually remove **rabbitmq-rabbitmq-0** by `kubectl delete -n openstack pod rabbitmq-rabbitmq-0`
* Test by oslo messaging **10.2.0**
* Openstack Rocky uses oslo.messaging **8.1.3**

## Serverside Log

```log
DEBUG:amqp:heartbeat_tick : for connection 6cff33739168443bb8e92f4d7949154f
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 6/6, now - 6/6, monotonic - 1265056.52356, last_heartbeat_sent - 1265041.52159, heartbeat int. - 60 for connection 6cff33739168443bb8e92f4d7949154f
DEBUG:amqp:heartbeat_tick : for connection ed5718c58cbe44559cc64d2365914162
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 19/23, now - 19/23, monotonic - 1265057.51833, last_heartbeat_sent - 1265026.49568, heartbeat int. - 60 for connection ed5718c58cbe44559cc64d2365914162
DEBUG:oslo.messaging._drivers.impl_rabbit:[1e839b1e-3fcd-4bc4-a938-f31392ebc57b] Received recoverable error from kombu:
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
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/connection.py", line 646, in _on_close
    self._x_close_ok()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/connection.py", line 661, in _x_close_ok
    self.send_method(spec.Connection.CloseOk, callback=self._on_close_ok)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/abstract_channel.py", line 59, in send_method
    conn.frame_writer(1, self.channel_id, sig, args, content)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/method_framing.py", line 172, in write_frame
    write(view[:offset])
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/transport.py", line 284, in write
    self._write(s)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/eventlet/greenio/base.py", line 390, in sendall
    tail = self.send(data, flags)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/eventlet/greenio/base.py", line 384, in send
    return self._send_loop(self.fd.send, data, flags)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/eventlet/greenio/base.py", line 371, in _send_loop
    return send_method(data, *args)
error: [Errno 104] Connection reset by peer
ERROR:oslo.messaging._drivers.impl_rabbit:[1e839b1e-3fcd-4bc4-a938-f31392ebc57b] AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672 is unreachable: [Errno 104] Connection reset by peer. Trying again in 1 seconds.
DEBUG:oslo.messaging._drivers.impl_rabbit:[1e839b1e-3fcd-4bc4-a938-f31392ebc57b] Received recoverable error from kombu:
Traceback (most recent call last):
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/utils/functional.py", line 343, in retry_over_time
    return fun(*args, **kwargs)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 283, in connect
    return self.connection
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 837, in connection
    self._connection = self._establish_connection()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 792, in _establish_connection
    conn = self.transport.establish_connection()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/transport/pyamqp.py", line 130, in establish_connection
    conn.connect()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/connection.py", line 311, in connect
    self.transport.connect()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/transport.py", line 77, in connect
    self._connect(self.host, self.port, self.connect_timeout)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/transport.py", line 148, in _connect
    "failed to resolve broker hostname"))
error: failed to resolve broker hostname
ERROR:oslo.messaging._drivers.impl_rabbit:[1e839b1e-3fcd-4bc4-a938-f31392ebc57b] AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672 is unreachable: failed to resolve broker hostname. Trying again in 2 seconds.
DEBUG:amqp:heartbeat_tick : for connection 6cff33739168443bb8e92f4d7949154f
DEBUG:amqp:heartbeat_tick : Prev sent/recv: 6/6, now - 6/7, monotonic - 1265071.52629, last_heartbeat_sent - 1265041.52159, heartbeat int. - 60 for connection 6cff33739168443bb8e92f4d7949154f
INFO:oslo.messaging._drivers.impl_rabbit:A recoverable connection/channel error occurred, trying to reconnect: [Errno 104] Connection reset by peer
ERROR:oslo.messaging._drivers.impl_rabbit:Connection failed: failed to resolve broker hostname (retrying in 2.0 seconds)
DEBUG:oslo.messaging._drivers.impl_rabbit:[1e839b1e-3fcd-4bc4-a938-f31392ebc57b] Received recoverable error from kombu:
Traceback (most recent call last):
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/utils/functional.py", line 343, in retry_over_time
    return fun(*args, **kwargs)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 283, in connect
    return self.connection
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 837, in connection
    self._connection = self._establish_connection()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 792, in _establish_connection
    conn = self.transport.establish_connection()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/transport/pyamqp.py", line 130, in establish_connection
    conn.connect()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/connection.py", line 311, in connect
    self.transport.connect()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/transport.py", line 77, in connect
    self._connect(self.host, self.port, self.connect_timeout)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/transport.py", line 148, in _connect
    "failed to resolve broker hostname"))
error: failed to resolve broker hostname
ERROR:oslo.messaging._drivers.impl_rabbit:[1e839b1e-3fcd-4bc4-a938-f31392ebc57b] AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672 is unreachable: failed to resolve broker hostname. Trying again in 4 seconds.
ERROR:oslo.messaging._drivers.impl_rabbit:Connection failed: failed to resolve broker hostname (retrying in 4.0 seconds)
DEBUG:oslo.messaging._drivers.impl_rabbit:[1e839b1e-3fcd-4bc4-a938-f31392ebc57b] Received recoverable error from kombu:
Traceback (most recent call last):
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/utils/functional.py", line 343, in retry_over_time
    return fun(*args, **kwargs)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 283, in connect
    return self.connection
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 837, in connection
    self._connection = self._establish_connection()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 792, in _establish_connection
    conn = self.transport.establish_connection()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/transport/pyamqp.py", line 130, in establish_connection
    conn.connect()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/connection.py", line 311, in connect
    self.transport.connect()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/transport.py", line 77, in connect
    self._connect(self.host, self.port, self.connect_timeout)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/transport.py", line 148, in _connect
    "failed to resolve broker hostname"))
error: failed to resolve broker hostname
ERROR:oslo.messaging._drivers.impl_rabbit:[1e839b1e-3fcd-4bc4-a938-f31392ebc57b] AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672 is unreachable: failed to resolve broker hostname. Trying again in 6 seconds.
ERROR:oslo.messaging._drivers.impl_rabbit:Connection failed: failed to resolve broker hostname (retrying in 6.0 seconds)
DEBUG:oslo.messaging._drivers.impl_rabbit:[1e839b1e-3fcd-4bc4-a938-f31392ebc57b] Received recoverable error from kombu:
Traceback (most recent call last):
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/utils/functional.py", line 343, in retry_over_time
    return fun(*args, **kwargs)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 283, in connect
    return self.connection
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 837, in connection
    self._connection = self._establish_connection()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 792, in _establish_connection
    conn = self.transport.establish_connection()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/transport/pyamqp.py", line 130, in establish_connection
    conn.connect()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/connection.py", line 311, in connect
    self.transport.connect()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/transport.py", line 77, in connect
    self._connect(self.host, self.port, self.connect_timeout)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/transport.py", line 148, in _connect
    "failed to resolve broker hostname"))
error: failed to resolve broker hostname
ERROR:oslo.messaging._drivers.impl_rabbit:[1e839b1e-3fcd-4bc4-a938-f31392ebc57b] AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672 is unreachable: failed to resolve broker hostname. Trying again in 8 seconds.
ERROR:oslo.messaging._drivers.impl_rabbit:Connection failed: failed to resolve broker hostname (retrying in 8.0 seconds)
DEBUG:oslo.messaging._drivers.impl_rabbit:[1e839b1e-3fcd-4bc4-a938-f31392ebc57b] Received recoverable error from kombu:
Traceback (most recent call last):
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/utils/functional.py", line 343, in retry_over_time
    return fun(*args, **kwargs)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 283, in connect
    return self.connection
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 837, in connection
    self._connection = self._establish_connection()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 792, in _establish_connection
    conn = self.transport.establish_connection()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/transport/pyamqp.py", line 130, in establish_connection
    conn.connect()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/connection.py", line 311, in connect
    self.transport.connect()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/transport.py", line 77, in connect
    self._connect(self.host, self.port, self.connect_timeout)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/transport.py", line 148, in _connect
    "failed to resolve broker hostname"))
error: failed to resolve broker hostname
DEBUG:oslo.messaging._drivers.impl_rabbit:[1e839b1e-3fcd-4bc4-a938-f31392ebc57b] Received recoverable error from kombu:
Traceback (most recent call last):
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 518, in _ensured
    return fun(*args, **kwargs)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 594, in __call__
    return fun(*args, channel=channels[0], **kwargs), channels[0]
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/impl_rabbit.py", line 798, in execute_method
    method()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/oslo_messaging/_drivers/impl_rabbit.py", line 1079, in _consume
    raise self.connection.recoverable_connection_errors[0]
RecoverableConnectionError: <RecoverableConnectionError: unknown error>
ERROR:oslo.messaging._drivers.impl_rabbit:[1e839b1e-3fcd-4bc4-a938-f31392ebc57b] AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672 is unreachable: <RecoverableConnectionError: unknown error>. Trying again in 1 seconds.
DEBUG:oslo.messaging._drivers.impl_rabbit:[1e839b1e-3fcd-4bc4-a938-f31392ebc57b] Received recoverable error from kombu:
Traceback (most recent call last):
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/utils/functional.py", line 343, in retry_over_time
    return fun(*args, **kwargs)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 283, in connect
    return self.connection
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 837, in connection
    self._connection = self._establish_connection()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 792, in _establish_connection
    conn = self.transport.establish_connection()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/transport/pyamqp.py", line 130, in establish_connection
    conn.connect()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/connection.py", line 311, in connect
    self.transport.connect()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/transport.py", line 77, in connect
    self._connect(self.host, self.port, self.connect_timeout)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/transport.py", line 148, in _connect
    "failed to resolve broker hostname"))
error: failed to resolve broker hostname
ERROR:oslo.messaging._drivers.impl_rabbit:[1e839b1e-3fcd-4bc4-a938-f31392ebc57b] AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672 is unreachable: failed to resolve broker hostname. Trying again in 2 seconds.
ERROR:oslo.messaging._drivers.impl_rabbit:Connection failed: failed to resolve broker hostname (retrying in 10.0 seconds)
DEBUG:oslo.messaging._drivers.impl_rabbit:[1e839b1e-3fcd-4bc4-a938-f31392ebc57b] Received recoverable error from kombu:
Traceback (most recent call last):
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/utils/functional.py", line 343, in retry_over_time
    return fun(*args, **kwargs)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 283, in connect
    return self.connection
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 837, in connection
    self._connection = self._establish_connection()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 792, in _establish_connection
    conn = self.transport.establish_connection()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/transport/pyamqp.py", line 130, in establish_connection
    conn.connect()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/connection.py", line 311, in connect
    self.transport.connect()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/transport.py", line 77, in connect
    self._connect(self.host, self.port, self.connect_timeout)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/transport.py", line 148, in _connect
    "failed to resolve broker hostname"))
error: failed to resolve broker hostname
ERROR:oslo.messaging._drivers.impl_rabbit:[1e839b1e-3fcd-4bc4-a938-f31392ebc57b] AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672 is unreachable: failed to resolve broker hostname. Trying again in 4 seconds.
DEBUG:oslo.messaging._drivers.impl_rabbit:[1e839b1e-3fcd-4bc4-a938-f31392ebc57b] Received recoverable error from kombu:
Traceback (most recent call last):
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/utils/functional.py", line 343, in retry_over_time
    return fun(*args, **kwargs)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 283, in connect
    return self.connection
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 837, in connection
    self._connection = self._establish_connection()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 792, in _establish_connection
    conn = self.transport.establish_connection()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/transport/pyamqp.py", line 130, in establish_connection
    conn.connect()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/connection.py", line 311, in connect
    self.transport.connect()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/transport.py", line 77, in connect
    self._connect(self.host, self.port, self.connect_timeout)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/transport.py", line 148, in _connect
    "failed to resolve broker hostname"))
error: failed to resolve broker hostname
ERROR:oslo.messaging._drivers.impl_rabbit:[1e839b1e-3fcd-4bc4-a938-f31392ebc57b] AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672 is unreachable: failed to resolve broker hostname. Trying again in 6 seconds.
ERROR:oslo.messaging._drivers.impl_rabbit:Connection failed: failed to resolve broker hostname (retrying in 12.0 seconds)
DEBUG:oslo.messaging._drivers.impl_rabbit:[1e839b1e-3fcd-4bc4-a938-f31392ebc57b] Received recoverable error from kombu:
Traceback (most recent call last):
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/utils/functional.py", line 343, in retry_over_time
    return fun(*args, **kwargs)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 283, in connect
    return self.connection
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 837, in connection
    self._connection = self._establish_connection()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 792, in _establish_connection
    conn = self.transport.establish_connection()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/transport/pyamqp.py", line 130, in establish_connection
    conn.connect()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/connection.py", line 311, in connect
    self.transport.connect()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/transport.py", line 77, in connect
    self._connect(self.host, self.port, self.connect_timeout)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/transport.py", line 148, in _connect
    "failed to resolve broker hostname"))
error: failed to resolve broker hostname
ERROR:oslo.messaging._drivers.impl_rabbit:[1e839b1e-3fcd-4bc4-a938-f31392ebc57b] AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672 is unreachable: failed to resolve broker hostname. Trying again in 8 seconds.
DEBUG:oslo.messaging._drivers.impl_rabbit:[1e839b1e-3fcd-4bc4-a938-f31392ebc57b] Received recoverable error from kombu:
Traceback (most recent call last):
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/utils/functional.py", line 343, in retry_over_time
    return fun(*args, **kwargs)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 283, in connect
    return self.connection
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 837, in connection
    self._connection = self._establish_connection()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/connection.py", line 792, in _establish_connection
    conn = self.transport.establish_connection()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/kombu/transport/pyamqp.py", line 130, in establish_connection
    conn.connect()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/connection.py", line 311, in connect
    self.transport.connect()
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/transport.py", line 77, in connect
    self._connect(self.host, self.port, self.connect_timeout)
  File "/tmp/sjt/test/local/lib/python2.7/site-packages/amqp/transport.py", line 148, in _connect
    "failed to resolve broker hostname"))
error: failed to resolve broker hostname
ERROR:oslo.messaging._drivers.impl_rabbit:[1e839b1e-3fcd-4bc4-a938-f31392ebc57b] AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672 is unreachable: failed to resolve broker hostname. Trying again in 10 seconds.
ERROR:oslo.messaging._drivers.impl_rabbit:Connection failed: failed to resolve broker hostname (retrying in 14.0 seconds)
DEBUG:amqp:Start from server, version: 0.9, properties: {'information': 'Licensed under the MPL.  See http://www.rabbitmq.com/', 'product': 'RabbitMQ', 'copyright': 'Copyright (C) 2007-2019 Pivotal Software, Inc.', 'capabilities': {'exchange_exchange_bindings': True, 'connection.blocked': True, 'authentication_failure_close': True, 'direct_reply_to': True, 'basic.nack': True, 'per_consumer_qos': True, 'consumer_priorities': True, 'consumer_cancel_notify': True, 'publisher_confirms': True}, 'cluster_name': 'rabbit@rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local', 'platform': 'Erlang/OTP 21.3.2', 'version': '3.7.13'}, mechanisms: ['PLAIN', 'AMQPLAIN'], locales: [u'en_US']
DEBUG:amqp:using channel_id: 1
DEBUG:amqp:Channel open
DEBUG:oslo.messaging._drivers.impl_rabbit:[1e839b1e-3fcd-4bc4-a938-f31392ebc57b] Queue.declare: test_fanout_68f3253bce83452b866a1fbf1e6f55b5
DEBUG:oslo.messaging._drivers.impl_rabbit:[1e839b1e-3fcd-4bc4-a938-f31392ebc57b] Queue.declare: test
DEBUG:oslo.messaging._drivers.impl_rabbit:[1e839b1e-3fcd-4bc4-a938-f31392ebc57b] Queue.declare: test.master1
INFO:oslo.messaging._drivers.impl_rabbit:[1e839b1e-3fcd-4bc4-a938-f31392ebc57b] Reconnected to AMQP server on rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local:5672 via [amqp] client with port 51500.
DEBUG:amqp:heartbeat_tick : for connection f5484fc5395b4a7399350c80d78be648
DEBUG:amqp:heartbeat_tick : Prev sent/recv: None/None, now - 17/17, monotonic - 1265121.19655, last_heartbeat_sent - 1265121.19654, heartbeat int. - 60 for connection f5484fc5395b4a7399350c80d78be648
DEBUG:amqp:Start from server, version: 0.9, properties: {'information': 'Licensed under the MPL.  See http://www.rabbitmq.com/', 'product': 'RabbitMQ', 'copyright': 'Copyright (C) 2007-2019 Pivotal Software, Inc.', 'capabilities': {'exchange_exchange_bindings': True, 'connection.blocked': True, 'authentication_failure_close': True, 'direct_reply_to': True, 'basic.nack': True, 'per_consumer_qos': True, 'consumer_priorities': True, 'consumer_cancel_notify': True, 'publisher_confirms': True}, 'cluster_name': 'rabbit@rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local', 'platform': 'Erlang/OTP 21.3.2', 'version': '3.7.13'}, mechanisms: ['PLAIN', 'AMQPLAIN'], locales: [u'en_US']
```

Here are output generated by **rabbitmqctl** before and after the pod removal. Clearly, although queues disappear for a short amount of time, it successfully comes back in the end and located on a different node.

```console
rabbitmq@rabbitmq-rabbitmq-0:/$ rabbitmqctl list_connections | egrep 10.151.161.0
neutron	10.151.161.0	43416	running
rabbitmq@rabbitmq-rabbitmq-0:/$ rabbitmqctl list_connections pid | egrep 10.151.161.0
rabbitmq@rabbitmq-rabbitmq-0:/$ rabbitmqctl list_connections pid peer_host | egrep 10.151.161.0
<rabbit@rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local.3.24625.5>	10.151.161.0
rabbitmq@rabbitmq-rabbitmq-0:/$ rabbitmqctl list_channels pid connection | grep 24625
<rabbit@rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local.3.24634.5>	<rabbit@rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local.3.24625.5>
rabbitmq@rabbitmq-rabbitmq-0:/$ rabbitmqctl list_channels pid connection vhost | grep 24625
<rabbit@rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local.3.24634.5>	<rabbit@rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local.3.24625.5>	neutron
rabbitmq@rabbitmq-rabbitmq-0:/$ rabbitmqctl list_consumers -p neutron | grep 24634
test.master1	<rabbit@rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local.3.24634.5>	2	true	64	[]
test	<rabbit@rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local.3.24634.5>	1	true	64	[]
test_fanout_68f3253bce83452b866a1fbf1e6f55b5	<rabbit@rabbitmq-rabbitmq-2.rabbitmq.openstack.svc.cluster.local.3.24634.5>	3	true	64	[]
rabbitmq@rabbitmq-rabbitmq-0:/$ rabbitmqctl list_consumers -p neutron | grep 24634
rabbitmq@rabbitmq-rabbitmq-0:/$ rabbitmqctl list_queues -p neutron | grep test
test.master1	0
test	0
test_fanout_68f3253bce83452b866a1fbf1e6f55b5	0
rabbitmq@rabbitmq-rabbitmq-0:/$ rabbitmqctl list_queues -p neutron | grep test
test.master1	0
test	0
test_fanout_68f3253bce83452b866a1fbf1e6f55b5	0
rabbitmq@rabbitmq-rabbitmq-0:/$ rabbitmqctl list_queues -p neutron pid name | grep test
<rabbit@rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local.1.3231.206>	test.master1
<rabbit@rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local.1.25876.205>	test
<rabbit@rabbitmq-rabbitmq-0.rabbitmq.openstack.svc.cluster.local.1.7192.244>	test_fanout_68f3253bce83452b866a1fbf1e6f55b5

```

Initially, rpc server fails to resolve IP address of the given host, as a result it experiences several back off timeout and after pod comes back it could finally declare and receive messages from messaging queue server.

## Pods Status

But still some pods are not working correctly, and describe pods returns liveness probe failed because of rpc timeout

```log
root@master1:~# kubectl get pods -n openstack -owide | awk '{if ($4 > 0) print $0}'
NAME                                             READY   STATUS      RESTARTS   AGE     IP               NODE     NOMINATED NODE   READINESS GATES
neutron-l3-agent-snat-default-2m7nm              1/1     Running     1          138m    172.30.0.12      slave4   <none>           <none>
neutron-l3-agent-snat-default-2sdhw              1/1     Running     1          140m    172.30.0.13      slave5   <none>           <none>
neutron-l3-agent-snat-default-8n8mz              1/1     Running     1          137m    172.30.0.14      slave6   <none>           <none>
neutron-ovs-agent-default-bc882                  1/1     Running     1          138m    172.30.0.14      slave6   <none>           <none>
neutron-ovs-agent-default-kfjlz                  1/1     Running     1          137m    172.30.0.13      slave5   <none>           <none>
nova-compute-default-kk4tv                       0/1     Running     37         2d1h    172.30.0.4       slave7   <none>           <none>
nova-conductor-55b8c87745-97688                  0/1     Running     3          2d1h    10.151.190.159   slave6   <none>           <none>
nova-conductor-55b8c87745-mlfcf                  0/1     Running     98         21h     10.151.174.3     slave5   <none>           <none>
nova-conductor-55b8c87745-ncprx                  1/1     Running     105        2d1h    10.151.26.216    slave4   <none>           <none>
nova-consoleauth-787f56d969-69tqw                0/1     Running     30         2d1h    10.151.174.247   slave5   <none>           <none>
nova-consoleauth-787f56d969-cnwtv                1/1     Running     6          2d1h    10.151.26.218    slave4   <none>           <none>
nova-consoleauth-787f56d969-r6d47                1/1     Running     18         2d1h    10.151.190.162   slave6   <none>           <none>
nova-scheduler-778dd5cfb9-4tnqh                  0/1     Running     124        21h     10.151.190.188   slave6   <none>           <none>
nova-scheduler-778dd5cfb9-lz4mq                  0/1     Running     123        21h     10.151.174.235   slave5   <none>           <none>
nova-scheduler-778dd5cfb9-rp9jt                  0/1     Running     97         21h     10.151.26.46     slave4   <none>           <none>
```
