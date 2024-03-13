from graphics import Window, Line, Point
from cell import Cell


def main():
    window = Window(800, 600)

    # point_a = Point(100, 100)
    # point_b = Point(200, 200)
    # line = Line(point_a, point_b)
    # window.draw_line(line, "black")
    # point_a.x = 300
    # point_a.y = 300
    # point_b.x = 400
    # point_b.y = 400
    # next_line = Line(point_a, point_b)
    # window.draw_line(next_line, "red")
    # cell = Cell((0, 100), (0, 100), window)
    # cell.draw()

    c = Cell(window, (10, 10), (50, 50))
    c.has_left_wall = False
    c.draw()

    c = Cell(window, (100, 100), (150, 150))
    c.has_right_wall = False
    c.draw()

    c = Cell(window, (200, 200), (250, 250))
    c.has_bottom_wall = False
    c.draw()

    c = Cell(window, (300, 300), (350, 350))
    c.has_top_wall = False
    c.draw()

    window.wait_for_close()


if __name__ == "__main__":
    main()
