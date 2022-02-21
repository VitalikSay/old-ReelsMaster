import numpy as np
from collections import defaultdict

# ШАГ 1: СОЗДАЕМ РИЛ И ШАФЛИМ ЕГО (ЭТА ФУНКЦИЯ ОТДЕЛЬНО НЕ ИСПОЛЬЗУЕТСЯ, ОНА ВХОДИТ В СОСТАВ ШАГА 2)

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


#def insert_special_symbols(stack_reel, sp_symbols, min_dist_between_sp_symbols):


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


def PrintSymbolWeight(reels, weights):
    for j in range(len(reels)):
        print('Reel: ', j+1)
        reel = reels[j]
        weight = weights[j]
        if len(reel) != len(weight):
            print("len(reel) != len(weights)")
            return 0
        counter = defaultdict(int)
        for i in range(len(reel)):
            counter[reel[i]] += weight[i]

        all_weight = 0
        for symbol in counter.keys():
            all_weight += counter[symbol]

        for symbol in sorted(counter.keys()):
            print(symbol, " : ", counter[symbol], ' (prob :', "%.3f" % (counter[symbol] * 100 / all_weight), ' % )')
        print()
    return 0

