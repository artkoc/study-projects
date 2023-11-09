height = input()
weight = input()

height_float = float(height)
weight_int = int(weight)

bmi = weight_int / height_float ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)

#alternative way which means less code (I did it this way but above is the more explained way)
#What I did here is I put (height_float **2) so that it would be prioritized
#Once the height_float ** 2 is prioritized, I did weight_int / height_float
#I also added int in the beginning so that I don't have to create a variable named bmi_as_int
#print(int(weight_int / (height_float ** 2)))
