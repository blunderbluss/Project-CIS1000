import random

class DiceRoll:
    def __init__(self):
        self.scores = []

    def play(self):
        input("Press Enter to roll the dice...")
        roll = random.randint(1, 6)
        print(f"You rolled a {roll}!")
        self.scores.append(roll)

    def show_scores(self):
        print("\nScores for Dice Roll:")
        if self.scores:
            print(f"Total rolls: {len(self.scores)}")
            print(f"Maximum roll: {max(self.scores)}")
            print(f"Minimum roll: {min(self.scores)}")
            print(f"Average roll: {sum(self.scores) / len(self.scores):.2f}")
        else:
            print("No rolls yet.")

if __name__ == "__main__":
    game = DiceRoll()
    while True:
        game.play()
        choice = input("Roll again? (y/n): ")
        if choice.lower() != 'y':
            game.show_scores()
            break
