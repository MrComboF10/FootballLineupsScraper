import premierleague

premierleague.start()
seasons = premierleague.scrap_premier_league(["2020_2021"], ["https://www.premierleague.com/results?co=1&se=363&cl=-1"])
premierleague.create_wb(seasons)
premierleague.write_taticas_rosques()
premierleague.write_jogos_quinados()
