from ssh.ssh import ssh_connect
from re import sub
import os


def restart_server_ssh():
    """
    Make a restart your server with this func using SSH
    :return:
    """
    result = ssh_connect(f'{os.getenv("PATH_TO_LGSM")}/csgoserver restart')
    result_re = sub(r'\[94m|\[93m|\[92m|\[0m|\[32m|\[31m', '', result)
    return result_re
