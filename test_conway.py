import unittest
import backend
import game_board



class board_tests(unittest.TestCase):
    def test_init(self):
        """creates board instance from conway and tests __init__'s against static versions"""
        test_board = backend.game(5)
        static = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        self.assertEqual(static, test_board.board)
        test_board02 = backend.game()
        static =  [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
        self.assertEqual(static, test_board02.board)
        self.assertEqual({}, test_board02.players)
        self.assertEqual(0, test_board02.turn)
        self.assertEqual([], test_board02.record)
        
        
    def test_new_board(self):
        """tests if board instance "new_board" function clears existing board on call"""
        test001_board = backend.game(5)
        test001_board.board[1][2] = 5
        test001_board = backend.game(6)
        static = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        self.assertEqual(static, test001_board.board)

    def test_tile_change(self):
        """Tests that tile changer only allows legal replacements

        Two Conditions:
        If tile empty ([0] or [{A-Z}0]) allow add any tile({A-Z or " "}{1 or 0}).
        If tile has active cell({A-Z}1) only remove tile ([0] or [{A-Z}0]).
        """
        test002_board = backend.game(8)
        #test that player tile writes over blank
        test_tile = test002_board.board[2][2]
        test002_board.change_tile((2,2), "A1")
        self.assertNotEqual(test_tile, test002_board.board[2][2]) 
        #test that player tiles will not write over each other
        test002_board.change_tile((2,2), "B1")
        self.assertEqual("A1", test002_board.board[2][2])
        # test that blank player tiles WILL write over player tiles
        test002_board.change_tile((2,2), "A0")
        self.assertEqual("A0", test002_board.board[2][2])
        # test that blank tiles will write over player tiles
        test002_board.change_tile((2,2), "0")
        self.assertEqual("0", test002_board.board[2][2])

    def test_neighbors(self):
        """passes various board positions to the get_neighbor function to test retreival and check for boundry issues."""
        #Setup
        neighbor_board = backend.game(10)
        active_cells = {(2,2):"A1", (2,1):"A0", (1,1):0, (2,3):"C0", (3,2):"A1", (3,1):"B1", (3,3):1, (1,2):"C1", (1,3):"B1"}
        for x, y in active_cells.items():
            neighbor_board.change_tile(x, y)
        # process a full table 
        side_neighborhood = neighbor_board.get_neighbors((2,1), "A0")
        side_result = [0, 0, 'C1', 0, 'A0', 'A1', 0, 'B1', 'A1']
        self.assertEqual(side_neighborhood, side_result)
        #another loc
        mid_neighborhood = neighbor_board.get_neighbors((2,2), "A1")
        mid_result = [0, "C1", "B1", "A0", "A1", "C0", "B1", "A1", 1]
        self.assertEqual(mid_neighborhood, mid_result)
        #another loc
        top_neighborhood = neighbor_board.get_neighbors((1,1), 0)
        top_result = [0, 0, 0, 0, 0, "C1", 0, "A0", "A1"]
        self.assertEqual(top_neighborhood, top_result)
        # process a corner table with only 4 cells on the board.
        tiny_neighborhood = neighbor_board.get_neighbors((0,0), 0)
        tiny_result = [0, 0, 0, 0]
        self.assertEqual(tiny_neighborhood, tiny_result)
        # process a table that gets a single column of left side cut off.
        left_side_neighbor = neighbor_board.get_neighbors((0,2), 0)
        left_side_result = [0, 0, 0, 0, "C1", "B1"]
        self.assertEqual(left_side_neighbor, left_side_result)
    def test_super_neig(self):
        """passes various board positions to the super_neighbor function to make sure that it passes true if a "same type" neihbor exists and fale is it is sad and alone in its neighborhood."""
        #Setup
        neighbor_board = backend.game(10)
        active_cells = {(2,2):"A1", (2,1):"A0", (1,1):0, (2,3):"C0", (3,2):"A1", (3,1):"B1", (3,3):1, (1,2):"C1", (1,3):"B1"}
        for x, y in active_cells.items():
            neighbor_board.change_tile(x, y)
        # 
        side_neighborhood = neighbor_board.super_neighbor((3,3), "A1")
        side_result = True
        self.assertEqual(side_neighborhood, side_result)
        mid_neighborhood = neighbor_board.super_neighbor((2,2), "W1")
        mid_result = False
        self.assertEqual(mid_neighborhood, mid_result)
    def test_mortality(self):
        mortality_game = backend.game(10)
        #Alive Cell Check
        cell = "B1" 
        neighborhood = [0, "C0", "C0", "C0", "B1", "C0", "C0", "C0", 0]
        result = mortality_game.live_or_die(cell, neighborhood)
        self.assertEqual("B0", result) #too little cells
        cell = "B1" 
        neighborhood = [0, "C1", "C1", "C0", "B1", "C0", "C1", "C1", 1]
        result = mortality_game.live_or_die(cell, neighborhood)
        self.assertEqual("B0", result) #too many (enemies)
        cell = "B1" 
        neighborhood = [0, "C1", "C1", "C0", "B1", "C0", "C1", "C0", 0]
        result = mortality_game.live_or_die(cell, neighborhood)
        self.assertEqual("B0", result) #just right (enemies) (= die)
        cell = "B1" 
        neighborhood = [0, "B1", "B1", "C0", "B1", "C0", "C0", "C0", 0]
        result = mortality_game.live_or_die(cell, neighborhood)
        self.assertEqual(cell, result)#just right (friends)
        cell = "B1" 
        neighborhood = [0, "B1", "B1", "B1", "B1", "B1", "B1", "B1", 0]
        result = mortality_game.live_or_die(cell, neighborhood)
        self.assertEqual("B0", result)# too many friends
        cell = "1" 
        neighborhood = [0, "B1", "B1", "C1", 1, "C0", "C0", "C0", 0]
        result = mortality_game.live_or_die(cell, neighborhood)
        self.assertEqual(cell, result) #just right cells
        cell = "1" 
        neighborhood = [1, "B1", "B1", "C1", 1, 1, "C1", "C1", 1]
        result = mortality_game.live_or_die(cell, neighborhood)
        self.assertEqual("0", result) #too many cells
        cell = "1" 
        neighborhood = [0, 0, 0, 0, 1, 0, 0, 0, 0]
        result = mortality_game.live_or_die(cell, neighborhood)
        self.assertEqual("0", result) #too little cells
        #dead cells
        cell = "0" 
        neighborhood = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        result = mortality_game.live_or_die(cell, neighborhood)
        self.assertEqual(cell, result) #too many cells
        cell = "0" 
        neighborhood = [0, 0, 0, 0, 1, 0, 0, 0, 0]
        result = mortality_game.live_or_die(cell, neighborhood)
        self.assertEqual(cell, result) #too few cells
        cell = "1" 
        neighborhood = [0, 0, 0, 0, 1, 1, 1, 1, 0]
        result = mortality_game.live_or_die(cell, neighborhood)
        self.assertEqual(cell, result) #just right cell
        # test common seperately (though it works enought to return cell)
    def test_common(self):
        common_game = backend.game(10)
        cell = 0
        neighborhood = [0, 0, 0, 0, 0, 1, 1, 1]
        result = common_game.common(cell, neighborhood)
        self.assertEqual(1, result)
        cell = 0
        neighborhood = [0, 0, 0, 0, 0, "B1", "B1", "B1", 0]
        result = common_game.common(cell, neighborhood)
        self.assertEqual("B1", result)
        cell = 0
        neighborhood = [0, 0, 0, 0, 0, "B1", "C1", "C1", 0]
        result = common_game.common(cell, neighborhood)
        self.assertEqual("C1", result)
        cell = "C0"
        neighborhood = [0, 0, 0, 0, 0, "B1", "B1", "B1", 0]
        result = common_game.common(cell, neighborhood)
        self.assertEqual("B1", result)
        cell = "W0"
        neighborhood = [0, 0, 0, 0, 0, 1, "B1", "C1", 0]
        result = common_game.common(cell, neighborhood)
        self.assertEqual(1, result)
    def test_score(self):
        score_game = backend.game(10)
        active_cells = {(2,2):"A1", (2,1):"A0", (1,1):0, (2,3):"C0", (3,2):"A1", (3,1):"B1", (3,3):1, (1,2):"C1", (1,3):"B1"}
        for x, y in active_cells.items():
            score_game.change_tile(x, y)
        result = score_game.score()
        print "(A=3, B=2, C=2)"
        print result
    def test_player(self):
        

if __name__ == "__main__":
    unittest.main()

