import numpy as np
from itertools import combinations


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


def calc_probs(probs_list):
    probs = []
    for i in range(len(probs_list) + 1):
        i_prob = 1
        s = 0
        indexes = [*range(len(probs_list))]

        if i == 0:
            for item in probs_list:
                i_prob *= (1 - item)
            probs.append(i_prob)
            continue

        for comb in combinations(indexes, i):
            i_prob = 1
            for item in comb:
                i_prob *= probs_list[item]
            for item in [n for n in indexes if n not in comb]:
                i_prob *= (1 - probs_list[item])
            s += i_prob
        probs.append(s)
    return probs