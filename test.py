import unittest
import PacManSim

# TODO: Suppress print statements while executing code from test file

class TestPacMan(unittest.TestCase):

    # TESTING PLACE COMMAND

    def test_initial_place(self):
        pacman = PacManSim.PacManSimulator()
        pacman.place(2,2,'NORTH')
        expected = "2,2,NORTH"
        self.assertEqual(pacman.report(), expected)

    def test_non_initial_place(self):
        pacman = PacManSim.PacManSimulator()
        pacman.place(4, 4, 'SOUTH')
        pacman.place(0, 0, 'EAST')
        expected = "0,0,EAST"
        self.assertEqual(pacman.report(), expected)

    def test_invalid_place(self):
        pacman = PacManSim.PacManSimulator()
        pacman.place(4, 4, 'SOUTH')
        pacman.place(10, 10, 'NORTH')
        expected = "4,4,SOUTH"
        self.assertEqual(pacman.report(), expected)

    # TESTING VALID MOVES

    def test_move_north(self):
        pacman = PacManSim.PacManSimulator()
        pacman.place(0, 0, 'NORTH')
        pacman.move()
        expected = "0,1,NORTH"
        self.assertEqual(pacman.report(), expected)

    def test_move_south(self):
        pacman = PacManSim.PacManSimulator()
        pacman.place(1, 1, 'SOUTH')
        pacman.move()
        expected = "1,0,SOUTH"
        self.assertEqual(pacman.report(), expected)

    def test_move_east(self):
        pacman = PacManSim.PacManSimulator()
        pacman.place(0, 0, 'EAST')
        pacman.move()
        expected = "1,0,EAST"
        self.assertEqual(pacman.report(), expected)

    def test_move_west(self):
        pacman = PacManSim.PacManSimulator()
        pacman.place(2, 0, 'WEST')
        pacman.move()
        expected = "1,0,WEST"
        self.assertEqual(pacman.report(), expected)

    # TESTING INVALID MOVES FROM SIDES OF GRID

    def test_move_north_when_at_top_of_grid(self):
        pacman = PacManSim.PacManSimulator()
        pacman.place(3, 4, 'NORTH')
        pacman.move()
        expected = "3,4,NORTH"
        self.assertEqual(pacman.report(), expected)

    def test_move_south_when_at_bottom_of_grid(self):
        pacman = PacManSim.PacManSimulator()
        pacman.place(1, 0, 'SOUTH')
        pacman.move()
        expected = "1,0,SOUTH"
        self.assertEqual(pacman.report(), expected)

    def test_move_west_when_at_left_of_grid(self):
        pacman = PacManSim.PacManSimulator()
        pacman.place(0, 3, 'WEST')
        pacman.move()
        expected = "0,3,WEST"
        self.assertEqual(pacman.report(), expected)

    def test_move_east_when_at_right_of_grid(self):
        pacman = PacManSim.PacManSimulator()
        pacman.place(4, 3, 'EAST')
        pacman.move()
        expected = "4,3,EAST"
        self.assertEqual(pacman.report(), expected)

    # TESTING INVALID MOVES FROM CORNERS OF GRID

    def test_move_north_when_at_north_west_of_grid(self):
        pacman = PacManSim.PacManSimulator()
        pacman.place(0, 4, 'NORTH')
        pacman.move()
        expected = "0,4,NORTH"
        self.assertEqual(pacman.report(), expected)

    def test_move_west_when_at_north_west_of_grid(self):
        pacman = PacManSim.PacManSimulator()
        pacman.place(0, 4, 'WEST')
        pacman.move()
        expected = "0,4,WEST"
        self.assertEqual(pacman.report(), expected)

    def test_move_west_when_at_south_west_of_grid(self):
        pacman = PacManSim.PacManSimulator()
        pacman.place(0, 0, 'WEST')
        pacman.move()
        expected = "0,0,WEST"
        self.assertEqual(pacman.report(), expected)

    def test_move_south_when_at_south_west_of_grid(self):
        pacman = PacManSim.PacManSimulator()
        pacman.place(0, 0, 'SOUTH')
        pacman.move()
        expected = "0,0,SOUTH"
        self.assertEqual(pacman.report(), expected)

    def test_move_south_when_at_south_east_of_grid(self):
        pacman = PacManSim.PacManSimulator()
        pacman.place(4, 0, 'SOUTH')
        pacman.move()
        expected = "4,0,SOUTH"
        self.assertEqual(pacman.report(), expected)

    def test_move_east_when_at_south_east_of_grid(self):
        pacman = PacManSim.PacManSimulator()
        pacman.place(4, 0, 'EAST')
        pacman.move()
        expected = "4,0,EAST"
        self.assertEqual(pacman.report(), expected)

    def test_move_east_when_at_north_east_of_grid(self):
        pacman = PacManSim.PacManSimulator()
        pacman.place(4, 4, 'EAST')
        pacman.move()
        expected = "4,4,EAST"
        self.assertEqual(pacman.report(), expected)

    def test_move_north_when_at_north_east_of_grid(self):
        pacman = PacManSim.PacManSimulator()
        pacman.place(4, 4, 'NORTH')
        pacman.move()
        expected = "4,4,NORTH"
        self.assertEqual(pacman.report(), expected)

    # TESTING ROTATING LEFT AND RIGHT

    def test_rotate_left_from_north(self):
        pacman = PacManSim.PacManSimulator()
        pacman.place(2, 0, 'NORTH')
        pacman.rotate('LEFT')
        expected = "2,0,WEST"
        self.assertEqual(pacman.report(), expected)

    def test_rotate_right_from_north(self):
        pacman = PacManSim.PacManSimulator()
        pacman.place(2, 0, 'NORTH')
        pacman.rotate('RIGHT')
        expected = "2,0,EAST"
        self.assertEqual(pacman.report(), expected)

    def test_rotate_left_from_west(self):
        pacman = PacManSim.PacManSimulator()
        pacman.place(2, 0, 'WEST')
        pacman.rotate('LEFT')
        expected = "2,0,SOUTH"
        self.assertEqual(pacman.report(), expected)

    def test_rotate_right_from_west(self):
        pacman = PacManSim.PacManSimulator()
        pacman.place(2, 0, 'WEST')
        pacman.rotate('RIGHT')
        expected = "2,0,NORTH"
        self.assertEqual(pacman.report(), expected)


if __name__ == "__main__":
    unittest.main()
