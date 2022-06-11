from ssh.ssh import ssh_connect
import os


def get_logs_console():
    """
    Get logs of server's console
    :return:
    """
    result = ssh_connect(f'cd {os.getenv("PATH_TO_LGSM")}/log/console/ && tail -n 40 csgoserver-console.log')
    return result
