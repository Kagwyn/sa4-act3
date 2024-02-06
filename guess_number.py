number = '10'

print("I'm thinking of a number...")
guess = input("What number am I thinking of? Enter 'q' to quit. ")

while True:
    if guess == 'q':
        print(f"Sorry! The number was {number}.")
        break
    elif guess == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        guess = input("Try again. What number am I thinking of? Enter 'q' to quit. ")