from ssh.ssh import ssh_connect
from re import sub
import os


def turn_on_server_ssh():
    """
    Turning ON server csgo
    :return:
    """
    result = ssh_connect(f'{os.getenv("PATH_TO_LGSM")}/csgoserver start')
    result_re = sub(r'\[94m|\[93m|\[92m|\[0m|\[32m|\[31m', '', result)
    return result_re
