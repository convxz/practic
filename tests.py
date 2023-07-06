from math import ceil, factorial
from itertools import combinations


def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])


def choose_nums(numbers):
    len_nums = ceil(len(numbers) / 2)
    nums = numbers[:len_nums]
    other_nums = numbers[len_nums:]

    if listsum(nums) % 3 == 0:
        return nums
    remainder = listsum(nums) % 3
    for i in range(len_nums):
        for el in other_nums:
            if el == nums[i] + (3 - remainder) or el == nums[i] - remainder: 
                nums[i] = el
                if listsum(nums) % 3 == 0:
                    return nums
                nums = numbers[:len_nums]
    return nums


if __name__ == "__main__":
    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # nums = [-5, -5, -5]
    print(choose_nums(nums))
