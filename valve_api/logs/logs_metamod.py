from ssh.ssh import ssh_connect
import os


def get_logs_metamod():
    """
    Get logs of MetaMod
    :return:
    """
    result = ssh_connect(f'cd {os.getenv("PATH_TO_LGSM")}/serverfiles/csgo/addons/metamod/bin/ && tail -n 40 metamod-fatal.log')
    return result
