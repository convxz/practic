from itertools import permutations
from math import ceil
from pprint import pprint


def open_tests(filename):
    with open(filename, "r") as file:
        text = file.read().split("\n")
        while "" in text:
            text.remove("")
        return text
                

class Game:

    def __init__(self, count_cards, values) -> None:
        self.count_cards = count_cards
        self.values = values
        self._game_process(count_cards, values)
    
    def _game_process(self, count_cards, values):
        permutations_list = permutations(values) # все возможные исходы игр
        print(len(list(permutations_list)))
        for lst in permutations_list:
            sum1 = sum([lst[i] for i in range(0, count_cards, 2)]) 
            sum2 = sum([lst[i] for i in range(1, count_cards, 2)])
            print(sum1)
            print(sum2)
            if sum1 % 3 == 0:
                break
        self.sum1, self.sum2 = sum1, sum2
        
    def return_winner(self):
        sum1, sum2 = self.sum1, self.sum2
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
    for i in range(0, len(testlist)+1, 2):
        count_cards = int(testlist[i])
        values = list(map(int, testlist[i+1].split()))
        temp = Game(count_cards, values)
        print(count_cards, values, temp.return_winner(), sep="\n", end="\n")
