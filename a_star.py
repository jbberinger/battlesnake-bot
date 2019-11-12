import numpy as np
import sys
'''
https://en.wikipedia.org/wiki/A*_search_algorithm
http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html
A* finds the shortest path from start to goal. It is an extension of Dijkstra's algorithm.

A* finds the patch that minimizes f(n) = g(n) + h(n)
n: next node on the path
g(n): cost of the path from the start node to n
h(n): heuristic function that estimates cost from n to goal

A* terminates when the path it extends is from start to goal (ie. solution found)
or there are no more paths to extend (ie. no solution)
'''


class Node:
    __slots__ = ('parent_node', 'position', 'f', 'g', 'h')

    def __init__(self, parent_node=None, position=None):
        self.parent_node = parent_node
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return np.array_equal(self.position, other.position)


def reconstruct_path(solution):
    path = []
    while solution is not None:
        path.append(solution.position)
        solution = solution.parent_node
    return path[::-1]

# Manhattan distance
def heuristic_cost(position1, position2):
    return abs(position1[0] - position2[0]) + abs(position1[1] - position2[1])

def a_star(graph, start_position, goal_position):
    occupied_spaces = graph['occupied_spaces']
    width = graph['width']
    height = graph['height']

    start_node = Node(None, start_position)
    end_node = Node(None, goal_position)

    # nodes that have not been fully evaluated
    open_list = [start_node]
    # nodes that have been fully evluated
    closed_list = []

    while open_list:

        current_node = open_list[0]
        current_index = 0

        # displays count
        # i = len(open_list)
        # j = open_list
        # sys.stdout.write("\rLoops %i and open list" % i % j)
        # sys.stdout.flush()
        print(len(open_list))

        # finds open node with lowest f score
        for index, open_node in enumerate(open_list):
            if open_node.f < current_node.f:
                current_node = open_node
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        # return path if solution found
        if current_node == end_node:
            return reconstruct_path(current_node)

        children = []
        # generates valid child nodes
        for move in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_position = np.add(current_node.position, move)

            # check border boundaries
            if new_position[0] not in range(0, width) or new_position[1] not in range(0, height):
                continue

            # check if position is occupied
            is_occupied = False
            for occupied_position in occupied_spaces:
                if np.array_equal(new_position, occupied_position):
                    is_occupied = True
                    break
            if is_occupied:
                continue

            new_node = Node(current_node, new_position)
            children.append(new_node)

        for child_node in children:
            skip = False
            for closed_node in closed_list:
                if child_node == closed_node:
                    skip = True
                    continue
            if skip:
                continue

            child_node.g = current_node.g + 1
            child_node.h = heuristic_cost(child_node.position, end_node.position)
            child_node.f = child_node.g + child_node.h

            for open_node in open_list:
                if child_node == open_node and child_node.g > open_node.g:
                    continue

            open_list.append(child_node) 

if __name__ == "__main__":
    graph = {
        'occupied_spaces': [[1,0],[1,1],[1,2],[1,3]],
        'width': 3,
        'height': 5
    }
    start_position = [0,0]
    goal_position = [2,0]

    path = a_star(graph, start_position, goal_position)
    print('\n', path)