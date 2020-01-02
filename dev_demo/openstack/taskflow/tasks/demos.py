from uuid import uuid4
from taskflow.task import Task


class SimplePrintTask(Task):
    def __init__(self, banner):
        super(SimplePrintTask, self).__init__()
        self.banner = banner
        self.name = "task-%s" % self.banner

    def execute(self, *args, **kwargs):
        print(self.banner)


class SimpleRevertablePrintTask(Task):
    def __init__(self, banner):
        super(SimpleRevertablePrintTask, self).__init__()
        self.name = str(uuid4())
        self.banner = banner

    def execute(self, *args, **kwargs):
        print(self.banner)

    def revert(self, *args, **kwargs):
        print("reverting job")


class SimpleFailedTask(Task):
    def __init__(self, *args):
        super(SimpleFailedTask, self).__init__()
        self.name = str(uuid4())

    def execute(self, *args, **kwargs):
        raise Exception("Task failed")
