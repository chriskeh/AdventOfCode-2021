#!/usr/bin/env /usr/bin/python36
import sys

import numpy as np

input_data_file = "part1.data"


def slurp_input(input_file):
    """
    Read the line from the file and create an numpy array from them.
    Return that array.
    :param input_file:
    :return:
    """
    max_x = 0
    max_y = 0
    f = open(input_file, "r")
    lines = f.readlines()
    for line in lines:
        # read each line, split it into the four values that are the coordinates of the two points.
        # Now we know the max in each direction. Create a square array filled with zeros.
        links, foo, rechts = line.split()

        start_x, start_y = links.split(',')
        max_x = max(max_x, int(start_x))
        max_y = max(max_y, int(start_y))

        ziel_x, ziel_y = rechts.split(',')
        max_x = max(max_x, int(ziel_x))
        max_y = max(max_y, int(ziel_y))

    groesse = max(max_x, max_y) + 1
    return np.zeros((groesse, groesse), dtype=np.int)


def main():
    # uncomment the next line to read the input data from the test file
    # input_data_file = "part1_test.data"

    matrix = slurp_input(input_file=input_data_file)

    f = open(input_data_file, "r")
    lines = f.readlines()
    for line in lines:
        links, foo, rechts = line.split()
        start_x_c, start_y_c = links.split(',')
        start_x = int(start_x_c)
        start_y = int(start_y_c)
        ziel_x, ziel_y = rechts.split(',')
        ziel_x = int(ziel_x)
        ziel_y = int(ziel_y)
        if start_x == ziel_x:
            if start_y > ziel_y:
                start_y, ziel_y = ziel_y, start_y
            for i in range(start_y, ziel_y + 1):
                matrix[start_x][i] += 1
        elif start_y == ziel_y:
            if start_x > ziel_x:
                start_x, ziel_x = ziel_x, start_x
            for i in range(start_x, ziel_x + 1):
                matrix[i][start_y] += 1
        else:
            continue

    print("Total: {}".format(len(matrix[matrix > 1])))


if __name__ == "__main__":
    main()
