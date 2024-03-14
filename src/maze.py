import random
import time
from cell import Cell


class Maze:
    def __init__(
        self,
        x,
        y,
        num_rows,
        num_cols,
        cell_width,
        cell_height,
        window=None,
        seed=None,
    ):
        self._cells = []
        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_width = cell_width
        self._cell_height = cell_height
        self._window = window
        self.seed = random.seed(seed) if seed else None

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows):
                top_left_cords = (
                    self._x + (i * self._cell_width),
                    self._y + (j * self._cell_height),
                )
                bottom_right_cords = (
                    top_left_cords[0] + self._cell_width,
                    top_left_cords[1] + self._cell_height,
                )
                column.append(Cell(top_left_cords, bottom_right_cords, self._window))
            self._cells.append(column)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i: int, j: int):
        if self._window is None:
            return
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        if self._window is None:
            return
        self._window.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            adjacent_options = self._get_adjacent_cells(i, j)
            if len(adjacent_options) == 0:
                self._draw_cell(i, j)
                return

            direction_index = random.randrange(len(adjacent_options))
            next_index = adjacent_options[direction_index]

            if next_index[0] == i + 1:  # right
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            if next_index[0] == i - 1:  # left
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            if next_index[1] == j + 1:  # down
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            if next_index[1] == j - 1:  # up
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            self._break_walls_r(next_index[0], next_index[1])

    def _get_adjacent_cells(self, i, j):
        adjacent_cells = []
        if i > 0 and not self._cells[i - 1][j].visited:  # left
            adjacent_cells.append((i - 1, j))
        if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:  # right
            adjacent_cells.append((i + 1, j))
        if j > 0 and not self._cells[i][j - 1].visited:  # up
            adjacent_cells.append((i, j - 1))
        if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:  # down
            adjacent_cells.append((i, j + 1))
        return adjacent_cells

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        current_cell = self._cells[i][j]
        self._animate()
        current_cell.visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        if (  # left
            i > 0
            and not current_cell.has_left_wall
            and not self._cells[i - 1][j].visited
        ):
            current_cell.draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                current_cell.draw_move(self._cells[i - 1][j], True)

        if (  # right
            i < self._num_cols - 1
            and not current_cell.has_right_wall
            and not self._cells[i + 1][j].visited
        ):
            current_cell.draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                current_cell.draw_move(self._cells[i + 1][j], True)
        if (  # up
            j > 0
            and not current_cell.has_top_wall
            and not self._cells[i][j - 1].visited
        ):
            current_cell.draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                current_cell.draw_move(self._cells[i][j - 1], True)
        if (  # down
            j < self._num_rows - 1
            and not current_cell.has_bottom_wall
            and not self._cells[i][j + 1].visited
        ):
            current_cell.draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                current_cell.draw_move(self._cells[i][j + 1], True)
        return False
