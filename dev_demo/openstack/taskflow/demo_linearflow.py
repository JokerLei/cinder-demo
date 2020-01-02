from oslo_log import log
import taskflow.engines
from taskflow.patterns import linear_flow

from dev_demo.openstack.taskflow.tasks.demos \
    import SimplePrintTask

LOG = log.getLogger(__name__)
flow_name = "test"

if __name__ == "__main__":

    test_flow = linear_flow.Flow(flow_name)
    test_flow.add(SimplePrintTask("The First Task"))
    test_flow.add(SimplePrintTask("The Second Task"))
    taskflow.engines.load(test_flow).run()
