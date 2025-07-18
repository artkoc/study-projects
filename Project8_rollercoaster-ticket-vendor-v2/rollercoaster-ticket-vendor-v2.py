# Rollercoaster-ticket-vendor.
# Initial code

height = int(input("Please type in your height in cm\n"))

"""
if height >= 120:
  print("you can ride the roller coaster!\n")
  age = int(input("What is your age?\n"))

  if age < 12:
    bill = 5
    print("Child tickers are 5$")

  elif age <= 18:
    bill = 7
    print("Youth tickets are 7$")

  elif age <= 45:
    bill = 12
    print("Adult tickets are 12$")

  elif age >= 55:
    bill = 12
    print("Adult tickets are 12$")

  else:
      bill = 0
      print("Relax, It's free")

  picture = str(input("Do you want to buy a picture?\n"))
  if picture == "yes" and age <= 45:
    bill += 3
    print(f"Your final bill is ${bill}")

  elif picture == "yes" and age >= 55:
    bill += 3
    print(f"Your final bill is ${bill}")

  else:
    print(f"Your final bill is ${bill}")

else:
  print("Sorry can't ride.")
"""

# Corrected code

if height >= 120:
  print("you can ride the roller coaster!\n")
  age = int(input("What is your age?\n"))

  if age < 12:
    bill = 5
    print("Child tickers are 5$")

  elif age <= 18:
    bill = 7
    print("Youth tickets are 7$")

  elif age >= 45 and age <= 55:
    bill = 0
    print("Relax, It's free for you.")

  else:
    bill = 12
    print("Adult tickets are 12$")

  picture = str(input("Do you want to buy a picture?\n"))
  if picture == "yes" and age <= 44:
    bill += 3
    print(f"Your final bill is ${bill}")

  elif picture == "yes" and age >= 56:
    bill += 3
    print(f"Your final bill is ${bill}")

  else:
    print(f"Your final bill is ${bill}")

else:
  print("Sorry can't ride.")











