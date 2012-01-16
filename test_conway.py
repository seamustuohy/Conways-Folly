import unittest
import conways_game


class check_start(unittest.TestCase):
    def test_visual(self):
        game = conways_game.game_start()
        with_var = conways_game.game_start("visual_start")
        self.assertEqual(game, with_var)
        


if __name__ == "__main__":
    unittest.main()

        
