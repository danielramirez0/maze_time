from tkinter import Tk, BOTH, Canvas


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start_point: Point, end_point: Point):
        self.start = start_point
        self.end = end_point

    def draw(self, canvas: Canvas, color: str, width: int):
        canvas.create_line(
            self.start.x, self.start.y, self.end.x, self.end.y, fill=color, width=width
        )
        canvas.pack(fill=BOTH, expand=1)


class Window:
    def __init__(self, width: int, height: int):
        self.__root_widget = Tk()
        self.__root_widget.title("Maze Solver")
        self.__canvas = Canvas(
            self.__root_widget, bg="white", height=height, width=width
        )
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root_widget.update_idletasks()
        self.__root_widget.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closed...")

    def close(self):
        self.__running = False

    def draw_line(self, line: Line, fill_color: str = "black", width: int = 2):
        line.draw(self.__canvas, fill_color, width)
