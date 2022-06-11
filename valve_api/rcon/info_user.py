from valve_api.rcon.users_rcon import get_users_rcon


def info_user(number):
    users_string = get_users_rcon()
    users = users_string.split('\n')[11:-3]
    curr_user = None
    for user in users:
        if user.split()[1:][1] == number:
            curr_user = user.split()[1:]
    return curr_user
