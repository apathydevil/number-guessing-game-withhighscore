import csv
import random
import os

def load_scores():
    if os.path.exists("scores.csv"):
        with open("scores.csv", "r") as f:
            reader = csv.DictReader(f)
            return [row for row in reader]
    return []

def save_score(score):
    existing = load_scores()
    with open("scores.csv", "a" if existing else "w", newline="") as f:
        writer = csv.writer(f)
        if not existing:
            writer.writerow(["name", "difficulty", "guesses"])
        writer.writerow(score)

def game(difficulty):
    
    match difficulty:
        case 1:
            max_num = 50
        case 2:
            max_num = 100
        case 3:
            max_num = 200
        case _:
            print("Unknown difficulty! Defaulting to 1 - 50")
            max_num = 50
    
    number_to_guess = random.randint(1,max_num)
    attempts = 0
    print(f"Guess a number between 1 and {max_num}!")
    print("\n")
    while True:
        guess = int(input("Please type out your guess: "))
        attempts += 1
        if guess == number_to_guess:
            print("Congratulations! You win!")
            return attempts
        else: 
            print("Sadly that was wrong!")
            if guess < number_to_guess:
                print("The number you are looking for is larger!")
            else:
                print("The number you are looking for is smaller!")
            print(f"Your current attempts: {attempts}")
            print()
        


def main():
    print("Welcome to my simple number guessing game with a highscore leaderboard!")
    print("Your goal is to try and guess my secret number!")
    while True:
        print("Would you like to start, see highscores, clear all highscores or quit? start/highscores/clear/quit: ")
        choice = input().strip().lower()
        match choice:
            case "start":
                print("Please choose a difficulty setting: ")
                print("1. 1 - 50")
                print("2. 1 - 100")
                print("3. 1 - 200")
                difficulty = int(input())
                attempts = game(difficulty)
                print("Would you like to save your score?")
                question = input("yes/no? ").strip().lower()
                if question == "yes":
                    score = [input("Please enter your name: "), difficulty, attempts]
                    save_score(score)
                else:
                    print("Your score will not be remembered!")
                    print()
            case "highscores":
                scores = load_scores()
                difficulty_names = {"1": "Easy", "2": "Medium", "3": "Hard"}
                sorted_scores = sorted(scores, key=lambda x: (int(x["difficulty"]), int(x["guesses"])))
                for score in sorted_scores:
                    print(f"Name: {score['name']}, Difficulty: {difficulty_names[score['difficulty']]}, Guesses: {score['guesses']}")
            case "clear":
                if os.path.exists("scores.csv"):
                    os.remove("scores.csv")
                    print("All highscores cleared!")
                else:
                    print("No highscores to clear!")
                print()
            case "quit":
                print("Thank you for playing!")
                break
            case _:
                print("Unknown command!")


if __name__ == "__main__":
    main()