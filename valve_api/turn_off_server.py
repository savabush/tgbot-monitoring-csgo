from ssh import ssh_connect
from re import sub


def turn_off_server_ssh():
    """
    Turning OFF server csgo
    :return:
    """
    result = ssh_connect('cd csgo/ && ./csgoserver stop')
    result_re = sub(r'\[94m|\[93m|\[92m|\[0m|\[32m|\[31m', '', result)
    return result_re
