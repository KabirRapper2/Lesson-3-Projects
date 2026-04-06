import random
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

numbers = [number1, number2, number3]
random.shuffle(numbers)
print("The numbers in random order are:")
for number in numbers:
    print(number)

