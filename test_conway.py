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
        board = conways_game.build_board_matrix(20)
        test_board = []
        for x in range(20):
            test_board.append([" "] * 20)
        self.assertEqual(test_board, board)
        
    def test_tile_set(self):
        """compare modified board with original to ensure change """
        test_board = conways_game.build_board_matrix(30)
        test_board_two = conways_game.build_board_matrix(30)
        test_board_two[1][1] = "x"
        self.assertNotEqual(test_board, test_board_two)

class phase_testing(unittest.TestCase):
    """tests that phases correctly exicute and iterate """
#    def test_player_iterate(self):
#        players = ["bob", "frank", "other", "again", "really?"]
#        finished_players = conways_game.play_phase(players)
#        self.assertEqual(players, finished_players)

class evolution_testing(unittest.TestCase):
    """ checks evolution"""
    def test_evolve(self):
        a = "a"
        b = "b"
        board = [[" ", " ", " ", " ", " "],[" ", " ", a, a, " "],[" ", a, a, a, " "],[" ", a, " ", " ", " "],[" ", " ", " ", " ", " "]]
        test_board = [[" ", " ", " ", " ", " "],[" ", a, " ", a, " "],[" ", a, " ", a, " "],[" ", a, " ", " ", " "],[" ", " ", " ", " ", " "]]
        conways_game.print_board(board)
        board = conways_game.evolve(board, 1)
        self.assertEqual(board, test_board)

        



        
if __name__ == "__main__":
    unittest.main()

        
