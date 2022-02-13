import heapq
from typing import List, Dict, Optional

from maze import CELL_PASSABLE
from maze.gen_maze import Maze


def solve(maze: Maze) -> Optional[Dict[tuple[int, int], tuple[int, int]]]:
    # Total cost, confirmed cost, x, y
    opend_node: List[tuple[int, int, int, int]] = []
    # (x,y): cost
    closed_node: Dict[tuple[int, int], int] = {}
    # (x1,y1): origin (x2, y2) to reach that point
    path: Dict[tuple[int, int], tuple[int, int]] = {}
    sx, sy = maze.get_start()
    gx, gy = maze.get_goal()
    heapq.heappush(opend_node, (__heuristic_cost__(gx, gy, sx, sy), 0, sx, sy))
    while len(opend_node) > 0:
        (total_cost, confirmed_cost, cur_x, cur_y) = heapq.heappop(opend_node)
        closed_node[(cur_x, cur_y)] = total_cost
        if (cur_x, cur_y) == (gx, gy):
            return path
        next_cands = __next_cand__(maze, cur_x, cur_y)
        for next_x, next_y in next_cands:
            total_cost = __heuristic_cost__(gx, gy, next_x, next_y) + confirmed_cost + 1
            if (next_x, next_y) in closed_node:
                existing_cost = closed_node[(next_x, next_y)]
                if total_cost < existing_cost:
                    heapq.heappush(opend_node, (total_cost, confirmed_cost + 1, next_x, next_y))
                    path[(next_x, next_y)] = cur_x, cur_y
            else:
                heapq.heappush(opend_node, (
                    total_cost, confirmed_cost + 1, next_x, next_y))
                path[(next_x, next_y)] = cur_x, cur_y
    return None


def __next_cand__(maze: Maze, cur_x: int, cur_y: int) -> List[
    tuple[int, int]]:
    res = []
    try:
        for dxy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            dx, dy = dxy
            if CELL_PASSABLE.count(
                    maze.get_node(cur_x + dx, cur_y + dy)) > 0:
                res.append((cur_x + dx, cur_y + dy))
    except IndexError:
        pass
    return res


def __heuristic_cost__(gx: int, gy: int, x: int, y: int) -> int:
    return abs(gx - x) + abs(gy - y)


def print_path(maze: Maze, path: Dict[tuple[int, int], tuple[int, int]]):
    gx, gy = maze.get_goal()
    sx, sy = maze.get_start()
    nx, ny = path[(gx, gy)]
    while (nx, ny) != (sx, sy):
        maze.set_solved_path(nx, ny)
        nx, ny = path[(nx, ny)]
