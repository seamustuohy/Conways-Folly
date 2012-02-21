
import unittest
import conway

class board_tests(unittest.TestCase):
    def test_init(self):
        """creates board instance from conway and tests __init__'s against static versions"""
        test_board = conway.board(5)
        static = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        self.assertEqual(static, test_board.aboard)
    
    def test_build(self):
        """tests if board instance "build" function clears existing board on call"""
        test001_board = conway.board(5)
        test001_board.aboard[1][2] = 5
        test001_board = conway.board(6)
        static = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        self.assertEqual(static, test001_board.aboard)

    def test_tile_change(self):
        """Tests that tile changer only allows legal replacements

        Two Conditions:
        If tile empty ([0] or [{A-Z}0]) allow add any tile({A-Z or " "}{1 or 0}).
        If tile has active cell({A-Z}1) only remove tile ([0] or [{A-Z}0]).
        """
        test002_board = conway.board(8)
        test_tile = test002_board.aboard[2][2]
        test002_board.change_tile("A1", (2,2))
        self.assertNotEqual(test_tile, test002_board.aboard[2][2]) 
        test002_board.change_tile("B1", (2,2))
        self.assertEqual("A1", test002_board.aboard[2][2])
        test002_board.change_tile("A0", (2,2))
        self.assertEqual("A0", test002_board.aboard[2][2])
        test002_board.change_tile("0", (2,2))
        self.assertEqual("0", test002_board.aboard[2][2])

    def test_evolve(self):
        """tests that evolver correctly works in different scenerio's

        Scenerio's
        Single cell = death as claimed squyare
        cell w/ 1 neighbor = die as claimed square
        Cell w/ 2 neighbors = die
        Cell w/ 3 friendly neighbors = live
        Cell w/ 4+ neighbors = die as claimed square
        Empty w/ 2 or 3 neighbors = live as most common neighbor

        original cell:
            generic == friendly cell
            player == player cell
            empty == emply cell claimed by either friendly or player
        neighbors:
            1N = one Neighbor
            1fN = one friendly neighbor
            1NA = One neighbor of player A
            1NB = " " " player B
        """
