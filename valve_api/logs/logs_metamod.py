from ssh.ssh import ssh_connect


def get_logs_metamod():
    """
    Get logs of MetaMod
    :return:
    """
    result = ssh_connect('cd csgo/serverfiles/csgo/addons/metamod/bin/ && tail -n 40 metamod-fatal.log')
    return result
