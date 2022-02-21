


def create_xml_realsets(reelset_reels_dict: dict, file_name="reelset_xml.txt"):
    """
    This function create .txt file with reelsets in xml formating.

    reelset_reels_dict: [key] : [[[reel], [weights]], [[reel], [weights]], ...]

    Input variables:

    reelset_reels_dict - dict, in which keys is weight of reelset and values
    is 2d array: first dimension is numbere of reel, second dimension is reel.

    file_name - way to file and its name.

    """
    reels_file = open(file_name, 'w')
    reels_file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
    reels_file.write("<settings id=\"AVV056335,93\">\n")
    reels_file.write("\t<ReelSets>")
    weight_sum = 0
    reel_counter = 1

    for reelset_prob, reels in reelset_reels_dict.items():
        reels_file.write(
            f"\n\t\t<Reelset reelName=\"{reel_counter}\" betsIndices=\"0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23\" range=\"{weight_sum} {weight_sum + int(reelset_prob * 100000) - 1}\" isFortuneBet=\"false\" isMainCycle=\"true\" isStartScreen=\"true\">")
        reel_counter += 1
        weight_sum += int(reelset_prob * 100000) - 1
        reels_file.write("\n\t\t\t")

        for reel_weight in reels:
            i = 1
            reels_file.write("<Reel>")
            reels_file.write("\n\t\t\t\t")
            reels_file.write("<Symbols>")
            l = len(reel_weight[0])
            for num in reel_weight[0]:
                if i < l:
                    reels_file.write(f"{int(num)},")
                    i += 1
                else:
                    reels_file.write(f"{int(num)}")
            reels_file.write("</Symbols>\n\t\t\t\t")

            reels_file.write("<Weights>")
            for j in range(l):
                if j != (l - 1):
                    reels_file.write(f"{reel_weight[1][j]},")
                else:
                    reels_file.write(f"{reel_weight[1][j]}")
            reels_file.write("</Weights>\n\t\t\t")
            reels_file.write("</Reel>\n\t\t\t")

        reels_file.write("\n\t\t</Reelset>")
    reels_file.write("\n\t</ReelSets>\n")
    reels_file.write("</settings>")
    reels_file.close()


def read_input(txt_path="set.txt"):
    file = open(txt_path, 'r')
    lines = file.readlines()

    for i in range(len(lines)):
        if lines[i][0] == "#":
            del lines[i]
    print(lines)


