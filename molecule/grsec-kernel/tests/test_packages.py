import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('pkg', [
    'linux-image-grsec-amd64-subgraph',
])
def test_subgraph_packages(host, pkg):

    p = host.package(pkg)
    assert p.is_installed


def test_subgraph_grsec_kernel(host):
    c = host.command('uname -r')
    assert c.stdout.startswith('4.9.')
    assert c.stdout.endswith('-subgraph')


def test_subgraph_paxtest_installed(host):
    p = host.package('paxtest')
    assert p.is_installed


PAXTEST_PASSING_RESULTS = """
Test results:
Executable anonymous mapping             : Killed
Executable bss                           : Killed
Executable data                          : Killed
Executable heap                          : Killed
Executable stack                         : Killed
Executable shared library bss            : Killed
Executable shared library data           : Killed
Executable anonymous mapping (mprotect)  : Killed
Executable bss (mprotect)                : Killed
Executable data (mprotect)               : Killed
Executable heap (mprotect)               : Killed
Executable stack (mprotect)              : Killed
Executable shared library bss (mprotect) : Killed
Executable shared library data (mprotect): Killed
Writable text segments                   : Killed
Anonymous mapping randomization test     : 28 quality bits (guessed)
Heap randomization test (ET_EXEC)        : 35 quality bits (guessed)
Heap randomization test (PIE)            : 35 quality bits (guessed)
Main executable randomization (ET_EXEC)  : 28 quality bits (guessed)
Main executable randomization (PIE)      : 28 quality bits (guessed)
Shared library randomization test        : 28 quality bits (guessed)
VDSO randomization test                  : 28 quality bits (guessed)
Stack randomization test (SEGMEXEC)      : 35 quality bits (guessed)
Stack randomization test (PAGEEXEC)      : 35 quality bits (guessed)
Arg/env randomization test (SEGMEXEC)    : 39 quality bits (guessed)
Arg/env randomization test (PAGEEXEC)    : 39 quality bits (guessed)
Randomization under memory exhaustion @~0: 28 bits (guessed)
Randomization under memory exhaustion @0 : 28 bits (guessed)
Return to function (strcpy)              : paxtest: return address contains a NULL byte.
Return to function (memcpy)              : Vulnerable
Return to function (strcpy, PIE)         : paxtest: return address contains a NULL byte.
Return to function (memcpy, PIE)         : Vulnerable
"""


def test_subgraph_paxtest(host):
    c = host.command('paxtest blackhat')
    assert c.rc == 0
    assert PAXTEST_PASSING_RESULTS.strip() in c.stdout
