import premierleague
import fifaoverallscraper


def replace_names_to_overalls(team_vector):
    for i in range(len(team_vector)):
        if team_vector[i] != "0":
            try:
                team_vector[i] = fifaoverallscraper.scrap_player_overall(team_vector[i], 13)
            except fifaoverallscraper.NotSinglePlayerFoundException as err:
                print(err.message)
        else:
            team_vector[i] = 0


def scrap_game_vector(game_url):
    premierleague.start()
    game = premierleague.scrap_match_page(game_url)
    replace_names_to_overalls(game["Home Vector"])
    replace_names_to_overalls(game["Away Vector"])
    return game["Home Vector"] + game["Away Vector"]


print(scrap_game_vector("https://www.premierleague.com/match/58903"))
