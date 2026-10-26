print("What do you want me to calculate?")
number1 = input("First number: ")
symbol = input("What do you wanna calculate with? (+, -, *, /): ")
number2 = input("Second number: ")

if symbol == "+":
    answer = float(number1) + float(number2)
elif symbol == "-":
    answer = float(number1) - float(number2)
elif symbol == "*":
    answer = float(number1) * float(number2)
elif symbol == "/":
    answer = float(number1) / float(number2)
else:
    answer = "Invalid symbol"

print(f"Your answer is: {answer}")
