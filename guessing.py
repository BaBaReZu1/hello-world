import random

counter = 0
secret_number = random.randint(1, 100)

while True:
    guessing_number = None
    while type(guessing_number) is not int:
        try:
            guessing_string = input("Give me number: ")
            guessing_number = int(guessing_string)
        except ValueError: 
            print("Please add a number!")

    counter += 1
    if secret_number < guessing_number:
        print("The generated number is smaller")
    elif secret_number > guessing_number:
        print("The generated number is bigger")
    elif secret_number == guessing_number:
        print("you win!")
        break

print("This is a secret number : ",secret_number)
print(f"You win with {counter} number of guesses")
