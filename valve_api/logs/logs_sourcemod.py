from ssh import ssh_connect


def get_logs_sourcemod():
    """
    Get logs of SourceMod
    :return:
    """
    result = ssh_connect('cd csgo/serverfiles/csgo/addons/sourcemod/logs && tail -n 40 "$(ls -1rt err* | tail -1)"')
    return result
