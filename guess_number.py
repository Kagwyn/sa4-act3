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
        try:
            guess = int(guess)
            if guess < int(number):
                guess = input("Try again. Your guess is too low. Enter 'q' to quit. ")
            else:
                guess = input("Try again. Your guess is too high. Enter 'q' to quit. ")
        except:
            guess = input("Try again. Your guess was not an integer value. Enter 'q' to quit. ")
        