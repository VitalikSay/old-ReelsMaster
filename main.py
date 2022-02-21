from Libs.IO_data import create_xml_realsets
from collections import defaultdict
import numpy as np


# ШАГ 1: СОЗДАЕМ РИЛ И ШАФЛИМ ЕГО (ЭТО ФУНКЦИЯ ОТДЕЛЬНО НЕ ИСПОЛЬЗУЕТСЯ, ОНА ВХОДИТ В СОСТАВ ШАГА 2)

def create_reel(stacks, number_of_stacks):
    if len(stacks) != len(number_of_stacks):
        print("len(stack) != len(number_of_stacks)")
        return 0
    list_with_stacks = []
    for i in range(len(stacks)):
        for _ in range(number_of_stacks[i]):
            list_with_stacks.append(stacks[i])
    indexes = [*range(len(list_with_stacks))]
    res_list = []
    for i in range(len(list_with_stacks)):
        rand_index = np.random.choice(indexes)
        del indexes[indexes.index(rand_index)]
        res_list.append(list_with_stacks[rand_index])
    return res_list


# ШАГ 2: ДЕЛАЕМ ТАК, ЧТО БЫ В ГОТОВОМ РИЛЕ НЕ БЫЛО ОДИНАКОВЫХ СИМВОЛОВ НА РАССТОЯНИИ <= 2 СИМВОЛА
# Разные стаки в этой функции могут появиться рядом (например [1,1,1,2,2,2])

def reel_processing(stacks, number_of_stacks):
    reel = create_reel(stacks, number_of_stacks)
    need_change_reel = False
    ln = len(reel)
    for i in range(len(reel)):

        cur_symb = reel[i][0]
        if len(reel[i-1]) == 1:
            left_neighbors = [reel[i-2][0], reel[i-1][0]]
        else:
            left_neighbors = reel[i-1][:2]
        if len(reel[(i+1) % ln]) == 1:
            right_neighbors = [reel[(i+1) % ln][0], reel[(i+2) % ln][0]]
        else:
            right_neighbors = reel[(i+1) % ln][:2]

        if (cur_symb in left_neighbors) or (cur_symb in right_neighbors):
            need_change = True
            for j in range(len(reel)):

                inside_cur_symb = reel[j][0]
                if len(reel[j-1]) == 1:
                    inside_left_neigh = [reel[j-2][0], reel[j-1][0]]
                else:
                    inside_left_neigh = reel[j-1][:2]
                if len(reel[(j+1) % ln]) == 1:
                    inside_right_neigh = [reel[(j+1) % ln][0], reel[(j+2) % ln][0]]
                else:
                    inside_right_neigh = reel[(j+1) % ln][:2]

                if (cur_symb not in inside_left_neigh) and (cur_symb not in inside_right_neigh)\
                        and (inside_cur_symb not in left_neighbors) and (inside_cur_symb not in right_neighbors):
                    temp = reel[i]
                    reel[i] = reel[j]
                    reel[j] = temp
                    need_change = False
                    break
            if need_change:
                need_change_reel = True
                break
    if need_change_reel:
        reel = reel_processing(stacks, number_of_stacks)
    return reel

# ШАГ 3: ПРОВЕРКА РИЛА НА ПРАВИЛЬНОСТЬ

# Возвращает True если все хорошо, False если есть ошибочки


def check_reel(test, symbols, number_of_symbols, special_symbol, number_of_sp_symbols):
    symbols.append(special_symbol)
    number_of_symbols.append(number_of_sp_symbols)
    dct = defaultdict(int)
    l = len(test)
    counter = 0
    for i in range(len(test)):
        dct[test[i]] += 1
        if (test[i] == test[i-1]) or (test[i] == test[(i+1)%l]):
            counter += 1
    error_in_dict = False
    for symb, num in dct.items():
        if num == number_of_symbols[symbols.index(symb)]:
            continue
        else:
            error_in_dict = True
    if (counter == 0) and (not error_in_dict):
        return True
    else:
        return False


# ШАГ 4: ВСТАВКА СПЕЦИАЛЬНОГО СИМВОЛА (ВАЙЛД, СКАТТЕР)


