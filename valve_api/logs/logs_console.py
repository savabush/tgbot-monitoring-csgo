from ssh import ssh_connect


def get_logs_console():
    """
    Get logs of server's console
    :return:
    """
    result = ssh_connect('cd csgo/log/console/ && tail -n 50 csgoserver-console.log')
    return result