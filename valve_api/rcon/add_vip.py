import os
import valve.rcon
from valve_api.rcon.info_user import info_user
from ssh.groups_vip import groups_vip


def add_vip_rcon(number, group_number, time_vip):
    """
    Function to add VIP to player using steamid or name
    :return: response from server
    """
    rcon_password = os.getenv('RCON_PASSWORD')
    server_address = (os.getenv('SERVER_IP'), int(os.getenv('SERVER_PORT')))

    file_groups = groups_vip()

    curr_user = info_user(number)
    userid, slot, name, uniqueid, connected, ping, loss, state, rate, adr = curr_user
    name = name.replace("\"", "") if name else None
    user = f'#{userid}' if userid else f'#{name}' if name else f'#{uniqueid}'

    try:
        with valve.rcon.RCON(server_address, rcon_password) as rcon:
            response = rcon.execute(f'sm_addvip {user} {file_groups[int(group_number) - 1]} {time_vip}')
            result = response.body.decode('utf-8')
            return result
    except ConnectionRefusedError:
        return 'Не удается отправить команду'