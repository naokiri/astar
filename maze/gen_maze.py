from typing import List
import random

from maze import CELL_WALL, CELL_PATH, CELL_START, CELL_GOAL, CELL_SOLVED


class Maze:
    # odd num only
    _ROW_SIZE: int = 21
    _COL_SIZE: int = 21

    def __init__(self) -> None:
        """

        """
        #         check_param(x,y)
        self._grid: List[List[str]] = []
        self.__fill__()
        self.__make_maze__()
        self.__set_start_goal__()

    def __fill__(self):
        for row_num in range(self._ROW_SIZE):
            row: List[str] = []
            for col_num in range(self._COL_SIZE):
                row.append(CELL_WALL)
            self._grid.append(row)

    def __make_maze__(self):
        cross_points: List[tuple[int, int]] = [(1, 1)]
        while len(cross_points) > 0:
            starting_point = random.choice(cross_points)
            cur_x, cur_y = starting_point
            # print(f'current: {cur_x}, {cur_y}')
            # print(self)
            can_continue = True
            while can_continue:
                next_options: List[tuple[int, int]] = []
                for dxy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    dx, dy = dxy
                    try:
                        if cur_x + (dx * 2) > 0 and cur_y + (dy * 2) > 0 and \
                                self._grid[cur_x + (dx * 2)][cur_y + (dy * 2)] == CELL_WALL:
                            next_options.append((dx, dy))
                    except IndexError:
                        # print(f'oob: {dx},{dy}')
                        pass
                # print('next_options:', next_options)
                if len(next_options) == 0:
                    cross_points.remove((cur_x, cur_y))
                    can_continue = False
                else:
                    next_dx, next_dy = random.choice(next_options)
                    self._grid[cur_x + next_dx][cur_y + next_dy] = CELL_PATH
                    self._grid[cur_x + next_dx * 2][cur_y + next_dy * 2] = CELL_PATH
                    cross_points.append((cur_x + next_dx * 2, cur_y + next_dy * 2))
                    cur_x = cur_x + next_dx * 2
                    cur_y = cur_y + next_dy * 2

    def __str__(self) -> str:
        grid_str: str = ''
        for row_cells in self._grid:
            for col_cell_type in row_cells:
                grid_str += col_cell_type
            grid_str += '\n'
        return grid_str

    def __set_start_goal__(self):
        self._grid[1][1] = CELL_START
        self._grid[self._ROW_SIZE - 2][self._COL_SIZE - 2] = CELL_GOAL

    def get_start(self) -> tuple[int, int]:
        for x in range(self._ROW_SIZE):
            for y in range(self._COL_SIZE):
                if self._grid[x][y] == CELL_START:
                    return x, y
        raise IndexError

    def get_goal(self) -> tuple[int, int]:
        for x in range(self._ROW_SIZE):
            for y in range(self._COL_SIZE):
                if self._grid[x][y] == CELL_GOAL:
                    return x, y
        raise IndexError

    def get_node(self, x: int, y: int) -> str:
        return self._grid[x][y]

    def set_solved_path(self, x: int, y: int):
        self._grid[x][y] = CELL_SOLVED
