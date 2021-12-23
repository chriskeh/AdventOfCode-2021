#!/usr/bin/env /usr/bin/python36

input_data_file = "part1.data"


def slurp_input(input_file):
    """
    Read the input file.
    :param input_file:
    :return: A list of sets. Each set represents the given answers in a group.
    """
    f = open(input_file, "r")
    lines = f.readlines()
    for line in lines:
        links, foo, rechts = line.split()
        start_x, start_y = links.split(',')
        ziel_x, ziel_y = rechts.split(',')
        if start_x != ziel_x and start_y != ziel_y:
            next()




    print("Zeile: {}".format(line))
    print("Links: {}".format(links))
    print("Rechts: {}".format(rechts))





    return "123"


def main():

    # uncomment the next line to read the input data from the test file
    # input_data_file = "part1_test.data"

    max_x = 0
    max_y = 0
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
        if start_x > max_x:
            max_x = start_x
        if ziel_x > max_x:
            max_x = ziel_x
        if start_y > max_y:
            max_y = start_y
        if ziel_y > max_y:
            max_y = ziel_y

    # print(max_x, max_y)
    matrix = []
    for i in range(max_x + 1):
        spalte = [0] * (max_y + 1)
        matrix.append(spalte)

    for line in lines:
        links, foo, rechts = line.split()
        start_x_c, start_y_c = links.split(',')
        start_x = int(start_x_c)
        start_y = int(start_y_c)
        ziel_x, ziel_y = rechts.split(',')
        ziel_x = int(ziel_x)
        ziel_y = int(ziel_y)
        if start_x == ziel_x:
            # print("X ist gleich")
            # print(start_y, ziel_y)
            if start_y > ziel_y:
                start_y, ziel_y = ziel_y, start_y
            for i in range(start_y, ziel_y + 1):
                matrix[start_x][i] += 1
        elif start_y == ziel_y:
            # print("Y ist gleich")
            # print(start_x, ziel_x)
            if start_x > ziel_x:
                start_x, ziel_x = ziel_x, start_x
            for i in range(start_x, ziel_x + 1):
                matrix[i][start_y] += 1
        else:
            continue

        # print("Matrix:")
        # print(matrix)

    total = 0
    for spalte in matrix:
        # print(spalte)
        for x in spalte:
            if x > 1:
                total += 1

    print("Total: {}".format(total))

    # print("Zeile: {}".format(line))
    # print("Links: {}".format(links))
    # print("Rechts: {}".format(rechts))

    # print("Total: {}".format(total))


if __name__ == "__main__":
    main()
