import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_works_with_valid_name(self):
        playerName = "Kurri"
        self.assertAlmostEqual(str(self.statistics.search(playerName)), "Kurri EDM 37 + 53 = 90")

    
    def test_search_with_invalid_name(self):
        self.assertIsNone(self.statistics.search("ssd"))

    def test_team_works_correctly(self):
        team = self.statistics.team("EDM")
        self.assertAlmostEqual(team[0].name, "Semenko")
        self.assertAlmostEqual(team[1].name, "Kurri")
        self.assertAlmostEqual(team[2].name, "Gretzky")

    def test_top_scorer_works(self):
        sortedPlayers = self.statistics.top_scorers(2)
        self.assertAlmostEqual(str(sortedPlayers[0]), "Gretzky EDM 35 + 89 = 124")
        self.assertAlmostEqual(str(sortedPlayers[1]), "Lemieux PIT 45 + 54 = 99")
        self.assertAlmostEqual(str(sortedPlayers[2]), "Yzerman DET 42 + 56 = 98")

