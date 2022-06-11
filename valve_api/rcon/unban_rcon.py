import os
import valve.rcon
from ssh.banned_users import banned_users


def unban_rcon(number):
    """
    Function to unban player using steamid, id or ip
    :return: response from server
    """
    rcon_password = os.getenv('RCON_PASSWORD')
    server_address = (os.getenv('SERVER_IP'), int(os.getenv('SERVER_PORT')))

    steamid = banned_users()[int(number) - 1].split('-')[1]

    try:
        with valve.rcon.RCON(server_address, rcon_password) as rcon:
            response = rcon.execute(f'sm_unban {steamid}')
            result = response.body.decode('utf-8')
            return result
    except ConnectionRefusedError:
        return 'Не удается отправить команду'