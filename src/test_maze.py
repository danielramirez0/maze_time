import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(maze._cells), num_cols)
        self.assertEqual(len(maze._cells[0]), num_rows)

    def test_maze_draw_cell(self):
        maze = Maze(0, 0, 5, 5, 100, 100)
        maze._draw_cell(0, 0)
        self.assertEqual(maze._window, None)
        self.assertEqual(maze._cells[0][0]._window, None)

    def test_maze_animate(self):
        maze = Maze(0, 0, 5, 5, 100, 100)
        maze._animate()
        self.assertNotEqual(maze._window, not None)
    
    def test_maze_break_entrance_and_exit(self):
        maze = Maze(0, 0, 5, 5, 100, 100)
        maze._break_entrance_and_exit()
        self.assertEqual(maze._cells[0][0].has_top_wall, False)
        self.assertEqual(maze._cells[0][0].has_left_wall, True)
        self.assertEqual(maze._cells[-1][-1].has_bottom_wall, False)
        self.assertEqual(maze._cells[-1][-1].has_left_wall, True)

    def test_maze_break_entrance_and_exit(self):
        maze = Maze(0, 0, 5, 5, 100, 100)
        maze._break_entrance_and_exit()
        self.assertEqual(maze._cells[0][0].has_top_wall, False)
        self.assertEqual(maze._cells[0][0].has_left_wall, True)
        self.assertEqual(maze._cells[-1][-1].has_bottom_wall, False)
        self.assertEqual(maze._cells[-1][-1].has_right_wall, True)

    def test_maze_break_walls_r(self):
        maze = Maze(0, 0, 5, 5, 100, 100)
        maze._break_walls_r(0, 0)
        self.assertEqual(maze._cells[0][1].has_top_wall, False)
        self.assertEqual(maze._cells[0][2].has_left_wall, True)
        self.assertEqual(maze._cells[0][4].has_left_wall, True)
    
    def test_maze_reset_cells_visited(self):
        maze = Maze(0, 0, 5, 5, 100, 100)
        maze._reset_cells_visited()
        for i in range(maze._num_cols):
            for j in range(maze._num_rows):
                self.assertEqual(maze._cells[i][j].visited, False)
            

if __name__ == "__main__":
    unittest.main()