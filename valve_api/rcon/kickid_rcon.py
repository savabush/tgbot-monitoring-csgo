import os
import valve.rcon
from valve_api.rcon.info_user import info_user


def kick_id(number, msg):
    """
    Function to kick player using steamid, id or name
    :return: response from server
    """
    rcon_password = os.getenv('RCON_PASSWORD')
    server_address = (os.getenv('SERVER_IP'), int(os.getenv('SERVER_PORT')))

    curr_user = info_user(number)
    userid, slot, name, uniqueid, connected, ping, loss, state, rate, adr = curr_user

    try:
        pass
        with valve.rcon.RCON(server_address, rcon_password) as rcon:
            response = rcon.execute(f'kickid {userid if userid else uniqueid} {msg if msg else "Deserved"}')
            result = response.body.decode('utf-8')
            return result
    except ConnectionRefusedError:
        return 'Не удается отправить команду'