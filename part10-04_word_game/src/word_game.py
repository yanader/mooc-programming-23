# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):

    def __init__(self, rounds:int):
        super().__init__(rounds)
    
    def round_winner(self, p1_word:str, p2_word:str):
        if len(p1_word) > len(p2_word):
            return 1
        elif len(p1_word) < len(p2_word):
            return 2

class MostVowels(WordGame):

    def __init__(self, rounds:int):
        super().__init__(rounds)
    
    def round_winner(self, p1_word: str, p2_word: str):
        p1_score = 0
        p2_score = 0
        for c in p1_word:
            if c in 'aeiouAEIOU':
                p1_score += 1
        for c in p2_word:
            if c in 'aeiouAEIOU':
                p2_score += 1
        if p1_score > p2_score:
            return 1
        elif p1_score < p2_score:
            return 2

class RockPaperScissors(WordGame):

    def __init__(self, rounds:int):
        super().__init__(rounds)
    
    def round_winner(self, p1_word: str, p2_word: str):
        legal_values = ['rock','paper','scissors']
        p1_legal = p1_word in legal_values
        p2_legal = p2_word in legal_values
        if not p1_legal and not p2_legal:
            return
        if not p1_legal:
            return 2
        elif not p2_legal:
            return 1
        
        if p1_word == p2_word:
            return
        
        if p1_word == 'rock':
            if p2_word == 'paper':
                return 2
            elif p2_word == 'scissors':
                return 1
        
        if p1_word == 'paper':
            if p2_word == 'scissors':
                return 2
            elif p2_word == 'rock':
                return 1

        if p1_word == 'scissors':
            if p2_word == 'rock':
                return 2
            elif p2_word == 'paper':
                return 1
        
