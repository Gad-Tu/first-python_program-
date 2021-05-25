#This program print your age.

birth_year = int(input("birth-year: "))
age = 2021 - birth_year
print("my age: ", age)

# This program evaluates the hypotenuse c.
# a and b are the lengths of the legs.
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5  # We use ** instead of square root.
print("c =", c)

# This is a test program.
x = 1
y = 2
# y = y + x #no longer needed.
print(x + y)
#This program show us, how to use the input function.
anything = input("Enter a number: ")
something = int(anything) **2
print(anything, "to the power of 2 is", something)

# More than one input and type casting.
leg_a = float(input("Input the first leg length:"))
leg_b = float(input("Input the second leg length:"))
hypo = (leg_a**2 + leg_b**2)** .5
print ("The hypotenuse of length is:", hypo)

# + sing as concatinator
fname = input("May i have your firstname, please? ")
lname = input("May i have your lastname, please? ")
print("Thank you!")
print("\n Your name is " + fname + " " + lname + ".")

#this program is gone show us the replication operator.
print("+" + 10 * "-" + "+")
print(("|" + " " *10 + "|\n")*1, end="")
print("+" + 10 * "-" + "+")

#this program calculate the hour and time
start_hour = int(input("The starting hour is: "))
start_minute = int(input("The starting minutes is: "))
length = int(input("The length of event is: "))

endhour = start_hour + (length // 60)   #calculate number hours
endminute = start_minute + (length % 60) # no of minutes
endhour += endminute // 60               #no of hour added to previous one
endminute = endminute % 60               # no of minute added to prevous one


print('{}:{}'.format(endhour, endminute))

