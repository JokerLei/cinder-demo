from masakari.engine.drivers.taskflow import base
from masakari import objects


class DemoTask(base.MasakariTask):

    def __init__(self, context, novaclient, **kwargs):
        kwargs['requires'] = ['host_name', 'notification_uuid']
        super(DemoTask, self).__init__(
            context, novaclient, **kwargs
        )

    def execute(self, host_name, notification_uuid, *args, **kwargs):
        with open('/tmp/masakari.test', 'w+') as f:
            f.writelines([str(objects.Notification.get_by_uuid(
                self.context, notification_uuid
            )), 'hello world'])
