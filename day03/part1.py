#!/usr/bin/env /usr/bin/python36

input_data_file = "part1.data"


def slurp_input(input_file):
    """
    Read the input file.
    :param input_file:
    :return: A list of sets. Each set represents the given answers in a group.
    """
    temp = open(input_file,'r').read().splitlines()
    return temp


def main():

    # uncomment the next line to read the input data from the test file
    # input_data_file = "part1_test.data"

    all_input = slurp_input(input_data_file)

    laenge = len(all_input[0])

    zeros = []
    ones = []
    most = []
    least = []
    for index in range(0, laenge):
        zeros.append(0)
        ones.append(0)
        most.append(0)
        least.append(0)

    # print(all_input)

    for zeile in all_input:
        index = 0
        zeros.append(0)
        ones.append(0)
        for buchstabe in zeile:
            if buchstabe == "0":
                zeros[index] += 1
            elif buchstabe == "1":
                ones[index] += 1
            else:
                print("Error: {}".format(zeile))
            index += 1

    for index in range(0, len(zeile)):
        if ones[index] > zeros[index]:
            most[index] = "1"
            least[index] = "0"
        elif zeros[index] > ones[index]:
            most[index] = "0"
            least[index] = "1"
        else:
            print("Error: ones and zeros are identical ({}) in column {}".format(zeros[index], index))

    # print("Most: {}".format(most))
    # print("Least: {}".format(least))
    most_string = ''.join(most)
    most_decimal = int(most_string, 2)
    # print("most: {}".format(int(most_string, 2)))
    least_string = ''.join(least)
    least_decimal = int(least_string, 2)

    total = most_decimal * least_decimal
    # print("least: {}".format(int(least_string, 2)))

    print("Total: {}".format(total))


if __name__ == "__main__":
    main()
