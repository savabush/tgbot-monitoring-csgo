import os
import valve.rcon
from valve_api.rcon.info_user import info_user


def del_vip_rcon(number):
    """
    Function to delete VIP to player using steamid
    :return: response from server
    """
    rcon_password = os.getenv('RCON_PASSWORD')
    server_address = (os.getenv('SERVER_IP'), int(os.getenv('SERVER_PORT')))

    curr_user = info_user(number)
    userid, slot, name, uniqueid, connected, ping, loss, state, rate, adr = curr_user

    try:
        with valve.rcon.RCON(server_address, rcon_password) as rcon:
            response = rcon.execute(f'sm_delvip {uniqueid}')
            result = response.body.decode('utf-8')
            return result
    except ConnectionRefusedError:
        return 'Не удается отправить команду'