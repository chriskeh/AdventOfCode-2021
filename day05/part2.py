#!/usr/bin/env /usr/bin/python36

input_data_file = "part1.data"


def main():
    # uncomment the next line to read the input data from the test file
    # input_data_file = "part1_test.data"

    max_x = 0
    max_y = 0
    f = open(input_data_file, "r")
    lines = f.readlines()

    # erstmal die maximalen Werte bestimmen
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
    # Kann sein, dass ein Wert nicht das Max erreicht
    if max_x > max_y:
        max_y = max_x
    if max_y > max_x:
        max_x = max_y

    # Matrix mit 0 vorbelegen
    matrix = []
    for i in range(max_x + 1):
        spalte = [0] * (max_y + 1)
        matrix.append(spalte)

    # Und los geht's
    for line in lines:
        links, foo, rechts = line.split()
        start_x_c, start_y_c = links.split(',')
        start_x = int(start_x_c)
        start_y = int(start_y_c)
        ziel_x, ziel_y = rechts.split(',')
        ziel_x = int(ziel_x)
        ziel_y = int(ziel_y)

        if start_x == ziel_x:
            # print("Vertikal, X ist gleich")
            if start_y > ziel_y:
                start_y, ziel_y = ziel_y, start_y
            for i in range(start_y, ziel_y + 1):
                matrix[i][start_x] += 1
        elif start_y == ziel_y:
            # print("Horizontal, Y ist gleich")
            if start_x > ziel_x:
                start_x, ziel_x = ziel_x, start_x
            # print(start_x, ",", start_y, "->", ziel_x, ",", ziel_y)
            for i in range(start_x, ziel_x + 1):
                matrix[start_y][i] += 1
        elif (start_x - start_y == ziel_x - ziel_y ):
            # 0,0 -> 8,8
            # 1,3 -> 4,6
            # print("diagonal, links-oben nach echts-unten")
            if start_x > ziel_x:
                start_x, ziel_x = ziel_x, start_x
            if start_y > ziel_y:
                start_y, ziel_y = ziel_y, start_y
            # print(start_x, ",", start_y, "->", ziel_x, ",", ziel_y)
            y_value = start_y
            for x_value in range(start_x, ziel_x + 1):
                # print(x_value, y_value)
                matrix[y_value][x_value] += 1
                y_value += 1
        elif (abs(start_x - ziel_y) == abs(start_y - ziel_x)):
            # 0,4 -> 4,0
            # 1,5 ->
            # 5,5 -> 8,2
            # print("reverse")
            if start_x > ziel_x:
                start_x, ziel_x = ziel_x, start_x
                start_y, ziel_y = ziel_y, start_y
            # print(start_x, ",", start_y, "->", ziel_x, ",", ziel_y)
            y_value = start_y
            for x_value in range(start_x, ziel_x + 1):
                matrix[y_value][x_value] += 1
                y_value -= 1
        else:
            continue
        # for spalte in matrix:
        #     print(spalte)

    total = 0
    for spalte in matrix:
        for x in spalte:
            if x > 1:
                total += 1
    print("Total: {}".format(total))

if __name__ == "__main__":
    main()
