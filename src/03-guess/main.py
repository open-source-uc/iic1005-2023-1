import random


class Guesser:
    def __init__(self, name: str):
        self.name = name
        self.number = None
        self.guesses = 0
        self.guesses_number = 0

    def start_game(self, lower_bound: int = 0, upper_bound: int = 50):
        self.number = random.randint(lower_bound, upper_bound)
        self.guesses = 0

    def guess(self, number: int):
        if self.number is None:
            raise Exception("Game not started")

        self.guesses += 1

        if number < self.number:
            print(f"Too low, {self.name}")
        elif number > self.number:
            print("Too high, {self.name}")

    def is_correct(self):
        return self.guesses_number == self.number

    def display_win_message(self):
        print(f"You win {self.name}! It took you {self.guesses} guesses")

    def quit(self):
        print(f"Bye {self.name}!")


guesser = Guesser(input("Name: "))
cmd = int(input("0:Start, 1:Guess, 2:Exit "))

while cmd != 2:
    if cmd == 0:
        guesser.start_game()
        print("Game started")
    elif cmd == 1:
        guesser.guess(int(input("Guess a number: ")))
        if guesser.is_correct:
            guesser.display_win_message()

    cmd = input("0:Start, 1:Guess, 2:Exit ")

guesser.quit()
