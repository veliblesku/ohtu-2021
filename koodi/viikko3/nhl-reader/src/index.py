import requests
#from player import Player
from datetime import datetime
from playerreader import PlayerReader
from playerstats import PlayerStats

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    #response = requests.get(url).json()
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    ##print(reader)

    players = stats.top_scorers_by_nationality("FIN")

    # print("JSON-muotoinen vastaus:")
    # print(response)

    # players = []
    # for player_dict in response:
    #     player = Player(
    #         player_dict['name'],
    #         player_dict['nationality'],
    #         player_dict['assists'],
    #         player_dict['goals'],
    #         player_dict['penalties'],
    #         player_dict['team'],
    #         player_dict['games']
    #     )

    #     players.append(player)

    # print("Players from FIN " + str(dateTimeObj))
    
    # finns = list(filter(lambda player: player.nationality == 'FIN', players))
    # finns.sort(reverse=True, key=sorter_by_goals)
    ##sorted_finns = finns.sort(key=sorter)
    for player in players:
        #print("moro")
        ##print(sorter(player))
        print(player)

if __name__ == "__main__":
    main()