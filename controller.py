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


def position_vector(position):
    return np.array([position['x'], position['y']])


def normalize_vector(vector):
    return vector / np.linalg.norm(vector)


def distance_scalar(vector1, vector2):
    return np.linalg.norm(vector1 - vector2)


def get_snake_direction(body):
    if len(body) == 1:
        return Direction.NONE
    else:
        head = position_vector(body[0])
        neck = position_vector(body[1])
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


def is_unoccupied(position, occupied_positions):
    for occupied_position in occupied_positions:
        if np.array_equal(occupied_position, position):
            return False
    return True


def get_possible_moves(width, height, position, snakes):
    occupied_positions = []
    for snake in snakes:
        for snake_position in snake['body']:
            occupied_positions.append(position_vector(snake_position))

    up = np.add(position, [0, -1])
    down = np.add(position, [0, 1])
    left = np.add(position, [-1, 0])
    right = np.add(position, [1, 0])

    possible_moves = []

    if is_unoccupied(up, occupied_positions) and up[1] > -1:
        possible_moves.append(Direction.UP)
    if is_unoccupied(down, occupied_positions) and down[1] < height:
        possible_moves.append(Direction.DOWN)
    if is_unoccupied(left, occupied_positions) and left[0] > -1:
        possible_moves.append(Direction.LEFT)
    if is_unoccupied(right, occupied_positions) and right[0] < width:
        possible_moves.append(Direction.RIGHT)

    return possible_moves


def get_food_positions(food_list):
    food_positions = []
    for food in food_list:
        food_positions.append(position_vector(food))
    return food_positions


def get_closest_food_position(position, food_positions):
    return min(food_positions, key=lambda x: distance_scalar(x, position))


def determine_move(data):
    # turn = data['turn']
    board = data['board']
    my_snake = data['you']

    height = board['height']
    width = board['width']
    # food = board['food']
    snakes = board['snakes']

    # my_health = my_snake['health']
    my_body = my_snake['body']

    my_head = position_vector(my_body[0])
    # my_snake_direction = get_snake_direction(my_body)

    possible_moves = get_possible_moves(width, height, my_head, snakes)
    # food_positions = get_food_positions(food)
    # closest_food_position = get_closest_food_position(my_head, food_positions)
    move = random.choice(possible_moves).value

    return move


def controller(req):
    # gather data from Battlensake request
    data = {**req}
    # snake logic
    move = determine_move(data)
    return move
