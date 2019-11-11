import numpy as np
'''
https://en.wikipedia.org/wiki/A*_search_algorithm
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
        self.f = 0
        self.g = 0
        self.h = 0

    def __eq__(self, other):
        return np.array_equal(self, other)


def reconstruct_path(solution):
    return solution

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

    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0

        # finds open node with lowest f score
        for index, open_node in enumerate(open_list):
            if open_node.f < current_node.f:
                current_node = open_node
                curent_index = index

        open_list.pop(curent_index)
        closed_list.append(current_node)

        # return path if solution found
        if current_node == end_node:
            return reconstruct_path(current_node)

        children = []
        # generates valid child nodes
        for move in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            position = np.add(current_node.position, move)

            # check board bonudaries
            if position[0] > width - 1 or position[1] > height - 1:
                continue
            # check if position is occupied
            if len(filter(lambda x: np.array_equal(position, x)), occupied_spaces) > 0:
                continue

            new_node = Node(current_node, position)
            children.append(new_node)

        for child_node in children:

            for closed_node in closed_list:
                if child_node == closed_node:
                    continue

            child_node.g = current_node.g + 1
            child_node.h = np.linalg.norm(child_node.position, goal_position)
            child_node.f = child_node.g + child_node.h

            for open_node in open_list:
                if child_node == open_node and child_node.g > open_node.g:
                    continue

            open_list.append(child_node) 