def insert_special_symbols(stack_reel, special_symbols, number_of_sp_symbols, step_between_sp_symbols):

    """
    top_indexes_to_insert = []
    ln = len(stack_reel)

    # Места между двумя большими стаками - лучшие для вставки
    for i in range(len(stack_reel)):
        if len(stack_reel[i]) > 1 and len(stack_reel[(i+1) % ln]) > 1:
            top_indexes_to_insert.append((i+1) % ln)

    max_step_between_symbols = max(step_between_sp_symbols)
    for i in range(len(top_indexes_to_insert) - 1):
        cur_dist = 0
        between_indexes = range(top_indexes_to_insert[i], top_indexes_to_insert[i+1])
        for j in between_indexes:
            cur_dist += len(stack_reel[j])
        if cur_dist > max_step_between_symbols:
            continue
        else:
            del top_indexes_to_insert[i]

    sp_symbol_counter = sum(number_of_sp_symbols)
    plus_counter = 0
    for i in range(len(top_indexes_to_insert)):
        rand_sp_symbol = np.random.choice(special_symbols)
        stack_reel.insert(top_indexes_to_insert[i] + plus_counter, rand_sp_symbol)
        plus_counter += 1
        number_of_sp_symbols[sp_symbol_counter.__index__(rand_sp_symbol)] -= 1

    """
    final_reel = []
    for stack in stack_reel:
        final_reel += stack
    return final_reel

    """
    ln = len(final_reel)
    indexes_to_insert = []
    for i in range(len(final_reel)):
        if final_reel[i] != final_reel[(i+1) % ln]:
            indexes_to_insert.append(i+1)

    max_dist_bet_sp_symbols = max(step_between_sp_symbols)
    i = 0
    while(True):
        dist = 0
        if i+1 >= ln:
            dist = ln - indexes_to_insert[i] + indexes_to_insert[0]
        else:
            dist = indexes_to_insert[i+1] - indexes_to_insert[i]
        if dist < max_dist_bet_sp_symbols:
            del indexes_to_insert[i]
    print(indexes_to_insert)
    return final_reel









    

    max_step_between_symbols = max(step_between_sp_symbols)
    indexes_to_insert = [*range(0, len(stack_reel)-4)]
    cur_dist = 0
    for i in range(len(indexes_to_insert)-2):
        between_indexes = [*range(indexes_to_insert[i], indexes_to_insert[i+1])]

        cur_dist = sum([len(stack_reel[i]) for i in between_indexes])
        print(between_indexes, cur_dist)
        if cur_dist > max_step_between_symbols:
            continue
        else:
            del indexes_to_insert[i]

    if sum(number_of_sp_symbols) > len(indexes_to_insert):
        print("not enough places to insert all special symbols, will be insert ", indexes_to_insert, " symbols")
    insert_indexes = []
    sp_symbols = []
    for i in range(len(special_symbols)):
        for count in range(number_of_sp_symbols[i]):
            sp_symbols.append(sp_symbols[i])

    plus_count = 0
    while len(indexes_to_insert) != 0 and len(sp_symbols) != 0:
        rand_sp_symbol = np.random.choice(sp_symbols)
        del sp_symbols[sp_symbols.index(rand_sp_symbol)]
        stack_reel.insert(rand_sp_symbol, indexes_to_insert[0 + plus_count])
        plus_count += 1
        del indexes_to_insert[0]

    return stack_reel
    """


# ШАГ 5: ПРОВЕРКА ПРАВИЛЬНОСТИ ВСТАВКИ СПЕЦИАЛЬНОГО СИМВОЛА

# ЕСЛИ ВСЕ ОК ТО ВОЗВРАЩАЕТ TRUE, ИНАЧЕ FALSE

