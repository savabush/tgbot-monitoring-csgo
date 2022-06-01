from ssh import ssh_connect


def get_logs_server():
    """
    Get logs of server CSGO
    :return:
    """
    result = ssh_connect('cd csgo/log/server/ && tail -n 40 "$(ls -1rt | tail -1)"')
    return result
