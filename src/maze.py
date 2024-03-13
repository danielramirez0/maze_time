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
    ):
        self._cells = []
        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_width = cell_width
        self._cell_height = cell_height
        self._window = window

        self._create_cells()

    def _create_cells(self):
        for i in range(self._num_rows):
            column = []
            for j in range(self._num_cols):
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
        for i in range(self._num_rows):
            for j in range(self._num_cols):
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
