import valve.rcon


def get_info_server_csgo(server_address, rcon_password):
    """
    Return string info about server with players/max_players and score
    :param server_address: IP addr
    :param rcon_password: RCON password
    :return:
    """
    try:
        with valve.rcon.RCON(server_address, rcon_password) as rcon_:
            response = rcon_.execute('users')
            return response.body.decode('utf-8')
    except ConnectionRefusedError:
        return 'Технические неполадки'
