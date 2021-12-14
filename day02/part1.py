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

    input_list = slurp_input(input_data_file)

    # print(input_list)

    h_position = 0
    depth = 0
    
    for order in input_list:
        direction, amount = order.split(" ")
        # print("D: {}, A: {}".format(direction, amount))
        if direction == "forward":
            h_position += int(amount)
        elif direction == "down":
            depth += int(amount)
        elif direction == "up":
            depth -= int(amount)
        else:
            print("Error: {}".format(order))
    total = h_position * depth
 
    print("Horizontal position: {}, Depth: {}".format(h_position, depth))
    print("Total: {}".format(total))

    h_position = 0
    depth = 0
    aim = 0
    
    for order in input_list:
        direction, amount_string = order.split(" ")
        amount = int(amount_string)
        # print("D: {}, A: {}".format(direction, amount))
        if direction == "forward":
            h_position += amount
            if aim != 0:
                depth += (aim * amount)
        elif direction == "down":
            aim += amount
        elif direction == "up":
            aim -= amount
        else:
            print("Error: {}".format(order))
    total = h_position * depth
 
    print("Horizontal position: {}, Depth: {}".format(h_position, depth))
    print("Total: {}".format(total))

if __name__ == "__main__":
    main()
