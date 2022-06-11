import os
import valve.rcon
from valve_api.rcon.info_user import info_user


def ban_id(number, time_ban, msg):
    """
    Function to ban player using steamid, id or ip
    :return: response from server
    """
    rcon_password = os.getenv('RCON_PASSWORD')
    server_address = (os.getenv('SERVER_IP'), int(os.getenv('SERVER_PORT')))

    curr_user = info_user(number)
    userid, slot, name, uniqueid, connected, ping, loss, state, rate, adr = curr_user
    name = name.replace("\"", '')

    try:
        with valve.rcon.RCON(server_address, rcon_password) as rcon:
            response = rcon.execute(f'sm_ban {"#" + userid if userid else name}'
                                    f' {time_ban if time_ban else "0"} {msg if msg else "Deserved"}')
            result = response.body.decode('utf-8')
            return result
    except ConnectionRefusedError:
        return 'Не удается отправить команду'