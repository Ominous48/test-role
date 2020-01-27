import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('pkg', [
  'chrony'
])

def test_chrony_installed(host, pkg):
    package = host.package(pkg)
    assert package.is_installed

def test_chrony_service_started_enabled(host):
    chrony_service_name = _get_chrony_package_name(host.system_info.distribution)
    chrony_service = host.service(chrony_service_name)
    assert chrony_service.is_running
    assert chrony_service.is_enabled

def _get_chrony_package_name(host_distro):
    return {
        "debian": "chrony",
        "centos": "chronyd"
    }.get(host_distro, "chrony")
