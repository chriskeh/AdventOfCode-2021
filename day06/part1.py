#!/usr/bin/env /usr/bin/python36
import sys

def single_fish(fish):
    if fish == 0:
        return 6
    if fish > 8:
        print(("Oops, this should never happen"))
        sys.exit(1)
    return fish - 1


def calc_fishes(fishes):
    new_fishes = []
    new = 0
    for number in fishes:
        result = single_fish(number)
        if number == 0:
            new += 1
        # print(new)
        new_fishes.append(result)
    if new > 0:
        new_fishes.extend(new * [8])

    return new_fishes


def main():

    fishes = [1,4,2,4,5,3,5,2,2,5,2,1,2,4,5,2,3,5,4,3,3,1,2,3,2,1,4,4,2,1,1,4,1,4,4,4,1,4,2,4,3,3,3,3,1,1,5,4,2,5,2,4,2,2,3,1,2,5,2,4,1,5,3,5,1,4,5,3,1,4,5,2,4,5,3,1,2,5,1,2,2,1,5,5,1,1,1,4,2,5,4,3,3,1,3,4,1,1,2,2,2,5,4,4,3,2,1,1,1,1,2,5,1,3,2,1,4,4,2,1,4,5,2,5,5,3,3,1,3,2,2,3,4,1,3,1,5,4,2,5,2,4,1,5,1,4,5,1,2,4,4,1,4,1,4,4,2,2,5,4,1,3,1,3,3,1,5,1,5,5,5,1,3,1,2,1,4,5,4,4,1,3,3,1,4,1,2,1,3,2,1,5,5,3,3,1,3,5,1,5,3,5,3,1,1,1,1,4,4,3,5,5,1,1,2,2,5,5,3,2,5,2,3,4,4,1,1,2,2,4,3,5,5,1,1,5,4,3,1,3,1,2,4,4,4,4,1,4,3,4,1,3,5,5,5,1,3,5,4,3,1,3,5,4,4,3,4,2,1,1,3,1,1,2,4,1,4,1,1,1,5,5,1,3,4,1,1,5,4,4,2,2,1,3,4,4,2,2,2,3]
    # fishes = [3,4,3,1,2]

    for i in range(0,80):
        fishes = calc_fishes(fishes)

    print("Total: {}".format(len(fishes)))


if __name__ == "__main__":
    main()
