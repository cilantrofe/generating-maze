from src.core.generator import MazeGenerator
from src.core.solver import MazeSolver


# Проверка на то, что лабиринт можно сгенерировать с помощью алгоритма Прима и он нужных размеров
def test_generate_maze_prim():
    generator = MazeGenerator(10, 11)
    generator.generate_prims()
    assert len(generator.maze) == 10
    assert len(generator.maze[0]) == 11


# Проверка на то, что лабиринт можно сгенерировать с помощью алгоритма Краскала и он нужных размеров
def test_generate_maze_kruskal():
    generator = MazeGenerator(10, 11)
    generator.generate_kruskal()
    assert len(generator.maze) == 10
    assert len(generator.maze[0]) == 11


# Тесты проводятся на этом лабиринте 10 на 11, сгенерированном с помощью алгоритма Прима
###########
# # #     #
#     # # #
## # #   ##
#   # # # #
## ## #   #
#  #  # # #
##  #    ##
###  # #  #
###########


# Проверка на то, что существующий путь был найден (BFS)
def test_find_existing_path_bfs():
    maze = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    solver = MazeSolver(maze, (1, 1), (9, 9), 10, 11)
    path = solver.solve_bfs()

    assert path is not None


# Проверка на то, что существующий путь был найден (BFS)
def test_find_existing_path_astar():
    maze = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    solver = MazeSolver(maze, (1, 1), (9, 9), 10, 11)
    path = solver.solve_astar()

    assert path is not None


# Проверка на то, что несуществующий путь не был найден (BFS)
def test_find_not_existing_path_bfs():
    maze = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    solver = MazeSolver(maze, (1, 1), (9, 1), 10, 11)
    path = solver.solve_bfs()

    assert path is None


# Проверка на то, что несуществующий путь не был найден (astar)
def test_find_not_existing_path_astar():
    maze = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    solver = MazeSolver(maze, (1, 1), (9, 1), 10, 11)
    path = solver.solve_astar()

    assert path is None
