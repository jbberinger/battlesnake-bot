from src.a_star import a_star
import numpy as np


def test_a_star__straight__no_obstacles():
    graph = {
        'occupied_positions': [],
        'width': 5,
        'height': 5
    }
    start_position = [0,0]
    goal_position = [0,4]

    path_length = len(a_star(graph, start_position, goal_position))
    expected_path_length = 4

    assert np.array_equal(path_length, expected_path_length)

def test_a_star__one_obstacle():
    graph = {
        'occupied_positions': [[2,0]],
        'width': 5,
        'height': 5
    }
    start_position = [0,0]
    goal_position = [3,0]

    path_length = len(a_star(graph, start_position, goal_position))
    expected_path_length = 5

    assert np.array_equal(path_length, expected_path_length)

def test_a_star__two_obstacles():
    graph = {
        'occupied_positions': [[2,0], [2,1]],
        'width': 5,
        'height': 5
    }
    start_position = [0,0]
    goal_position = [3,0]

    path_length = len(a_star(graph, start_position, goal_position))
    expected_path_length = 7

    assert np.array_equal(path_length, expected_path_length)

def test_a_star__three_obstacles():
    graph = {
        'occupied_positions': [[2,0], [2,1], [2,2]],
        'width': 5,
        'height': 5
    }
    start_position = [0,0]
    goal_position = [3,0]

    path_length = len(a_star(graph, start_position, goal_position))
    expected_path_length = 9

    assert np.array_equal(path_length, expected_path_length)

def test_a_star__hook():
    graph = {
        'occupied_positions': [[1,0],[1,1],[1,2],[1,3],[2,3],[3,3],[3,2],[3,1]],
        'width': 5,
        'height': 5
    }
    start_position = [0,0]
    goal_position = [2,2]

    path_length = len(a_star(graph, start_position, goal_position))
    expected_path_length = 16

    assert np.array_equal(path_length, expected_path_length)

def test_a_star__15x15__no_obstacles():
    graph = {
        'occupied_positions': [],
        'width': 15,
        'height': 15
    }
    start_position = [0,0]
    goal_position = [14,14]

    path_length = len(a_star(graph, start_position, goal_position))
    expected_path_length = 28

    assert np.array_equal(path_length, expected_path_length)

def test_a_star__20x20__no_obstacles():
    graph = {
        'occupied_positions': [],
        'width': 20,
        'height': 20
    }
    start_position = [0,19]
    goal_position = [19,0]

    path_length = len(a_star(graph, start_position, goal_position))
    expected_path_length = 38

    assert np.array_equal(path_length, expected_path_length)

def test_a_star__20x20__long_wall():
    graph = {
        'occupied_positions': [[6,y] for y in range(1,20)],
        'width': 20,
        'height': 20
    }
    start_position = [0,19]
    goal_position = [19,19]

    path_length = len(a_star(graph, start_position, goal_position))
    expected_path_length = 57

    assert np.array_equal(path_length, expected_path_length)