"""        blank_board = conway.board(10)
        # single cell
        single_generic = single_player = blank_board
        single_generic.aboard[5][5] = 1 # die
        single_player.aboard[5][5] = "A1" #die
        single_player.evolve
        single_generic.evolve
        self.assertEqual(single_generic.aboard[5][5], 0)
        self.assertEqual(single_player.aboard[5][5], "A0")        
        # cell with one neighbor
        generic_1N = player_1N = blank_board
        generic_1N.board[5][5] = generic_1N.board[5][6] = 1 # all die
        player_1N.board[5][5] = player_1N.board[5][6] = "A1" # all die
        generic_1N.evolve
        player_1N.evolve
        self.assertEqual(generic_1N.board[5][5], 0, generic_1N.board[5][6])
        self.assertEqual(player_1N.board[5][5], "A0", player_1N.board[5][6])
        # cell with 2 neighbors only one friendly
        generic_1fN_1other = player_1fN_1other = blank_board
        generic_1fN_1other[5][5] = 1
        generic_1fN_1other.board[5][4] = "B1" # all die
        player_1fN_1other[5][5] = "A1"
        player_1fN_1other.board[5][4] = "B1" # all die
        generic_1fN_1other.evolve
        player_1fN_1other.evolve
        self.assertEqual(generic_1fN_1other.board[5][5], 0, generic_1N.board[5][6])
        self.assertEqual(player_1fN_1other.board[5][5], "A0", player_1N.board[5][6])
        self.assertEqual(player_1fN_1other.baord[5][4], "B0")
        self.assertEqual(generic_1fN_1other.baord[5][4], "B0")        
        # cell with 2 neighbors
        generic_2fN = player_1fN_1o = player_2fN = blank_board
        generic_2fN[5][5] = generic_2fN[5][4] = generic_2fN[5][6] = 1 # all die
        player_2fN[5][4] = player_2fN[5][5] = player_2fN[5][6] = "A1" # all die
        player_1fN_1o[5][5] = player_2fN[5][4] = "A1"
        player_2fN[5][6] = "B1" # all die
        player_2fN.evolve
        player_1fN_1o.evolve
        generic_2fN.evolve
        self.assertEqual(generic_2fN, blank_board)
        self.assertEqual(player_2fN[5][4], player_2fN[5][5], player_2fN[5][6], "A0")
        self.assertEqual(player_1fN_1o[5][5],player_1fN_1o[5][4], "A0")
        self.assertEqual(player_1fN_1o[5][6], "B0")
        #cell with 3 neighbors (only 2 friendly)
        generic_2fN_1other = player_2fN_1other = blank_board
        generic_2fN_1other[5][5] = generic_2fN_1other[5][4] = generic_2fN_1other[5][6] = 1
        generic_2fN_1other[4][5] = "B1"
        player_2fN_1other[5][5] = player_2fN_1other[5][4] = player_2fN_1other[5][6] = "A1"
        player_2fN_1other[4][5] = "B1" 
        player_2fN_1other.evolve
        generic_2fN_1other.evolve
        self.assertEqual(player_2fN_1other[5][5], player_2fN_1other[5][4], player_2fN_1other[5][6], "A0")
        self.assertEqual(generic_2fN_1other[5][5], generic_2fN_1other[5][4], generic_2fN_1other[5][6], 0)
        self.assertEqual(player_2fN_1other[4][5], "B0", generic_2fn_1other[4][5])
        #cell with 3 freindly neighbors
        generic_3fN = player_3fN = player_2fn_1g = blank_board
        generic_3fN[5][5] = generic_3fN[5][6] = generic_3fN[4][5] = generic_3fN[5][4] = 1
        player_3fN[5][5] = player_3fN[5][6] = player_3fN[4][5] = player_3fN[5][4] = "A1"
        player_2fN_1g[5][5] = player_2fN_1g[5][6] = player_2fN_1g[5][4] = "A1"
        player_2fN_1g[4][5] = 1
        player_3fN_1g.evolve
        player_3fN.evolve
        generic_3fN.evolve
        self.assertEqual(generic_3fN[5][5], generic_3fN[4][5], 1)
        self.assertEqual(generic_3fN[5][4], generic_3fN[5][6], 0)
        self.assertEqual(player_3fN[5][5], player_3fN[4][5], "A1")
        self.assertEqual(player_3fN[5][4], player_3fN[5][6], "A0")
        self.assertEqual(player_3fN_1g[5][5], "A1")
        self.assertEqual(player_3fN_1g[5][4], player_3fN_1g[5][6], "A0")
        self.assertEqual(player_3fN_1g, 1)
        # cell with 3 friendly and 1 other
        generic_3fN_1o = player_3fN_1o = player_3fn_1g = blank_board
        generic_3fN_1o[5][5] = generic_3fN_1o[5][6] = generic_3fN_1o[4][5] = generic_3fN_1o[5][4] = 1
        generic_3fN_1o[6][5] = "A1"
        player_2fN[5][5] = player_2fN[5][6] = player_2fN[4][5] = player_2fN[5][4] = "A1"
        player_3fN[6][5] = "B1" 

        
        player_2fN_1g[5][5] = player_2fN_1g[5][6] = player_2fN_1g[5][4] = "A1"
        player_2fN_1g[4][5] = 1
        player_2fN_1g.evolve
        player_2fN.evolve
        generic_2fN.evolve
        self.assertEqual(generic_2fN[5][5], generic_2fN[4][5], 1)
        self.assertEqual(generic_2fN[5][4], generic_2fN[5][6], 0)
        self.assertEqual(player_2fN[5][5], player_2fN[4][5], "A1")
        self.assertEqual(player_2fN[5][4], player_2fN[5][6], "A0")
        self.assertEqual(player_2fN_1g[5][5], "A1")
        self.assertEqual(player_2fN_1g[5][4], player_2fN_1g[5][6], "A0")
        self.assertEqual(player_2fN_1g, 1)

        
        generic_4N = player_4N = blank_board
        generic_6N = player_6N = blank_board
        empty_generic_0N = empty_player_0N = blank_board
        empty_generic_1N = empty_player_1N = blank_board
        empty_generic_2N = empty_player_2N = blank_board
        empty_generic_1NA_1NB = empty_player_1NA_1NB = blank_board
        empty_generic_2NA_1NB = empty_player_2NA_1NB = blank_board
        empty_generic_2NA_2NB = empty_player_2NA_2NB = blank_board
        empty_generic_3NA = empty_player_3NA = blank_board
"""        
class history_tests(unittest.TestCase):
    """tests the history function's"""
    def test_history(self):
        """Test history saver by changing and saving board and comparing"""
        test003_board = conway.board(5)
        static = test003_board.static_board
        test003_hist = conway.history(static)
        test003_board.aboard[2][2] = 3
        static = test003_board.static_board
        test003_hist.save(static)
        print test003_hist.archive[0]
        print test003_hist.archive[1]
        self.assertNotEqual(test003_hist.archive[0], test003_hist.archive[1])
        
        
if __name__ == "__main__":
    unittest.main()

