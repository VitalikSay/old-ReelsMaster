import numpy as np


def calc_symbol_prob(reel : list, weights : list, symbol : int, window_height : int) -> float:
    """
    This fynction calculates probability of definit symbol considering reel length
    :param reel:
    :param weights:
    :param symbol:
    :param window_height:
    :return:
    """
    weight_counter = 0
    r_len = len(reel)
    inside_reel = reel.copy()
    inside_reel.extend(inside_reel[:window_height-1])
    for i in range(len(reel)):
        segment = inside_reel[i: i + window_height]
        for j in range(len(segment)):
            if segment[j] == symbol:
                weight_counter += weights[i % r_len]
    return weight_counter / np.sum(weights)

print(calc_symbol_prob([1,2,3,4], [1,1,1,1], 4, 3))