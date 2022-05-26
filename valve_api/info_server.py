import valve.source
import valve.source.a2s
import valve.source.master_server


def get_info_server_csgo(server_address):
    """
    Return string info about server with players/maxplayers and score
    :param server_address:
    :return:
    """
    with valve.source.a2s.ServerQuerier(server_address) as server:
        try:
            info = server.info()
            info_repr = '{player_count}/{max_players} {server_name}'.format(**info)
            players = server.players()
            if players['player_count'] > 0:
                sort_players = sorted(players['players'], key=lambda p: p['score'], reverse=True)
                players_repr = '\n'.join('{score} {name}'.format(**player) for player in sort_players)
            else:
                players_repr = 'На сервере пока пусто'
            return info_repr + '\n\n\n' + players_repr
        except valve.source.NoResponseError:
            return 'Технические неполадки'
