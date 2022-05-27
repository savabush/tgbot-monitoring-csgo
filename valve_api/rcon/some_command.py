import os
import valve.rcon


def post_rcon(func):
    """
    Function to post command through RCON
    :return: response from server
    """
    rcon_password = os.getenv('RCON_PASSWORD')
    server_address = (os.getenv('SERVER_IP'), int(os.getenv('SERVER_PORT')))
    try:
        with valve.rcon.RCON(server_address, rcon_password) as rcon:
            response = rcon.execute(func)
            result = response.body.decode('utf-8')
            return result
    except ConnectionRefusedError:
        return 'Не удается отправить команду'