print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

#Initial code

#if size == "S":
#    pizza = 15

#elif size == "M":
#    pizza = 20

#elif size == "L":
#    pizza = 25

#if add_pepperoni == "Y":
#    pizza += 2

#if add_pepperoni == "Y":
#    pizza += 3

#if extra_cheese == "Y":
#    pizza += 1


#    print(f"Your final bill is: ${pizza}.\n")

#else:
#    print(f"Your final bill is: ${pizza}.\n")



#corrected code

bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")

