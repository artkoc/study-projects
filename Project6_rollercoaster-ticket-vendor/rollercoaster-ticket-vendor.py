# Rollercoaster-ticket-vendor

height = int(input("Please type in your height in cm\n"))

if height >= 120:
  print("you can ride the roller coaster!\n")
  age = int(input("What is your age?\n"))

  if age < 12:
    bill = 5
    print("Child tickers are 5$")
  elif age <= 18:
    bill = 7
    print("Youth tickets are 7$")
  else:
    bill = 12
    print("Adult tickets are 12$")

  picture = str(input("Do you want to buy a picture?\n"))
  if picture == "yes":
    bill += 3
    print(f"Your final bill is ${bill}")

  else:
    print(f"Your final bill is ${bill}")

else:
  print("Sorry can't ride.")
