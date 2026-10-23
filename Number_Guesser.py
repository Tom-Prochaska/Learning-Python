from random import randint, random                                                              #Import randit so random doesn't have to be called with random.randint

possible = list(range(1, 101))                                                                  # Create a list of possible numbers

print("Let me guess your number!")
input("Think of a number between 1 and 100, and press Enter when you're ready...")

while True:
    print("--------------------------------")
    number = randint(possible[0], possible[-1])                                                 # Generate a random number from the possible numbers
    print(f"Is your number {number}? You can respond with 'yes', 'higher', or 'lower'.")

    answer = input().strip().lower()                                                            # User input is stripped of whitespace and converted to lowercase for consistency

    if answer == 'yes':
        print("Yay! I guessed your number!")
        break
    elif answer == 'higher':
        possible = [n for n in possible if n > number]                                          # Filter possible numbers to only include those higher than the guessed number in the array
    elif answer == 'lower':
        possible = [n for n in possible if n < number]                                          # Filter possible numbers to only include those lower than the guessed number in the array