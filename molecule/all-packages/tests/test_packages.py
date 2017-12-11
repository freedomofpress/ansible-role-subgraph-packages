import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('pkg', [
    'paxrat',
    'macouflage'
])
def test_subgraph_packages(host, pkg):

    p = host.package(pkg)
    assert p.is_installed
