# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import solver
from maze.gen_maze import Maze
from solver.solve import solve, print_path


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = Maze()
    print(a)
    path = solve(a)
    if path is not None:
        print_path(a, path)
    print(a)
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
