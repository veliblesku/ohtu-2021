from playerreader import PlayerReader


def sorter_by_goals(player):
    return player.goals + player.assists

class PlayerStats:
    def __init__(self, reader):
        self.filtered_players = []
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        #print("Players from xx" + str(dateTimeObj))
        #self.filtered_players = self.reader.players
        self.filtered_players  = list(filter(lambda player: player.nationality == nationality, self.reader.players))
        self.filtered_players.sort(reverse=True, key=sorter_by_goals)

        return self.filtered_players