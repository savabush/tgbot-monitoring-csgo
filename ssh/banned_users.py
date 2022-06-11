from ssh.ssh import ssh_connect
import os


def banned_users():
    result = ssh_connect(
        f'cd {os.getenv("PATH_TO_LGSM")}/serverfiles/csgo/cfg && cat banned_user.cfg'
    )
    result = [f'{i} - {banned_user.split()[2]}' for i, banned_user in enumerate(result.split('\r\n')[:-1], 1)]
    return result
