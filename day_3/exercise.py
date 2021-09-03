# ITP Week 2 Day 3 Exercise


#Write a basic calculator using the input function to complete the following tasks.  Be sure to call your functions at the end, using the correct arguments.

# Easy:
#     - A function that subtracts one integer from another
def Subtraction (num1,num2):
    difference = num1 - num2
    return difference

print(Subtraction(1,1))

#     - A function that multiplies three integers
def Multiplication(num1,num2):
    product = num1 * num2
    return product

print(Multiplication(4,4))

#     - A function that adds four integers
def Addition4 (num1,num2,num3,num4):
    sum = num1 + num2 + num3 + num4
    return sum

print(Addition4(3,3,3,3))


# Medium: 
#     - Create a calculator function using THREE input parameters (two float, one string[hint: it will be a math symbol]) to allow the user to add, substract, multiply and divide.
def Addition (num1,num2):
    sum = num1 + num2
    return sum

def calculator (num1,num2,operation):
    global Addition
    global Subtraction
    global Multiplication

    if operation.lower() == "addition" or "add":
        return print(Addition(num1,num2))
    elif operation.lower() == "subtraction" or "subtract":
        return print(Subtraction(num1,num2))
    elif operation.lower() == "multiplication" or "multiply":
        return print(Multiplication(num1,num2))
    else: 
        print("Invalid input")
        

# operation = input("Choose an Operatiion: Addition, Subtraction, Multiplication. ")
# calculator(1,1,operation)

# Hard: 
#     - You're at a restaurant with some friends and the server didn't split up the check.  Create a function that takes a bill amount, multiplies it by a global variable called tax_rate, adds the tax, and then divides the total bill by the number of people input by the user.  BONUS:  Include an option for adding tip through either a percentage amount assigned to a global varible, or through a specific amount input by the user.  You may use the math module from the Python standard library.

tax_rate = 10 #global varaible

def splitCalculator (amount,numPeople):
    global tax_rate
    global tipAmount
    taxPercent = tax_rate * .10
    totalAmount = amount + taxPercent + tipAmount
    print(totalAmount)

    splitAmount = totalAmount / numPeople
    print("The bill is $" + str(splitAmount) + " per person.")


numPeople = int(input(("How many people? ")))
tipAmount = int(input("How much do you want to tip? if none put 0. $")) #global variable
splitCalculator(100,numPeople)