def check_special_symbols(reel, special_symbol, step_between_sp_symbols, number_of_sp_symbols):
    error_in_step = False
    error_in_count = False
    special_symbol_positions = []
    for i in range(len(reel)):
        if reel[i] == special_symbol:
            special_symbol_positions.append(i)
    steps_between_sp_symbols = []
    for i in range(1, len(special_symbol_positions)):
        steps_between_sp_symbols.append(special_symbol_positions[i] - special_symbol_positions[i-1])
    if (number_of_sp_symbols != 0):
        steps_between_sp_symbols.append(special_symbol_positions[0] + len(reel) - special_symbol_positions[-1] - 1)
    for _ in steps_between_sp_symbols:
        if _ < step_between_sp_symbols:
            error_in_step = True
    if len(special_symbol_positions) != number_of_sp_symbols:
        error_in_count = True
    if error_in_step or error_in_count:
        return False
    else:
        return True


def create_and_check_reel(symbols,
                          number_of_symbols,
                          special_symbol,
                          number_of_sp_symbols,
                          step_between_sp_symbols,
                          symbol_stack_dict):
    reel_without_sp_symbols_and_stack = reel_processing(symbols, number_of_symbols)
    reel_with_sp_symbols = insert_special_symbols(reel_without_sp_symbols_and_stack, special_symbol,number_of_sp_symbols, step_between_sp_symbols)

    return reel_without_sp_symbols_and_stack



def create_weights(reel, weight_to_input, wild_symbol, window_height, reel_number):
    r_copy = reel.copy()
    weight = [1 for _ in range(len(r_copy))]
    while(weight_to_input != 0):
        for i in range(len(reel)):
            if reel[i] == wild_symbol:
                weight[i] += 1
                weight_to_input -= 1
                if (weight_to_input == 0):
                    break
    return weight

    rl = len(reel)
    r_copy.extend(r_copy[0:window_height])
    while weight_to_input != 0:
        for i in range(rl):

            window = r_copy[i:(i + window_height)]
            royal_count = 0

            if window.count(wild_symbol) > 0:
                weight[i] = 2
                continue

            for el in window:
                if el > 3 and el < 9:
                    royal_count += 1
            if royal_count != 2 and reel_number < 3:
                continue

            weight[i] += 1
            weight_to_input -= 1
            if weight_to_input == 0:
                break
    return weight


def FinalReel(stack_reel):
    final_reel = []
    for stack in stack_reel:
        final_reel += stack
    return final_reel


def CheckDistBetweenWilds(cur_reel, wild_symb, min_step_between_wilds):
    if wild_symb not in cur_reel:
        return True
    wild_indexes = []
    for i in range(len(cur_reel)):
        if cur_reel[i] == wild_symb:
            wild_indexes.append(i)

    for i in range(len(wild_indexes)-1):
        if wild_indexes[i+1] - wild_indexes[i] < min_step_between_wilds:
            return False
        continue

    if len(cur_reel) - 1 - wild_indexes[-1] + wild_indexes[0] < min_step_between_wilds:
        return False
    return True





first_reel_stacks = [[0], [0, 0], [0, 0, 0],
                     [1], [1, 1], [1, 1, 1],
                     [2], [2, 2], [2, 2, 2],
                     [3], [3, 3], [3, 3, 3],
                     [4], [4, 4], [4, 4, 4],
                     [5], [5, 5], [5, 5, 5],
                     [6], [6, 6], [6, 6, 6],
                     [7], [7, 7], [7, 7, 7],
                     [8], [8, 8], [8, 8, 8],
                     [9], [9, 9], [9, 9, 9]]
first_reel_number_of_stacks = [10, 6, 3,
                               10, 6, 3,
                               10, 6, 3,
                               10, 6, 3,
                               10, 6, 3,
                               12, 0, 0,
                               12, 0, 0,
                               12, 0, 0,
                               12, 0, 0,
                               12, 0, 0]
second_reel_stacks = [[0], [0, 0], [0, 0, 0],
                      [1], [1, 1], [1, 1, 1],
                      [2], [2, 2], [2, 2, 2],
                      [3], [3, 3], [3, 3, 3],
                      [4], [4, 4], [4, 4, 4],
                      [5], [5, 5], [5, 5, 5],
                      [6], [6, 6], [6, 6, 6],
                      [7], [7, 7], [7, 7, 7],
                      [8], [8, 8], [8, 8, 8],
                      [9], [9, 9], [9, 9, 9],
                      [11]]
