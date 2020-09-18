import requests
import bs4


class NotSinglePlayerFoundException(Exception):
    def __init__(self, players_found):
        self.players_found = players_found
        if players_found == 0:
            self.message = "Players not found"
        else:
            self.message = "Multiple players found: " + str(players_found)
        super().__init__(self.message)


def scrap_player_overall(player_name, league_id):
    url = "https://www.fifaindex.com/players/?name={}&league={}&order=desc".format(player_name.replace(" ", "+"), league_id)
    request_page = requests.get(url)
    soup = bs4.BeautifulSoup(request_page.content, "html.parser")
    players_soup_list = soup.findAll("tr", attrs={"data-playerid": True})
    if len(players_soup_list) != 1:
        raise NotSinglePlayerFoundException(len(players_soup_list))
    player_soup = players_soup_list[0]
    player_fields_soup = player_soup.findAll("td", attrs={"data-title": True})
    return int(player_fields_soup[1].findAll("span")[0].get_text())
