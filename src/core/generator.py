import random


class MazeGenerator:
    """Класс для генерации лабиринта"""

    def __init__(self, height: int, width: int):
        self.height, self.width = height, width
        self.maze = [[1] * width for _ in range(height)]

    def generate_prims(self) -> None:
        """Генерация лабиринта алгоритмом Прима"""
        walls = []
        start_x, start_y = random.randint(1, self.height - 2), random.randint(
            1, self.width - 2
        )
        self.maze[start_x][start_y] = 0
        walls.extend(self._add_walls(start_x, start_y))

        while walls:
            wall = random.choice(walls)
            walls.remove(wall)
            x, y = wall

            if self._count_neighbors(x, y) == 1:
                self.maze[x][y] = 0
                walls.extend(self._add_walls(x, y))

    def generate_kruskal(self) -> None:
        """Генерация лабиринта алгоритмом Краскала"""
        parent = {}
        for x in range(1, self.height - 1, 2):
            for y in range(1, self.width - 1, 2):
                parent[(x, y)] = (x, y)
                self.maze[x][y] = 0

        walls = []
        for x in range(1, self.height - 1, 2):
            for y in range(1, self.width - 1, 2):
                if x + 2 < self.height:
                    walls.append((x + 1, y))
                if y + 2 < self.width:
                    walls.append((x, y + 1))

        random.shuffle(walls)

        while walls:
            wall = walls.pop()
            x, y = wall

            if x % 2 == 1:
                cell1, cell2 = (x - 1, y), (x + 1, y)
            else:
                cell1, cell2 = (x, y - 1), (x, y + 1)

            if cell1 not in parent:
                parent[cell1] = cell1
            if cell2 not in parent:
                parent[cell2] = cell2

            if self._find(parent, cell1) != self._find(parent, cell2):
                self._union(parent, cell1, cell2)
                self.maze[x][y] = 0

    def _add_walls(self, x: int, y: int) -> list[tuple[int, int]]:
        """Добавление стен вокруг лабиринта"""
        walls = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            n_x, n_y = x + dr, y + dc
            if 0 < n_x < self.height - 1 and 0 < n_y < self.width - 1:
                if self.maze[n_x][n_y] == 1:
                    walls.append((n_x, n_y))
        return walls

    def _count_neighbors(self, x: int, y: int) -> int:
        """Подсчет количества соседей"""
        count = 0
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            n_x, n_y = x + dr, y + dc
            if 0 <= n_x < self.height and 0 <= n_y < self.width:
                if self.maze[n_x][n_y] == 0:
                    count += 1
        return count

    def _find(
        self, parent: dict[tuple[int, int], tuple[int, int]], cell: tuple[int, int]
    ) -> tuple[int, int]:
        """Нахождение корня дерева"""
        if parent[cell] != cell:
            parent[cell] = self._find(parent, parent[cell])
        return parent[cell]

    def _union(
        self,
        parent: dict[tuple[int, int], tuple[int, int]],
        cell1: tuple[int, int],
        cell2: tuple[int, int],
    ) -> None:
        """Объединение деревьев"""
        root1 = self._find(parent, cell1)
        root2 = self._find(parent, cell2)
        if root1 != root2:
            parent[root1] = root2
