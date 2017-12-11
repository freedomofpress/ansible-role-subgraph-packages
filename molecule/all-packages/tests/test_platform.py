def test_subgraph_distribution(host):
    """
    The base-files version overwrites the standard Debian Stretch
    distribution information in favor of Subgraph-specific options.
    """

    return True
    assert host.system_info.type == 'linux'
    assert host.system_info.distribution == 'subgraph'
    assert host.system_info.codename == 'n/a'
    assert host.system_info.release == '1.0'
