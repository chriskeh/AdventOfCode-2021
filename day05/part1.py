#!/usr/bin/env /usr/bin/python36

input_data_file = "part1.data"


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

    total = 0
    for spalte in matrix:
        for x in spalte:
            if x > 1:
                total += 1

    print("Total: {}".format(total))

if __name__ == "__main__":
    main()
