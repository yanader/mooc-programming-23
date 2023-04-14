import json

def file_reader(file_name:str):
    #read the given file and return a list from the file
    with open(file_name) as my_file:
        data = my_file.read()
    players_list = json.loads(data)
    my_file.close()
    return players_list

def display_command_details():
    # display command options to the user
    print('commands:')
    print('0 quit')
    print('1 search for player')
    print('2 teams')
    print('3 countries')
    print('4 players in team')
    print('5 players from country')
    print('6 most points')
    print('7 most goals')


def player_search(player_list:list):
    player_dictionary = {}
    search_player = input('name: ')
    for player in player_list:
        if player["name"] == search_player:
            player_dictionary = player
    print_player(player_dictionary)


def print_player(player:dict):
    print(f'{player["name"]:20} {player["team"]:5}{player["goals"]:>2} + {player["assists"]:>2} = {player["goals"] + player["assists"]:>3}')


def teams(player_list:list):
    teams = []
    for player in player_list:
        if not player["team"] in teams:
            teams.append(player["team"])
    for team in sorted(teams):
        print(team)


def countries(player_list:list):
    countries = []
    for player in player_list:
        if not player["nationality"] in countries:
            countries.append(player["nationality"])
    for country in sorted(countries):
        print(country)


def players_in_team(player_list:list):
    team_list = []
    team = input('team: ')
    for player in player_list:
        if player["team"] == team:
            team_list.append(player)
    team_list = order_by_total_points(team_list)
    for player in team_list:
        print_player(player)


def players_from_country(player_list:list):
    country_list = []
    country = input('country: ')
    for player in player_list:
        if player['nationality'] == country:
            country_list.append(player)
    country_list = order_by_total_points(country_list)
    
    for player in country_list:
        print_player(player)

def highest_total_points(player_list:list):
    success_list = order_by_total_points(player_list)
    qty = int(input('how many: '))
    for i in range(qty):
        print_player(success_list[i])

def highest_goals(player_list:list):
    success_list = order_by_total_goals(player_list)
    qty = int(input('how many: '))
    for i in range(qty):
        print_player(success_list[i])

def order_by_total_goals(team_list:list):
    def by_goals(player):
        return player['goals'], -1 * player['games']
    
    in_goals_order= sorted(team_list, key=by_goals,reverse=True)
    return in_goals_order

def order_by_total_points(team_list:list):
    def by_points(player):
        return player['goals'] + player['assists'], player['goals']
    
    in_points_order = sorted(team_list, key=by_points,reverse=True)
    return in_points_order


def interface():
    # interact with the user
    file_name = input("file name: ")
    player_list = file_reader(file_name)
    print(f'read the data of {len(player_list)} players')
    print()
    display_command_details()

    while True:
        print()
        command = int(input('command: '))

        if command == 0:
            break   
        elif command == 1:
            player_search(player_list)
        elif command == 2:
            teams(player_list)
        elif command == 3:
            countries(player_list)
        elif command == 4:
            players_in_team(player_list)
        elif command == 5:
            players_from_country(player_list)
        elif command == 6:
            highest_total_points(player_list)
        elif command == 7:
            highest_goals(player_list)


interface()


