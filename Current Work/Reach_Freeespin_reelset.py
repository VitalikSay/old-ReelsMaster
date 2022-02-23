from Libs.Make_Reel import *
from Libs.IO_data import create_xml_realsets


# [5, 3, 1,
#                                7, 4, 2,
#                                9, 5, 3,
#                                16, 8, 4,
#                                16, 8, 4]

first_reel_stacks = [[0], [0, 0], [0, 0, 0],
                     [1], [1, 1], [1, 1, 1],
                     [2], [2, 2], [2, 2, 2],
                     [3], [3, 3], [3, 3, 3],
                     [4], [4, 4], [4, 4, 4]]
first_reel_number_of_stacks = [7, 4, 1,
                               9, 6, 1,
                               10, 8, 2,
                               14, 9, 3,
                               14, 9, 3]
second_reel_stacks = [[0], [0, 0], [0, 0, 0],
                      [1], [1, 1], [1, 1, 1],
                      [2], [2, 2], [2, 2, 2],
                      [3], [3, 3], [3, 3, 3],
                      [4], [4, 4], [4, 4, 4]]
second_reel_number_of_stacks = [7, 4, 1,
                               9, 6, 1,
                               10, 8, 2,
                               14, 9, 3,
                               14, 9, 3]
third_reel_stacks = [[0], [0, 0], [0, 0, 0],
                     [1], [1, 1], [1, 1, 1],
                     [2], [2, 2], [2, 2, 2],
                     [3], [3, 3], [3, 3, 3],
                     [4], [4, 4], [4, 4, 4]]

third_reel_number_of_stacks = [7, 4, 1,
                               9, 6, 1,
                               10, 8, 2,
                               14, 9, 3,
                               14, 9, 3]
fourth_reel_stacks = [[0], [0, 0], [0, 0, 0],
                      [1], [1, 1], [1, 1, 1],
                      [2], [2, 2], [2, 2, 2],
                      [3], [3, 3], [3, 3, 3],
                      [4], [4, 4], [4, 4, 4]]
fourth_reel_number_of_stacks = [7, 4, 1,
                               9, 6, 1,
                               10, 8, 2,
                               14, 9, 3,
                               14, 9, 3]
fifth_reel_stacks = [[0], [0, 0], [0, 0, 0],
                     [1], [1, 1], [1, 1, 1],
                     [2], [2, 2], [2, 2, 2],
                     [3], [3, 3], [3, 3, 3],
                     [4], [4, 4], [4, 4, 4]]
fifth_reel_number_of_stacks = [7, 4, 1,
                               9, 6, 1,
                               10, 8, 2,
                               14, 9, 3,
                               14, 9, 3]


def create_weights(reel, weight_to_input, wild_symbol, wild_weight, window_height, reel_number):
    r_copy = reel[:]
    r_copy.extend(r_copy[:window_height])
    weight = [1 for _ in range(len(reel))]
    #return weight

    # ВЕСА НА ВАЙЛДЫ
    # while(wild_weight != 0):
    #     for i in range(len(reel)):
    #         window = r_copy[i: i+window_height]
    #         if wild_symbol in window:
    #             weight[i] += 1
    #             wild_weight -= 1
    #             if (wild_weight == 0):
    #                 break
    #
    while(weight_to_input > 0):
        for i in range(len(reel)):
            window = r_copy[i: i+window_height]
            if wild_symbol in window:
                continue

            reach_pic_counter = 0
            cheap_pic_counter = 0
            for symb in window:
                if symb in [0, 1, 2]:
                    reach_pic_counter += 1
                elif symb in [3, 4]:
                    cheap_pic_counter += 1

            pic_counter = reach_pic_counter + cheap_pic_counter


            if (reel_number == 1):
                if reach_pic_counter == 3:
                    weight[i] += 1
                    weight_to_input -= 1
                if weight_to_input <= 0:
                    break


            if (reel_number == 2):
                if reach_pic_counter == 3:
                    weight[i] += 4
                    weight_to_input -= 4

                if weight_to_input <= 0:
                    break


            if (reel_number == 3):
                if cheap_pic_counter == 3:
                    weight[i] += 5
                    weight_to_input -= 5

                if weight_to_input <= 0:
                    break


            if (reel_number == 4):
                if reach_pic_counter == 3:
                    weight[i] += 5
                    weight_to_input -= 5

                if weight_to_input <= 0:
                    break


            if (reel_number == 5):
                if cheap_pic_counter == 1:
                    weight[i] += 4
                    weight_to_input -= 4

                if weight_to_input <= 0:
                    break

    return weight




np.random.seed(42)
reel_1 = reel_processing(first_reel_stacks, first_reel_number_of_stacks)
np.random.seed(43)
reel_2 = reel_processing(second_reel_stacks, second_reel_number_of_stacks)
np.random.seed(48)
reel_3 = reel_processing(third_reel_stacks, third_reel_number_of_stacks)
np.random.seed(42)
reel_4 = reel_processing(fourth_reel_stacks, fourth_reel_number_of_stacks)
np.random.seed(47)
reel_5 = reel_processing(fifth_reel_stacks, fifth_reel_number_of_stacks)


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
"""
weights_1 = create_weights(reel_1, 3000, 11, 0, 3, 1)
weights_2 = create_weights(reel_2, 3000, 11, 445, 3, 2)
weights_3 = create_weights(reel_3, 3000, 11, 773, 3, 3)
weights_4 = create_weights(reel_4, 3000, 11, 669, 3, 4)
weights_5 = create_weights(reel_5, 3000, 11, 0, 3, 5)
"""
weights_1 = create_weights(reel_1, 3000, 11, 0, 3, 1)
weights_2 = create_weights(reel_2, 1000, 11, 0, 3, 2)
weights_3 = create_weights(reel_3, 2000, 11, 0, 3, 3)
weights_4 = create_weights(reel_4, 7000, 11, 0, 3, 4)
weights_5 = create_weights(reel_5, 2000, 11, 0, 3, 5)

PrintSymbolWeight([reel_1, reel_2, reel_3, reel_4, reel_5],
                  [weights_1, weights_2, weights_3, weights_4, weights_5])



reel_weight_list = [[reel_1, weights_1],
                   [reel_2, weights_2],
                   [reel_3, weights_3],
                   [reel_4, weights_4],
                   [reel_5, weights_5]]
reelset_dict = {}
reelset_dict[1] = reel_weight_list
create_xml_realsets(reelset_dict, "PoL_Freespin_Win.txt")