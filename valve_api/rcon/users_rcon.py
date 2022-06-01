import os
import valve.rcon


def get_users_rcon():
    """
    Function to get users list from server CSGO
    :return: response from server
    """
    rcon_password = os.getenv('RCON_PASSWORD')
    server_address = (os.getenv('SERVER_IP'), int(os.getenv('SERVER_PORT')))
    try:
        with valve.rcon.RCON(server_address, rcon_password) as rcon:
            response = rcon.execute('status')
            result = response.body.decode('utf-8')
            return result
    except ConnectionRefusedError:
        return 'Не удается отправить команду'
