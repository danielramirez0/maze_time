from graphics import Line, Point


class Cell:
    def __init__(
        self,
        top_left_cords: tuple,
        bottom_right_cords: tuple,
        window = None,
        visited: bool = False,
    ):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._top_left_cords = top_left_cords
        self._bottom_right_cords = bottom_right_cords
        self._window = window
        self.visited = visited

    def draw(self):
        x1, y1 = self._top_left_cords
        x2, y2 = self._bottom_right_cords
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._window.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._window.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._window.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._window.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._window.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._window.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._window.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._window.draw_line(line, "white")

    def get_center_point(self):
        x1, y1 = self._top_left_cords
        x2, y2 = self._bottom_right_cords
        return Point((x1 + x2) / 2, (y1 + y2) / 2)

    def draw_move(self, to_cell, undo=False):
        if self._window is None:
            return
        center_start = self.get_center_point()
        center_end = to_cell.get_center_point()
        line = Line(center_start, center_end)
        fill_color = "red" if not undo else "gray"
        self._window.draw_line(line, fill_color)
