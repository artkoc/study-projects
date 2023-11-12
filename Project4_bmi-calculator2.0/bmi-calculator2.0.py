# Enter your height in meters e.g., 1.55
#height = float(input())
# Enter your weight in kilograms e.g., 72
#weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Over 18.5 but below 25 they have a normal weight
#Equal to or over 25 but below 30 they are slightly overweight
#Equal to or over 30 but below 35 they are obese
#Equal to or over 35 they are clinically obese.
#Under 18.5 they are underweight

#Initial code

#height_square = height ** 2
#bmi = weight / height_square

#if bmi > 18.5 and bmi < 25:
#    print("You have a normal weight.")
#elif bmi >= 25 and bmi < 30:
#    print("You are slightly overweight.")
#elif bmi >= 30 and bmi < 35:
#    print("You are obese.")
#elif bmi >= 35:
#    print("You are critically obese.")
#else:
#    print("You are underweight.")

#Corrected code

# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())

bmi = weight / (height * height)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
