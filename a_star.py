import numpy as np
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

    # stop condition
    outer_iterations = 0
    # max_iterations = width ** 4

    # all four adjacent moves (up, down, left, right)
    adjacent_moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    while open_list:

        outer_iterations += 1

        current_node = open_list[0]
        current_index = 0

        # finds open node with lowest f score
        for index, open_node in enumerate(open_list):
            if open_node.f < current_node.f:
                current_node = open_node
                current_index = index

        # end pathfinding and return unfinished path
        # if outer_iterations > max_iterations:
        #     print('pathfinding ended, too many iterations')
        #     return reconstruct_path(current_node)

        open_list.pop(current_index)
        closed_list.append(current_node)

        # return path if solution found
        if current_node == end_node:
            print(outer_iterations)
            return reconstruct_path(current_node)

        children = []
        # generate child nodes
        for move in adjacent_moves:
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
            is_closed = False
            for closed_node in closed_list:
                if child_node == closed_node:
                    is_closed = True
                    continue
            if is_closed:
                continue

            child_node.g = current_node.g + 1
            child_node.h = heuristic_cost(child_node.position, end_node.position)
            child_node.f = child_node.g + child_node.h

            in_open_list = False
            for open_node in open_list:
                # >= makes straighter lines, > makes squggly lines
                if child_node == open_node and child_node.g >= open_node.g:
                    # already exists in open list
                    in_open_list = True
                    break
            
            if in_open_list:
                continue

            open_list.append(child_node) 

if __name__ == "__main__":
    graph = {
        'occupied_spaces': [],
        'width': 7,
        'height': 7
    }
    start_position = [0,0]
    goal_position = [6,6]

    path = a_star(graph, start_position, goal_position)
    print('\n', 'path: ', path)