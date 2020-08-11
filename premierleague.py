import json
import bs4
import requests

with open("lineups.json") as lineups_json:
    lineups = json.load(lineups_json)


def scrap_match_page(url):
    match_data = {}
    request_page = requests.get(url)
    soup = bs4.BeautifulSoup(request_page.content, "html.parser")

    match_data["Home Team"] = soup.find("div", class_="team home").find("span", class_="long").get_text()
    match_data["Away Team"] = soup.find("div", class_="team away").find("span", class_="long").get_text()
    teams_formation_soup_list = soup.find_all("strong", class_="matchTeamFormation")
    home_team_formation = teams_formation_soup_list[0].get_text()
    away_team_formation = teams_formation_soup_list[1].get_text()

    # players = {}
    home_players_soup_list = soup.find("div", class_="col-4-m").find_all("li", class_="player")
    away_players_soup_list = soup.find("div", class_="col-4-m right").find_all("li", class_="player")
    home_players = {player.find("div", class_="number").get_text(): player.find("span", class_="name").get_text().strip() for player in home_players_soup_list}
    away_players = {player.find("div", class_="number").get_text(): player.find("span", class_="name").get_text().strip() for player in away_players_soup_list}

    # print(match_data["Home Team"])
    # print(home_team_formation)
    # print(match_data["Away Team"])
    # print(away_team_formation)
    # print(players_soup_list)
    print(home_players)
    print(away_players)


scrap_match_page("https://www.premierleague.com/match/46975")
