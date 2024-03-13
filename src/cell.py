from graphics import Line, Point 


class Cell:
    def __init__(self, window, top_left_cords, bottom_right_cords):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__top_left_cords = top_left_cords
        self.__bottom_right_cords = bottom_right_cords
        self.__window = window

    def draw(self):
        x1, y1 = self.__top_left_cords
        x2, y2 = self.__bottom_right_cords
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.__window.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.__window.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.__window.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.__window.draw_line(line)
