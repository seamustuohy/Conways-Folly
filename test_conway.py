import unittest
import conways_game


class check_players(unittest.TestCase):
    def test_player_shuffle(self):
        players = ["bob", "frank", "other", "again", "really?"]
        test = ["bob", "frank", "other", "again", "really?"]
        players_rand = conways_game.shuffle_players(players)
        self.assertNotEqual(players, test)

class board_testing(unittest.TestCase):
    def test_board_create(self):
        """compare board creation to static creation"""
        board = conways_game.game_size(20)
        test_board = []
        for x in range(20):
            test_board.append([" "] * 20)
        self.assertEqual(test_board, board)

    def test_tile_set(self):
        """compare modified board with original to ensure change """
        test_board = conways_game.game_size(30)
        test_board_two = conways_game.game_size(30)
        test_board_two[0][0] = "x"
        self.assertNotEqual(test_board, test_board_two)


        
if __name__ == "__main__":
    unittest.main()

        
