number = '10'
guess_count = 4

print("I'm thinking of a number...")
guess = input(f"What number am I thinking of? You have {guess_count + 1} guesses. Enter 'q' to quit. ")

while True:
    if guess == 'q' or guess_count == 0:
        print(f"Sorry! The number was {number}.")
        break
    elif guess == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        guess = input(f"Try again. What number am I thinking of? You have {guess_count} guesses left. Enter 'q' to quit. ")
        guess_count -= 1