second_reel_number_of_stacks = [10, 6, 3,
                                10, 6, 3,
                                10, 6, 3,
                                10, 6, 3,
                                10, 6, 3,
                                12, 0, 0,
                                12, 0, 0,
                                12, 0, 0,
                                12, 0, 0,
                                12, 0, 0,
                                10]

third_reel_stacks = [[0], [0, 0], [0, 0, 0],
                     [1], [1, 1], [1, 1, 1],
                     [2], [2, 2], [2, 2, 2],
                     [3], [3, 3], [3, 3, 3],
                     [4], [4, 4], [4, 4, 4],
                     [5], [5, 5], [5, 5, 5],
                     [6], [6, 6], [6, 6, 6],
                     [7], [7, 7], [7, 7, 7],
                     [8], [8, 8], [8, 8, 8],
                     [9], [9, 9], [9, 9, 9],
                     [11]]
third_reel_number_of_stacks = [10, 6, 3,
                               10, 6, 3,
                               10, 6, 3,
                               10, 6, 3,
                               10, 6, 3,
                               12, 0, 0,
                               12, 0, 0,
                               12, 0, 0,
                               12, 0, 0,
                               12, 0, 0,
                               16]

fourth_reel_stacks = [[0], [0, 0], [0, 0, 0],
                      [1], [1, 1], [1, 1, 1],
                      [2], [2, 2], [2, 2, 2],
                      [3], [3, 3], [3, 3, 3],
                      [4], [4, 4], [4, 4, 4],
                      [5], [5, 5], [5, 5, 5],
                      [6], [6, 6], [6, 6, 6],
                      [7], [7, 7], [7, 7, 7],
                      [8], [8, 8], [8, 8, 8],
                      [9], [9, 9], [9, 9, 9],
                      [11]]
fourth_reel_number_of_stacks = [10, 6, 3,
                                10, 6, 3,
                                10, 6, 3,
                                10, 6, 3,
                                10, 6, 3,
                                12, 0, 0,
                                12, 0, 0,
                                12, 0, 0,
                                12, 0, 0,
                                12, 0, 0,
                                14]

fifth_reel_stacks = [[0], [0, 0], [0, 0, 0],
                     [1], [1, 1], [1, 1, 1],
                     [2], [2, 2], [2, 2, 2],
                     [3], [3, 3], [3, 3, 3],
                     [4], [4, 4], [4, 4, 4],
                     [5], [5, 5], [5, 5, 5],
                     [6], [6, 6], [6, 6, 6],
                     [7], [7, 7], [7, 7, 7],
                     [8], [8, 8], [8, 8, 8],
                     [9], [9, 9], [9, 9, 9],]
fifth_reel_number_of_stacks = [10, 6, 3,
                               10, 6, 3,
                               10, 6, 3,
                               10, 6, 3,
                               10, 6, 3,
                               12, 0, 0,
                               12, 0, 0,
                               12, 0, 0,
                               12, 0, 0,
                               12, 0, 0]


