import json
import random
import numpy as np
from enum import Enum


class Direction(Enum):
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
    NONE = None


def get_position_vector(position):
    return np.array([position['x'], position['y']])


def normalize_vector(vector):
    sum_of_squares = np.sum(vector ** 2)
    norm = vector / np.sqrt(sum_of_squares)
    return norm


def get_snake_direction(body):
    if len(body) == 1:
        return Direction.NONE
    else:
        head = np.array([body[0]['x'], body[0]['y']])
        neck = np.array([body[1]['x'], body[1]['y']])
        direction_vector = head - neck
        norm = normalize_vector(direction_vector)
        if np.array_equal(norm, [0, 1]):
            return Direction.DOWN
        elif np.array_equal(norm, [0, -1]):
            return Direction.UP
        elif np.array_equal(norm, [1, 0]):
            return Direction.RIGHT
        elif np.array_equal(norm, [-1, 0]):
            return Direction.LEFT
        else:
            return Direction.NONE


def is_unoccupied(point, occupied_points):
    for occupied_point in occupied_points:
        if np.array_equal(occupied_point, point):
            return False
    return True


def get_possible_moves(width, height, my_head, snakes):

    occupied_points = []

    for snake in snakes:
        for point in snake['body']:
            occupied_points.append(get_position_vector(point))

    # occupied_points = np.array(occupied_points)

    up = np.add(my_head, [0, -1])
    down = np.add(my_head, [0, 1])
    left = np.add(my_head, [-1, 0])
    right = np.add(my_head, [1, 0])

    possible_moves = []

    if is_unoccupied(up, occupied_points) and up[1] > -1:
        possible_moves.append(Direction.UP)
    if is_unoccupied(down, occupied_points) and down[1] < height:
        possible_moves.append(Direction.DOWN)
    if is_unoccupied(left, occupied_points) and left[0] > -1:
        possible_moves.append(Direction.LEFT)
    if is_unoccupied(right, occupied_points) and right[0] < width:
        possible_moves.append(Direction.RIGHT)

    return possible_moves


def get_food_positions(food_dict):
    food_positions = []
    for food in food_dict:
        food_positions.append(get_position_vector(food))
    return food_positions


def controller(req):
    '''
    Gather board data from Battlensake request
    '''

    turn = req['turn']
    board = req['board']
    my_snake = req['you']

    height = board['height']
    width = board['width']
    food = board['food']
    snakes = board['snakes']

    my_health = my_snake['health']
    my_body = my_snake['body']

    my_head = get_position_vector(my_body[0])

    my_snake_direction = get_snake_direction(my_body)

    '''
    Snake logic
    '''
    possible_moves = get_possible_moves(width, height, my_head, snakes)
    food_positions = get_food_positions(food)
    move = random.choice(possible_moves).value

    return move
