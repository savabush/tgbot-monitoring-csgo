from ssh.ssh import ssh_connect
import os


def get_logs_script():
    """
    Get logs of server's script LGSM
    :return:
    """
    result = ssh_connect(f'cd {os.getenv("PATH_TO_LGSM")}/log/script/ && tail -n 40 csgoserver-script.log')
    return result
