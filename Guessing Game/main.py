from random import randint

def Game():
    has_won = False
    num_of_guesses = 0
    times_guessed = 0
    max_num = 100
    min_num = 1
    random_number = randint(min_num, max_num)

    print("Welcome to the guessing game!")
    print(f"I'm thinking of a number between {min_num} and {max_num}.")
    print("Start by selecting the difficulty:\n1. Easy (10 guesses)\n2. Medium (5 guesses)\n3. Hard (3 guesses)\n")

    while True:
        difficulty = input("Enter your selection (1, 2, or 3): ")
        if difficulty in ("1","2","3"):
            break
        else:
            print("Please select 1, 2, or 3.")

    if difficulty == "1":
        print("You have selected easy difficulty.")
        num_of_guesses = 10
    if difficulty == "2":
        print("You have selected medium difficulty.")
        num_of_guesses = 5
    if difficulty == "3":
        print("You have selected hard difficulty.")
        num_of_guesses = 3

    print()

    while num_of_guesses:
        print(f"You have {num_of_guesses} guesses remaining.\n")

        while True:
            try:
                guess = int(input(f"Enter a guess between {min_num} and {max_num}: "))
                if guess < min_num or guess > max_num:
                    print(f"Guess out of range. Select a number between {min_num} and {max_num}.")
                else:
                    break
            except ValueError:
                print(f"Select a number between {min_num} and {max_num}.")
        
        times_guessed += 1

        if guess < random_number:
            print("Too low!")
            min_num = guess

        elif guess > random_number:
            print("Too high!")
            max_num = guess

        elif guess == random_number:
            has_won = True
            break
        
        num_of_guesses -= 1
        print()

    if has_won:
        print("Congratulations! You win!")
        print(f"You guessed the number in {times_guessed} attempts.\n")

    else:
        print("Sorry! You lose.")
        print(f"The number was {random_number}\n")


while True:
    Game()

    play_again = input("Play again? y or n: ")
    if play_again.lower() == "y":
        print()
    else:
        break