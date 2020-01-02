# Debug Oslo Messaging Issue

## Amqp Timeout After Rabbit Node Crash

### Background

* Deploy in kubernetes: version 1.14.3 (verify by `kubectl version`)
* Rabbitmq version: 3.7.13 (verify by `rabbitmqctl status`)

### Problem Description

If I manually delete a pod, for example *rabbitmq-rabbitmq-0*, after kubernets controller manager brings it back again, some rpc services will **not** correctly respond to a **call** method.

It seems that under most of the cases, problem could be alleviated by manually clearing queues

> Supposedly removing specific queues will be more preferable

If manually purging queues does not work out, then problematic agents has to be manually deleted

#### Error Logs

For nova conductor, some error logs look like below

```ini
Timed out waiting for a reply to message ID 70b5b5ce51004a9a95d9a2ab3a68fac2', u'code': 500, u'details': u'  File "/var/lib/openstack/local/lib/python2.7/site-packages/nova/conductor/manager.py", line 1237, in schedule_and_build_instances\n    instance_uuids, return_alternates=True)\n  File "/var/lib/openstack/local/lib/python2.7/site-packages/nova/conductor/manager.py", line 750, in _schedule_instances\n    return_alternates=return_alternates)\n  File "/var/lib/openstack/local/lib/python2.7/site-packages/nova/scheduler/client/__init__.py", line 50, in select_destinations\n    instance_uuids, return_objects, return_alternates)\n  File "/var/lib/openstack/local/lib/python2.7/site-packages/nova/scheduler/client/__init__.py", line 35, in __run_method\n    return getattr(self.instance, __name)(*args, **kwargs)\n  File "/var/lib/openstack/local/lib/python2.7/site-packages/nova/scheduler/client/query.py", line 42, in select_destinations\n    instance_uuids, return_objects, return_alternates)\n  File "/var/lib/openstack/local/lib/python2.7/site-packages/nova/scheduler/rpcapi.py", line 160, in select_destinations\n    return cctxt.call(ctxt, \'select_destinations\', **msg_args)\n  File "/var/lib/openstack/local/lib/python2.7/site-packages/oslo_messaging/rpc/client.py", line 179, in call\n    retry=self.retry)\n  File "/var/lib/openstack/local/lib/python2.7/site-packages/oslo_messaging/transport.py", line 133, in _send\n    retry=retry)\n  File "/var/lib/openstack/local/lib/python2.7/site-packages/oslo_messaging/_drivers/amqpdriver.py", line 584, in send\n    call_monitor_timeout, retry=retry)\n  File "/var/lib/openstack/local/lib/python2.7/site-packages/oslo_messaging/_drivers/amqpdriver.py", line 573, in _send\n    call_monitor_timeout)\n  File "/var/lib/openstack/local/lib/python2.7/site-packages/oslo_messaging/_drivers/amqpdriver.py", line 459, in wait\n    message = self.waiters.get(msg_id, timeout=timeout)\n  File "/var/lib/openstack/local/lib/python2.7/site-packages/oslo_messaging/_drivers/amqpdriver.py", line 336, in get\n    \'to message ID %s\' % msg_id)\n', u'created': u'2019-10-10T07:15:01Z
```

Sometimes, a massive amount of pods restarting themselves because liveness probe continue failing

```console
root@master1:~# kubectl get pods -n openstack -owide | awk '{if ($4 > 0) print $0}'
NAME                                             READY   STATUS      RESTARTS   AGE     IP               NODE     NOMINATED NODE   READINESS GATES
neutron-dhcp-agent-default-fss74                 0/1     Running     3          7h29m   172.30.0.14      slave6   <none>           <none>
neutron-dhcp-agent-default-ks82l                 0/1     Running     3          7h31m   172.30.0.13      slave5   <none>           <none>
neutron-l3-agent-dvr-default-qb7cc               1/1     Running     27         7h31m   172.30.0.4       slave7   <none>           <none>
neutron-l3-agent-snat-default-4vzwl              0/1     Running     3          7h29m   172.30.0.14      slave6   <none>           <none>
neutron-metadata-agent-default-grzxz             0/1     Running     4          7h31m   172.30.0.14      slave6   <none>           <none>
neutron-metadata-agent-default-ndtxp             0/1     Running     4          7h30m   172.30.0.12      slave4   <none>           <none>
neutron-metadata-agent-default-zzxs4             0/1     Running     4          7h29m   172.30.0.13      slave5   <none>           <none>
nova-compute-default-kk4tv                       1/1     Running     27         30h     172.30.0.4       slave7   <none>           <none>
nova-consoleauth-787f56d969-69tqw                0/1     Running     4          30h     10.151.174.247   slave5   <none>           <none>
nova-consoleauth-787f56d969-r6d47                0/1     Running     4          30h     10.151.190.162   slave6   <none>           <none>
nova-scheduler-778dd5cfb9-4tnqh                  0/1     Running     4          110m    10.151.190.188   slave6   <none>           <none>
nova-scheduler-778dd5cfb9-lz4mq                  0/1     Running     4          111m    10.151.174.235   slave5   <none>           <none>
nova-scheduler-778dd5cfb9-rp9jt                  1/1     Running     1          110m    10.151.26.46     slave4   <none>           <none>
```

I also try to write some simple scripts myself, but it could handle messages correctly. Since rabbitmq status is health reported from `rabbitmqctl cluster_status`, right now my hypothesis is that there might be some problems inside **oslo.messaging**.

In this document, I will try to record and analyze the situation and hopefully find out a way to monitor the cluster.

### Relate Connection, Channel and Consumer

One of the difficulty is to relate connection, channel and consumers together, although it does not appear to be obvious, actually there is a way find out some useful information

```bash
# first list connections and find out targets
# pid: erlang pid of a connection object
# peer_host: client's host ip address
# peer_port: client's host port
rabbitmqctl list_connections pid peer_host peer_port | grep <host> | grep <port>

# pid: erlang pid of channel object
# connection: connection's pid
# name: channel name
# vhost: vhost name
rabbitmqctl list_channels pid connection name vhost | grep <connection pid>

# consumers are namespaced to a specific vhost
rabbitmqctl list_consumers -p <vhost> | grep <channel pid>
# queue_name	channel_pid	consumer_tag	ack_required	prefetch_count	arguments
```

> In openstack, **queue name** is the same as **binding name** and got fancy name **topic**

### Steps to Reproduce Issue

Right now it seems like there is a way to reproduce the issue, but of course further investigation is needed to confirm.

* First create demo rpc server, and try
* Make sure connection & queue created on different node
* delete rabbitmq server where queue is running on

## REFs

* [bug 1822778](https://bugs.launchpad.net/oslo.messaging/+bug/1822778)
* [pull #1913 waill wait joined node for syncing vhosts](https://github.com/rabbitmq/rabbitmq-server/pull/1913)