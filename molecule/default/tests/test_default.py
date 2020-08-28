"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_user_exists(host):
    """Verify that the joiner user exists."""
    assert host.user("joiner").name == "joiner"


def test_ssh_config_exists(host):
    """Verify that the joiner sudo config file exists."""
    f = host.file("/etc/sudoers.d/joiner")
    assert f.exists
    assert f.is_file


def test_sudo_config(host):
    """Verify that the joiner user is only allowed to run a single command via sudo."""
    with host.sudo("joiner"):
        # This command should fail, since
        # 1. joiner is not allowed to run this command via sudo.
        # 2. Therefore sudo will ask for a password, and there is no
        # askpass helper installed.
        #
        # On all distributions, "askpass" is mentioned in the failure
        # message.
        bad_cmd = host.run("sudo ls")
        assert "askpass" in bad_cmd.stderr
        assert bad_cmd.failed

        # This command will also fail, since the FreeIPA variables
        # file that is created via cloud-init is not yet present.
        # Sudo will allow joiner to try to run it, though, and we will
        # get the failure message from the script itself.
        good_cmd = host.run("sudo /usr/local/sbin/setup_freeipa.sh")
        assert (
            good_cmd.stdout.rstrip()
            == """FreeIPA variables file does not exist: /var/lib/cloud/instance/freeipa-vars.sh
It should have been created by cloud-init at boot."""
        )
        assert good_cmd.failed