def create_weights(reel, weight_to_input, wild_symbol, wild_weight, window_height, reel_number):
    r_copy = reel.copy()
    weight = [1 for _ in range(len(r_copy))]

    # ВЕСА НА ВАЙЛДЫ
    while(wild_weight != 0):
        for i in range(len(reel)):
            window = r_copy[i: i+window_height]
            if wild_symbol in window:
                weight[i] += 1
                wild_weight -= 1
                if (wild_weight == 0):
                    break

    while(weight_to_input > 0):
        for i in range(len(reel)):
            window = r_copy[i: i+window_height]
            if wild_symbol in window:
                continue

            reach_pic_counter = 0
            cheap_pic_counter = 0
            royal_counter = 0
            for symb in window:
                if symb in [0, 1, 2]:
                    reach_pic_counter += 1
                elif symb in [3, 4]:
                    cheap_pic_counter += 1
                elif symb in [5, 6, 7, 8, 9]:
                    royal_counter += 1
            pic_counter = reach_pic_counter + cheap_pic_counter

            if (reel_number == 1):
                if pic_counter == 2:
                    if reach_pic_counter == 2:
                        weight[i] += 2
                        weight_to_input -= 2
                    elif reach_pic_counter == 1:
                        weight[i] += 3
                        weight_to_input -= 3
                    elif reach_pic_counter == 0:
                        weight[i] += 1
                        weight_to_input -= 1
                elif pic_counter == 3:
                    if reach_pic_counter in [2, 3]:
                        weight[i] += 3
                        weight_to_input -= 3
                    else:
                        weight[i] += 2
                        weight_to_input -= 2
                elif pic_counter == 1:
                    weight[i] += 1
                    weight_to_input -= 1
                if weight_to_input <= 0:
                    break


            if (reel_number == 2):
                if pic_counter == 2:
                    if reach_pic_counter == 2:
                        weight[i] += 1
                        weight_to_input -= 1
                    elif reach_pic_counter == 1:
                        weight[i] += 2
                        weight_to_input -= 2
                    elif reach_pic_counter == 0:
                        weight[i] += 3
                        weight_to_input -= 3
                elif pic_counter == 3:
                    if reach_pic_counter in [2, 3]:
                        weight[i] += 1
                        weight_to_input -= 1
                    else:
                        weight[i] += 3
                        weight_to_input -= 3
                elif pic_counter == 1:
                    weight[i] += 1
                    weight_to_input -= 1
                if weight_to_input <= 0:
                    break

            if (reel_number == 3):
                if pic_counter == 2:
                    if reach_pic_counter == 2:
                        weight[i] += 2
                        weight_to_input -= 2
                    elif reach_pic_counter == 1:
                        weight[i] += 3
                        weight_to_input -= 3
                    elif reach_pic_counter == 0:
                        weight[i] += 1
                        weight_to_input -= 1
                elif pic_counter == 3:
                    if reach_pic_counter in [2, 3]:
                        weight[i] += 3
                        weight_to_input -= 3
                    else:
                        weight[i] += 2
                        weight_to_input -= 2
                elif pic_counter == 1:
                    weight[i] += 1
                    weight_to_input -= 1
                if weight_to_input <= 0:
                    break


            if (reel_number == 4):
                if pic_counter == 2:
                    if reach_pic_counter == 2:
                        weight[i] += 1
                        weight_to_input -= 1
                    elif reach_pic_counter == 1:
                        weight[i] += 1
                        weight_to_input -= 1
                    elif reach_pic_counter == 0:
                        weight[i] += 2
                        weight_to_input -= 2
                elif pic_counter == 3:
                    if reach_pic_counter in [2, 3]:
                        weight[i] += 0
                        weight_to_input -= 0
                    else:
                        weight[i] += 1
                        weight_to_input -= 1
                elif pic_counter == 1:
                    weight[i] += 3
                    weight_to_input -= 3
                if weight_to_input <= 0:
                    break

            if (reel_number == 5):
                if pic_counter == 2:
                    if reach_pic_counter == 2:
                        weight[i] += 1
                        weight_to_input -= 1
                    elif reach_pic_counter == 1:
                        weight[i] += 1
                        weight_to_input -= 1
                    elif reach_pic_counter == 0:
                        weight[i] += 2
                        weight_to_input -= 2
                elif pic_counter == 3:
                    if reach_pic_counter in [2, 3]:
                        weight[i] += 0
                        weight_to_input -= 0
                    else:
                        weight[i] += 1
                        weight_to_input -= 1
                elif pic_counter == 1:
                    weight[i] += 3
                    weight_to_input -= 3
                if weight_to_input <= 0:
                    break

    return weight




np.random.seed(42)
reel_1 = reel_processing(first_reel_stacks, first_reel_number_of_stacks)
np.random.seed(42)
reel_2 = reel_processing(second_reel_stacks, second_reel_number_of_stacks)
np.random.seed(48)
reel_3 = reel_processing(third_reel_stacks, third_reel_number_of_stacks)
np.random.seed(42)
reel_4 = reel_processing(fourth_reel_stacks, fourth_reel_number_of_stacks)
np.random.seed(47)
reel_5 = reel_processing(fifth_reel_stacks, fifth_reel_number_of_stacks)


