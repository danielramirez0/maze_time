from graphics import Window, Line, Point
from cell import Cell
from maze import Maze


def main():

    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_width = (screen_x - 2 * margin) / num_cols
    cell_height = (screen_y - 2 * margin) / num_rows
    window = Window(screen_x, screen_y)

    maze = Maze(
        margin, margin, num_rows, num_cols, cell_width, cell_height, window, 10
    )

    window.wait_for_close()


if __name__ == "__main__":
    main()
