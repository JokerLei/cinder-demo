import requests
from requests.auth import HTTPBasicAuth
import argparse


class RabbitManagementAPI(object):

    def __init__(self, args):
        self.auth = HTTPBasicAuth(args.user, args.password)
        self.url = "%s://%s:%s" % (args.protocol, args.host, args.port)

    def list_vhosts(self):
        url = "%s%s" % (self.url, '/api/vhosts')
        return requests.get(url, auth=self.auth).json()

    def list_exchanges(self, vhost=None):
        url = "%s%s" % (self.url, '/api/exchanges')
        if vhost:
            url = "%s/%s" % (url, vhost)
        return requests.get(url, auth=self.auth).json()

    def list_bindings(self, vhost=None, exchange=None):
        url = "%s%s" % (self.url, '/api/bindings')

        if vhost:
            url = "%s/%s" % (url, vhost)
        if vhost and exchange:
            url = "%s/%s" % (url, exchange)

        return requests.get(url, auth=self.auth).json()

    def list_queues(self, vhost=None):
        url = "%s%s" % (self.url, '/api/queues')
        if vhost:
            url = "%s/%s" % (url, vhost)
        return requests.get(url, auth=self.auth).json()

    def get_queue(self, vhost, name):
        url = "%s%s/%s/%s" % (self.url, '/api/queues', vhost, name)
        return requests.get(url, auth=self.auth).json()

    def publish(self, vhost, exchange, routing_key=None, payload=None):
        url = '%s%s/%s/%s/publish' % (self.url, '/api/exchanges', vhost, exchange)  # noqa
        body = {
            "routing_key": routing_key,
            "payload": payload,
            "properties": {},
            "payload_encoding": "string"
        }
        resp = requests.post(url, json=body, auth=self.auth)
        return resp.status_code, resp.json()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--user', dest='user')
    parser.add_argument('--password', dest='password')
    parser.add_argument('--host', dest='host')
    parser.add_argument('--port', dest='port', default=15672)
    parser.add_argument('--protocol', dest='protocol', default='http')

    return parser.parse_args()


if __name__ == '__main__':

    mgmt_api = RabbitManagementAPI(parse_args())

    for _vhost in mgmt_api.list_vhosts():
        vhost = _vhost.get('name', None)
        if not vhost:
            continue
        exchanges = {obj['name']: obj for obj in mgmt_api.list_exchanges(vhost=vhost)}  # noqa
        bindings = mgmt_api.list_bindings(vhost=vhost)

        for binding in bindings:
            exchange = exchanges.get(binding.get('source', None), None)

            # default direct exchange is ignored because reply_* message
            # is not worth restored
            if not exchange or not exchange.get('name', None):
                continue
            elif exchange.get('name').startswith('reply_'):
                continue

            # openstack will bind one queue for each routing key
            _queue = binding.get('destination', None)
            queue = mgmt_api.get_queue(vhost, _queue)
            queue_name = queue.get('name', None)
            status, body = mgmt_api.publish(
                vhost,
                exchange.get('name', None),
                routing_key=queue_name,
                payload='{"test": "test"}')

            if 200 <= status < 400:
                if not body['routed']:
                    print queue
