from ssh import ssh_connect


def get_logs_script():
    """
    Get logs of server's script LGSM
    :return:
    """
    result = ssh_connect('cd csgo/log/script/ && tail -n 40 csgoserver-script.log')
    return result
