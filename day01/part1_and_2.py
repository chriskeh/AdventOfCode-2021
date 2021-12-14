#!/usr/bin/env /usr/bin/python36

input_data_file = "part1.data"


def slurp_input(input_file):
    """
    Read the input file. It contains one number per line.
    Reading it in the with-statement creates a list of strings, not numbers.
    So a second command is necessary, which applies the function 'int' to the iterable 'my_list' which
    converts each element of the iterable into an int and then create a list from that again.  Et voila!
    :param input_file:
    :return: list of integers
    """
    with open(input_file) as f:
        my_list = list(f)
    my_list = list(map(int, my_list))
    return my_list


def main():

    # uncomment the next line to read the input data from the test file
    # input_data_file = "part1_test.data"

    numbers = slurp_input(input_data_file)

    count = 0
    for index in range(1, len(numbers)):
        if numbers[index] > numbers[index - 1]:
            count += 1

    print("Part1: {}".format(count))

    count = 0
    prev = numbers[0] + numbers[1] + numbers[2]
    for index in range(3, len(numbers)):
        current = numbers[index - 2] + numbers[index - 1] + numbers[index]
        if current > prev:
            count += 1
        prev = current
      
    print("Part2: {}".format(count))


if __name__ == "__main__":
    main()
