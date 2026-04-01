h = float(input("Enter your height in meters: "))
w = float(input("Enter your weight in kg: "))
bmi = (w/(h**2))
print("Your BMI is: ", bmi)
if bmi < 18.5 and bmi > 0:
    print("You are underweight.")
elif bmi < 25 and bmi >= 18.6:
    print("You have a normal weight.")
elif bmi < 30 and bmi >= 25.1:
    print("You are overweight.")
else:
    print("You are obese.")