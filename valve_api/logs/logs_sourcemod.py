from ssh.ssh import ssh_connect
import os


def get_logs_sourcemod():
    """
    Get logs of SourceMod
    :return:
    """
    result = ssh_connect(f'cd {os.getenv("PATH_TO_LGSM")}/serverfiles/csgo/addons/sourcemod/logs &&'
                         f' tail -n 40 "$(ls -1rt err* | tail -1)"')
    return result
