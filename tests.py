from math import ceil, factorial
from itertools import combinations


def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])


def choose_nums(numbers):
    nums = []
    len_nums = ceil(len(numbers) / 2)

    all_permutations = combinations(numbers, len_nums)
    for lst in all_permutations:
        if listsum(lst) % 3 == 0:
            break


if __name__ == "__main__":
    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    print(len(nums))
    print(choose_nums(nums))
