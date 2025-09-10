height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height**2)

if bmi < 18.5:
    print("Underweight.")
elif 18.5 <= bmi < 25:
    print("Normal weight.")
elif 25 <= bmi < 30:
    print("Overweight.")
else:
    print("Obese.")