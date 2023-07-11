def open_tests(filename):
    with open(filename, "r") as file:
        text = file.read().split("\n")
        while "" in text:
            text.remove("")
        return text
           

def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])


def choose_nums(numbers):
    len_nums = len(numbers) // 2 + len(numbers) %   2
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


def winner(sum1: int, sum2: int) -> str:
    if sum1 % 3 == 0:
        if sum2 % 3 == 0:
            return "DRAW"
        return "FIRST"
    if sum2 % 3 == 0:
        return "SECOND"
    return "DRAW"


if __name__ == "__main__":
    print("Tests:")
    testlist = open_tests("tests.txt")
    for i in range(0, len(testlist), 2):
        count_cards = int(testlist[i])
        values = list(map(int, testlist[i+1].split()))
        sum1 = sum(choose_nums(values))
        sum2 = sum(values) - sum1
        print(count_cards, values, winner(sum1, sum2), sep="\n", end="\n")
