import os
import valve.rcon
from valve_api.rcon.users_rcon import get_users_rcon


def kick_id(number, msg):
    """
    Function to kick player using steamid, id or name
    :return: response from server
    """
    rcon_password = os.getenv('RCON_PASSWORD')
    server_address = (os.getenv('SERVER_IP'), int(os.getenv('SERVER_PORT')))

    users_string = get_users_rcon()
    users = users_string.split('\n')[9:-3]
    curr_user = None
    for user in users:
        if user.split()[1:][1] == number:
            curr_user = user.split()[1:]
    userid, slot, name, uniqueid, connected, ping, loss, state, rate, adr = curr_user

    try:
        pass
        with valve.rcon.RCON(server_address, rcon_password) as rcon:
            response = rcon.execute(f'kickid {userid if userid else uniqueid} {msg if msg else "Deserved"}')
            result = response.body.decode('utf-8')
            return result
    except ConnectionRefusedError:
        return 'Не удается отправить команду'