"""
REACH REELSET
np.random.seed(42)
reel_1 = reel_processing(first_reel_stacks, first_reel_number_of_stacks)
np.random.seed(42)
reel_2 = reel_processing(second_reel_stacks, second_reel_number_of_stacks)
np.random.seed(48)
reel_3 = reel_processing(third_reel_stacks, third_reel_number_of_stacks)
np.random.seed(42)
reel_4 = reel_processing(fourth_reel_stacks, fourth_reel_number_of_stacks)
np.random.seed(47)
reel_5 = reel_processing(fifth_reel_stacks, fifth_reel_number_of_stacks)
"""

reel_1 = FinalReel(reel_1)
reel_2 = FinalReel(reel_2)
reel_3 = FinalReel(reel_3)
reel_4 = FinalReel(reel_4)
reel_5 = FinalReel(reel_5)

if all([CheckDistBetweenWilds(reel_1, 11, 3),
        CheckDistBetweenWilds(reel_2, 11, 3),
        CheckDistBetweenWilds(reel_3, 11, 3),
        CheckDistBetweenWilds(reel_4, 11, 3),
        CheckDistBetweenWilds(reel_5, 11, 3)]):
    print("ok")
else:
    print("not ok")

weights_1 = create_weights(reel_1, 3000, 11, 0, 3, 1)
weights_2 = create_weights(reel_2, 3000, 11, 250, 3, 2)
weights_3 = create_weights(reel_3, 3000, 11, 396, 3, 3)
weights_4 = create_weights(reel_4, 3000, 11, 359, 3, 4)
weights_5 = create_weights(reel_5, 3000, 11, 0, 3, 5)

reel_weight_list = [[reel_1, weights_1],
                   [reel_2, weights_2],
                   [reel_3, weights_3],
                   [reel_4, weights_4],
                   [reel_5, weights_5]]
reelset_dict = {}
reelset_dict[1] = reel_weight_list
create_xml_realsets(reelset_dict, "PoL_Wild_Reelset.txt")





"""
np.random.seed(42)
symb_stack_1 = {}
symb_stack_1[0] = [[2, 3], [3, 1]]
symb_stack_1[1] = [[2, 5], [3, 2]]
symb_stack_1[2] = [[2, 7], [3, 3]]
symb_stack_1[3] = [[2, 9], [3, 4]]
symb_stack_1[4] = [[2, 11], [3, 5]]
reel_1 = create_and_check_reel([0,1,2,3,4,5,6,7,8,9], [10,10,10,10,10,10,10,10,10,10], 11, 12, 4,)
np.random.seed(43)
reel_2 = create_and_check_reel([0,1,2,3,4,5,6,7,8], [12,12,12,12,36,36,36,3,3], 11, 12, 4)
np.random.seed(44)
reel_3 = create_and_check_reel([0,1,2,3,4,5,6,7,8], [12,12,12,12,36,36,36,3,3], 11, 8, 4)
np.random.seed(45)
reel_4 = create_and_check_reel([0,1,2,3,4,5,6,7,8], [22,12,22,12,3,36,36,3,3], 11, 4, 4)
np.random.seed(46)
reel_5 = create_and_check_reel([0,1,2,3,4,5,6,7,8], [12,22,12,22,3,3,3,33,33], 11, 4, 4)


weights_1 = create_weights(reel_1, 1200, 11, 3,1)
weights_2 = create_weights(reel_2, 1200, 11, 3,2)
weights_3 = create_weights(reel_3, 900, 11, 3,3)
weights_4 = create_weights(reel_4, 500, 11, 3,4)
weights_5 = create_weights(reel_5, 500, 11, 3,5)

reel_weight_list = [[reel_1, weights_1],
                   [reel_2, weights_2],
                   [reel_3, weights_3],
                   [reel_4, weights_4],
                   [reel_5, weights_5]]
reelset_dict = {}
reelset_dict[1] = reel_weight_list
create_xml_realsets(reelset_dict, "Sticky_Wilds_1_2_3.txt")
"""


