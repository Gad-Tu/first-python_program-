#this program read two numbers

# this program reads two numbers

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# choose the largest number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# print the result
print( "The lager number is: ", larger_number)



# This program test. If you entered the string.
name = input(str("Enter: "))
Upper_case = "Spathiphyllum"
Lower_case = "spathiphyllum"
if name == Upper_case:
    print("Yes - Spathiphyllum is best plant ever!")

elif name == Lower_case:
    print("No, I want a big spathiphyllum!")

else:
    print("Spathiphyllum! Not[input]"





# This program calculte the personal income tax
income = float(input("Enter the annual income: "))

tax_relief = 556 + 2
if income <= 85528:
        tax = ((income * 0.18) - (tax_relief))

elif income > 85528:
        tax = (14839 + 2) + (income - 85528) * 0.32
else:
        tax == 0
    print(" No tax at all.")
tax = round(tax, 0)
print("The tax is:", tax, "thalers"

    #program see the if the year is common or leap year or not within gregory calendar.

    year = int(input("Enter a year: "))

    if (year % 4 and year % 400) != 0:

        print("common year.")

    elif (year % 100) != 0:

        print("leap year")
    else:
        print("Not within the Georgorian calendar")