from ssh.ssh import ssh_connect
from re import sub


def get_info_server_csgo():
    """
    Return info about server with MANY info about server
    :return:
    """
    result = ssh_connect('cd csgo/ && ./csgoserver dt')
    result_re = sub(r'\[94m|\[93m|\[92m|\[0m|\[32m|\[31m', '', result)
    return result_re[:-395]
