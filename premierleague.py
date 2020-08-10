import json

with open("lineups.json") as lineups_json:
    lineups = json.load(lineups_json)

print(lineups)
