from controller import Direction, get_snake_direction, get_possible_moves, position_vector, get_food_positions
import numpy as np


def test_get_position_vector():
    position_dict = {
        'x': 2,
        'y': 7
    }
    position = position_vector(position_dict)
    expected_position = np.array([2, 7])
    assert np.array_equal(position, expected_position)


def test_direction_NONE():
    snake_body = [
        {
            'x': 2,
            'y': 2
        },
    ]
    snake_direction = get_snake_direction(snake_body)
    assert snake_direction == Direction.NONE


def test_direction_UP():
    snake_body = [
        {
            'x': 2,
            'y': 1
        },
        {
            'x': 2,
            'y': 2
        }
    ]
    snake_direction = get_snake_direction(snake_body)
    assert snake_direction == Direction.UP


def test_direction_LEFT():
    snake_body = [
        {
            'x': 3,
            'y': 2
        },
        {
            'x': 4,
            'y': 2
        }
    ]
    snake_direction = get_snake_direction(snake_body)
    assert snake_direction == Direction.LEFT


def test_direction_RIGHT():
    snake_body = [
        {
            'x': 4,
            'y': 2
        },
        {
            'x': 3,
            'y': 2
        }
    ]
    snake_direction = get_snake_direction(snake_body)
    assert snake_direction == Direction.RIGHT


def test_get_possible_moves_alone():
    snakes = [
        {
            "id": "db9afed1-d45d-4bb0-85d8-f48de5dd3d79",
            "name": "",
            "health": 98,
            "body": [
                {
                    "x": 11,
                    "y": 10
                },
                {
                    "x": 11,
                    "y": 11
                },
                {
                    "x": 10,
                    "y": 11
                },
                {
                    "x": 9,
                    "y": 11
                }
            ]
        }
    ]

    my_head = [11, 12]

    possible_moves = get_possible_moves(15, 15, my_head, snakes)
    expected_possible_moves = [Direction.DOWN, Direction.LEFT, Direction.RIGHT]

    assert np.array_equal(expected_possible_moves, possible_moves)


def test_get_food_positions():

    food = [
        {
            "x": 3,
            "y": 1
        },
        {
            "x": 6,
            "y": 3
        },
        {
            "x": 9,
            "y": 5
        }
    ]

    food_positions = get_food_positions(food)
    print(food_positions)
    expected_food_positions = np.array([[3, 1], [6, 3], [9, 5]])
    print(expected_food_positions)
    assert np.array_equal(expected_food_positions, food_positions)
