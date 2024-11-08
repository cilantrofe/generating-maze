from collections import deque
from heapq import heappop, heappush


class MazeSolver:
    """Класс для решения лабиринта"""

    def __init__(
        self,
        maze: list[list[int]],
        start: tuple[int, int],
        end: tuple[int, int],
        height: int,
        width: int,
    ):
        self.start, self.end = start, end

        maze[start[0]][start[1]] = 0
        maze[end[0]][end[1]] = 0

        self.maze = maze
        self.height, self.width = height, width

    def solve_bfs(self) -> list[tuple[int, int]] | None:
        """Поиск в ширину (BFS)"""
        queue = deque([self.start])
        visited = set()
        vertices = {}
        visited.add(self.start)

        while queue:
            curr = queue.popleft()

            if curr == self.end:
                return self._rpath(vertices, curr)

            for neighbor in self._get_neighbors(curr):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    vertices[neighbor] = curr

        return None

    def solve_astar(self) -> list[tuple[int, int]] | None:
        """Алгоритм поиска пути A*"""
        list = []
        heappush(list, (0, self.start))
        vertices = {}
        g_score = {self.start: 0}
        f_score = {self.start: self._heuristic(self.start)}

        visited = set()

        while list:
            _, curr = heappop(list)

            if curr == self.end:
                return self._rpath(vertices, curr)

            visited.add(curr)

            for neighbor in self._get_neighbors(curr):
                if neighbor in visited:
                    continue

                t_g_score = g_score[curr] + 1

                if neighbor not in g_score or t_g_score < g_score[neighbor]:
                    vertices[neighbor] = curr
                    g_score[neighbor] = t_g_score
                    f_score[neighbor] = t_g_score + self._heuristic(neighbor)
                    heappush(list, (f_score[neighbor], neighbor))

        return None

    def _get_neighbors(self, cell: tuple[int, int]) -> list[tuple[int, int]]:
        """Получение соседей"""
        neighbors = []
        x, y = cell
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            n_x, n_y = x + dr, y + dc
            if 0 <= n_x < self.height and 0 <= n_y < self.width:
                if self.maze[n_x][n_y] == 0:
                    neighbors.append((n_x, n_y))
        return neighbors

    def _heuristic(self, cell: tuple[int, int]) -> int:
        """Эвристическая функция для A*"""
        x1, y1 = cell
        x2, y2 = self.end
        return abs(x1 - x2) + abs(y1 - y2)

    def _rpath(
        self,
        vertices: dict[tuple[int, int], tuple[int, int]],
        curr: tuple[int, int],
    ) -> list[tuple[int, int]]:
        """Реконструирование пути"""
        path = []
        while curr in vertices:
            path.append(curr)
            curr = vertices[curr]
        path.reverse()
        return path
