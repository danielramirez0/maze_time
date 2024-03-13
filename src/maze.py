import time
from cell import Cell
from graphics import Point


class Maze:
    def __init__(
        self,
        x,
        y,
        num_rows,
        num_cols,
        cell_width,
        cell_height,
        window = None,
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
        for row in range(self._num_rows):
            column = []
            for col in range(self._num_cols):
                top_left_cords = (
                    self._x + (col * self._cell_width),
                    self._y + (row * self._cell_height),
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

