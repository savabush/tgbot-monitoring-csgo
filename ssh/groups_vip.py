from ssh.ssh import ssh_connect
from re import split


def groups_vip():
    result = ssh_connect('cd csgo/serverfiles/csgo/addons/sourcemod/data/vip/cfg && cat groups.ini')[14:]
    groups = split(r"{[\w\s\"\/\.\(\)\-\,\[\]]+}", result)
    return [group.strip().strip('\"') for group in groups[:-1]]
