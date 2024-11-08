import logging
import platform

from core.generator import MazeGenerator
from core.solver import MazeSolver

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)


class MazeUI:
    GREETING = "Привет! Это программа для генерации лабиринта и поиска пути в нём."
    VALUE_ERROR = "Некорректный ввод. Попробуй ещё раз."

    INPUT_HEIGHT = "Введи высоту лабиринта: "
    INPUT_WIDTH = "Введи ширину лабиринта: "
    SIZE_ERROR = "Высота и ширина должны быть положительными."

    INPUT_START_POINT = "Введи координаты начальной точки через пробел: "
    INPUT_END_POINT = "Введи координаты конечной точки через пробел: "

    INPUT_GENERATOR = "Выбери алгоритм генерации лабиринта (1 - Прим, 2 - Краскал): "
    INPUT_SOLVER = "Выберите алгоритм поиска пути (1 - Поиск в ширину, 2 - A*): "

    def __init__(self):
        self.height, self.width = None, None
        self.start, self.end = None, None
        self.generator = None
        self.solver = None

    def _choose_size(self) -> tuple[int, int]:
        """Выбор размера лабиринта"""
        try:
            height = int(input(self.INPUT_HEIGHT))
            width = int(input(self.INPUT_WIDTH))
            if height > 0 and width > 0:
                return height, width
            else:
                print(self.SIZE_ERROR)
                self._choose_size()
        except ValueError:
            print(self.VALUE_ERROR)
            self._choose_size()

    def _choose_point(self, message: str) -> tuple[int, int]:
        """Выбор начальной и конечной точки"""
        try:
            x, y = map(int, input(message).split())
            if 0 <= x < self.height - 1 and 0 <= y < self.width - 1:
                return x, y
            else:
                print(
                    f"Координаты должны быть в пределах от 1 до {self.height - 2} для x и от 1 до {self.width - 2} для y."
                )
                self._choose_point(message)
        except ValueError:
            print(self.VALUE_ERROR)
            self._choose_point(message)

    def _choose_generator(self) -> None:
        """Выбор алгоритма генерации лабиринта"""
        choice = input(self.INPUT_GENERATOR)
        if choice == "1":
            self.generator = MazeGenerator(self.height, self.width)
            self.generator.generate_prims()
        elif choice == "2":
            self.generator = MazeGenerator(self.height, self.width)
            self.generator.generate_kruskal()
        else:
            print(self.VALUE_ERROR)
            self._choose_generator()

    def _choose_solver(self) -> list[tuple[int, int]]:
        """Выбор алгоритма поиска пути"""
        choice = input(self.INPUT_SOLVER)
        self.solver = MazeSolver(
            self.generator.maze, self.start, self.end, self.height, self.width
        )

        path = None

        if choice == "1":
            path = self.solver.solve_bfs()
        elif choice == "2":
            path = self.solver.solve_astar()
        else:
            print(self.VALUE_ERROR)
            self._choose_solver()

        return path

    def display_maze(self) -> None:
        for row in self.generator.maze:
            print("".join("#" if cell else " " for cell in row))

    def display_path(self, path: list[tuple[int, int]]) -> None:
        if not path:
            print("Путь не найден")
            return None

        for x in range(self.height):
            for y in range(self.width):
                if (x, y) == self.start or (x, y) == self.end:
                    print("○", end="")
                elif (x, y) in path:
                    print("●", end="")
                else:
                    print("#" if self.solver.maze[x][y] == 1 else " ", end="")
            print()

    def run(self) -> None:
        """Запуск программы"""
        print(self.GREETING)

        self.height, self.width = self._choose_size()

        self._choose_generator()
        self.display_maze()

        self.start, self.end = self._choose_point(
            self.INPUT_START_POINT
        ), self._choose_point(self.INPUT_END_POINT)

        path = self._choose_solver()
        self.display_path(path)


def main() -> None:
    logger.info(platform.python_version())

    ui = MazeUI()
    ui.run()


if __name__ == "__main__":
    main()
