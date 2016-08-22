import pytest
import testinfra
import os

SSH_CONFIG = '.ssh-config'

@pytest.fixture
def TestinfraBackend(request, tmpdir):
    # Override the TestinfraBackend fixture,
    # all testinfra fixtures (i.e. modules) depend on it.
    ssh_config_file = tmpdir.join(SSH_CONFIG)
    ssh_config_file.write('Host {0}\nUser {1}\nPort {2}\nIdentityFile {3}\n'.format(
            os.environ['KITCHEN_HOSTNAME'],
            os.environ['KITCHEN_USERNAME'],
            os.environ['KITCHEN_PORT'],
            os.environ['KITCHEN_SSH_KEY'],
        ))


    # Return a dynamic created backend
    return testinfra.backend.paramiko.ParamikoBackend(os.environ['KITCHEN_HOSTNAME'], str(ssh_config_file), sudo=True)
