import random

class NumberGuessingGame:
    def __init__(self, min_number, max_number):
        self.min_number = min_number
        self.max_number = max_number
        self.target_number = random.randint(min_number, max_number)
        self.guesses = 0

    def play(self):
        print(f"Guess the number between {self.min_number} and {self.max_number}.")

        while True:
            try:
                guess = int(input("Enter your guess: "))
                self.guesses += 1

                if guess < self.min_number or guess > self.max_number:
                    print(f"Please guess a number between {self.min_number} and {self.max_number}.")
                elif guess < self.target_number:
                    print("Too low! Try again.")
                elif guess > self.target_number:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You guessed the number {self.target_number} in {self.guesses} guesses.")
                    break
            except ValueError:
                print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    game = NumberGuessingGame(1, 100)
    game.play()
