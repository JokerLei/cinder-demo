#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from tempest.lib import decorators
from tempest.api.compute import base

from dev_demo.openstack.tempest.inspur.tests.functional import functional_base


class LocalResizeTest(
    functional_base.FunctionalTestBase,
    base.BaseV2ComputeAdminTest
):

    def create_flavor_and_set_extra_specs(self, ram, vcpus, disk, name=None,
                                          is_public='True', specs=None,
                                          **kwargs):
        flavor = self.create_flavor(ram, vcpus, disk, name=name,
                                    is_public=is_public, **kwargs)

        if specs:
            client = self.admin_flavors_client
            client.set_flavor_extra_spec(
                flavor['id'],
                **specs
            )

        return flavor

    def _get_server_host(self, server_id):
        client = self.admin_servers_client
        return client.show_server(server_id)['server']['OS-EXT-SRV-ATTR:host']

    @decorators.idempotent_id('121eb93d-1c5a-4518-8a49-e2d2b8b1ea5f')
    def test_local_resize(self):
        origin_flavor = self.create_flavor(
            2048, 1, 40)
        dest_flavor = self.create_flavor_and_set_extra_specs(
            4096, 4, 80, specs={"inspur:dest": "only_local"})
        server = self.create_test_server(
            False,
            flavor=origin_flavor['id'],
            wait_until='ACTIVE')
        host_pre_resize = self._get_server_host(server['id'])
        self.resize_server(
            server['id'],
            dest_flavor['id'])
        host_post_resize = self._get_server_host(server['id'])

        self.assertEqual(host_pre_resize, host_post_resize)
