print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# Your code below this line 👇

combine_input = name1 + name2
combine_lower_case = combine_input.lower()

t = combine_lower_case.count("t")
r = combine_lower_case.count("r")
u = combine_lower_case.count("u")
e = combine_lower_case.count("e")

combine_word1 = t + r + u + e

l = combine_lower_case.count("l")
o = combine_lower_case.count("o")
v = combine_lower_case.count("v")
e = combine_lower_case.count("e")

combine_word2 = l + o + v + e

final_score = (int(str(combine_word1) + str(combine_word2)))

if final_score < 10 or final_score > 90:
    print(f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score < 50 and final_score > 40:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}.")
