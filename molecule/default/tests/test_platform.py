def test_debian_distribution(host):
    """
    Apt pinning should prevent upgrade of base-files to Subgraph's
    version, and stick with the default Debian info.
    """

    assert host.system_info.type == 'linux'
    assert host.system_info.distribution == 'debian'
    assert host.system_info.codename == 'stretch'
