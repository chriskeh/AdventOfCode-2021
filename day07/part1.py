#!/usr/bin/env /usr/bin/python36

import sys

input_data_file = "part1.data"

def slurp_input(input_file):
    """
    Read the input file. It contains one line with numbers separated by comma.
    Reading it in with the readline method creates a list of strings, not numbers.
    So a second command is necessary, which applies the function 'int' to the iterable 'my_list' which
    converts each element of the iterable into an int and then create a list from that again.  Et voila!
    :param input_file:
    :return: list of integers
    """
    f = open(input_file, "r")
    zeile = f.readline()

    my_list = zeile.split(',')

    my_list = list(map(int, my_list))
    my_list.sort()

    return my_list


def calculate_median(list_of_ints):
    """
    Calculate the median for a given list of integers.

    LIMITATION:
    :param input_data: list with integers
    :return: the meridian
    """

    # There are different methods for calculating the meridian for even and uneven numbers. As we have an even number
    # as input, we exit if we get an uneven number of input data.
    if (len(list_of_ints) % 2):
        print("Uneven number of input integers.  Not yet implemented. Exit.")
        sys.exit(1)

    half = len(list_of_ints) / 2
    half = int(half)

    summe = sum(list_of_ints)
    median = ( list_of_ints[half - 1] + list_of_ints[half] ) / 2
    #
    # print("Summe: {}".format(summe))
    # print("Median: {}".format(median))

    return int(median)


def calculate_fuel(median, input_data):
    """
        Calculate the Absoluter Mittelwert.
        :param median:
        :param input_data:
        :return: Mittelwert
        """
    fuel = 0
    for squid in input_data:
        fuel += abs(squid - median)
    return fuel


def main():

    # uncomment the next line to read the input data from the test file
    # input_data_file = "part1_test.data"
    input_data = slurp_input(input_data_file)
    # print(input_data)


    median = calculate_median(input_data)
    # print("Median: {}".format(median))

    fuel = calculate_fuel(median, input_data)

    print("Fuel: {}".format(fuel))

if __name__ == "__main__":
    main()






