Subgraph OS packages Ansible role
=================================

Configures apt repositories from the Subgraph OS project, for installing
apt packages maintained by the Subgraph team.

Requirements
------------

Assumes Debian Stretch. You'll likely have problems with any other base
distribution, although judicious use of apt preferences may help.

Role Variables
--------------

```yaml
# Base apt packages required to configure repos
subgraph_pre_packages:
  - apt-transport-https
  - gnupg2

# Distribution release in Subgraoh OS nomenclature; "aaron" = "alpha".
subgraph_release: aaron

# Apt repository sources to provide.
subgraph_channels:
  - main

# Base repository URL, will be used to generate default list of apt repositories.
# Override this var if you use a mirror.
subgraph_apt_repo_url: "https://devrepo.subgraph.com/subgraph"

# Apt repositories to configure.
subgraph_apt_repos:
  - "deb {{ subgraph_apt_repo_url }} {{ subgraph_release }} {{ subgraph_channels|join(' ') }}"
  - "deb-src {{ subgraph_apt_repo_url }} {{ subgraph_release }} {{ subgraph_channels|join(' ') }}"

# Packages to install after Subgraph OS repos are configured, e.g.
# macouflage, paxrat.
subgraph_packages: []

# Downgrade priority so that only explicitly requested packages will
# be installed, never upgrades of other packages standard in Debian.
# Override by creating a new flat file and setting the filepath here.
subgraph_apt_preferences_src_file: "{{ role_path+'/files/subgraph_apt_preferences' }}"
```

Example Playbook
----------------


```yaml
- name: Install SubgraphOS packages.
  hosts: workstations
  vars:
    subgraph_packages:
      - macouflage
      - paxrat
  roles:
    - role: freedomofpress.subgraph-packages
```

Running tests
-------------
The config tests use both Docker and libvirt-backed VMs to validate
host state. The container strategy tests only the apt repo functionality,
whereas the VM strategy installs a custom kernel and tests it.

```
make test
```

License
-------

MIT

Author Information
------------------

Freedom of the Press Foundation (@freedomofpress)
