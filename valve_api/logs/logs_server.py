from ssh.ssh import ssh_connect
import os


def get_logs_server():
    """
    Get logs of server CSGO
    :return:
    """
    result = ssh_connect(f'cd {os.getenv("PATH_TO_LGSM")}/log/server/ && tail -n 40 "$(ls -1rt | tail -1)"')
    return result
