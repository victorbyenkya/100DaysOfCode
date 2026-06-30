# %%
# Printing means that the program will show some text on the screen
#The text must be encased in quotation marks.
#Quotation marks signify strings, letters,numbers, and any other character.
print('Hello there!.')
print("2+2*10")
print('"Come right back!", Shouted the police officer.')

#Arithmetic operations
print(2+2)
print(2+2*10)


# %%
#input refers to any information a user gives to the program
name = input("What is your name? ")
print("Hi there, " + name)

symbol = input("What is your name? ")
print(symbol)
print(symbol)

name = input("What is your name? ")
print("Hi ," + name + "!")
print(name + " is quite a nice name. ")
print("Hi " + name + "! let me make sure: your name is " + name + "!")

#using more than input
name = input("What is your name? ")
email = input("What is your email address? ")
nickname = input("What is your nickname? ")

print("Let's make sure this is right")
print("Your name is: " + name)
print("Your email address is: " + email)
print("Your nickname is: " + nickname)

address = input("What's your address? ")
print("Your address is " + address)
address = input("What's your new address in a year's time? ")
print("Okay that " + address + " place is a good one!")


# %%
#The value in variables can also be used to define another variable
first_name = "Victor"
given_name = "Byenkya"

name = given_name + " " + first_name

print(name)



# %%
#Changing the value of the variable
word = input('Please type in a word: ')
print(word)

word = input('And another word: ')
print(word)

word = "Third"
print(word)

#the value assigned to a variable changes each time the variable is assigned a new value. 

word = input('Please type in a word: ')
print(word)

word = word + "!!!"
print(word)


# %%
print("We are now back!!!!!   ")

#Integers
#The following contains a variable age, that contains an Integer
age = 24
print(age)

#The quotation marks makes an integer a string 
#why does it matter?????.....

number_1 = 100
number_2 ='100'

print(number_1)
print(number_2)
#some how on printing it looks the same but it's way different

print(number_1 + number_1)
print(number_2 + number_2)

#Here's where it matters most:
#the integer variable takes + operator as an addition 
#while the string variabke take the + operator as a concatenator


# %%
#Combining values while printing

result = 10 * 25
print("The result is " + str(result))
#the "The result is " is a string and the "result is an integer" so combiningthe two 
#we always have to make an int a str by attaching the str operator!

#the easiest way to fore go the str and the int opertors
#is by using a comma,
# the print command has it as an in built function

result = 10 * 25
print("The result is", result)

# %%
#Using f strings,
#this is the easiest way to combine variables

result = 10 * 25
print(f"The result is {result}")
#with in the string 
#the enclosed the curly brackets 
#is the variable name "results"
#the value it contains becomes part of the printed string





# %%
#a single string can contain multiple variables
name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print(f"My name is {name}, I am {age} years old.")
print("my skills are")
print("- ", skill1, " (", level1, ")")
print("- ", skill2, " (", level2, ")")
print("- ", skill3, " (", level3, " )")
print(f"I am looking for a job with a salary of {lower} - {upper} euros per month")


# %%

#floating numbers refer to numbers with a decimal point
number1 = 2.5
number2 = -1.25
number3 = 3.62

mean = (number1 + number2 + number3) / 3
print(f"mean: {mean}")

x = 4
y = 9
print(f" {x+y} = ")


# %%
#Recap Recap!
#A simple program which asks the user's name and adress

given_name = input('What is your given name? ')
family_name = input('What is your family name? ')
street_address = input('What is your street address? ')
city_and_postal_code = input('What is your city and postal code? ')

print(f"Given name: {given_name}")
print(f"Family name: {family_name}")
print(f"Street address: {street_address}")
print(f"City and postal code: {city_and_postal_code}")

print(f"{given_name} {family_name}")
print(street_address)
print(city_and_postal_code)



# %%
#making sure we dont print the line change while using the print command

print("Hi ", end="")
print("there!")


# %%
#Arithmetic operations

print(2 + 3 * 3)
#the order of operation is similar from mathematics
#the order changs with parentices

print((2 + 3) * 3)

height = 172.5
weight = 68.55

## the Body Mass Index, or BMI, 
##is calculated by dividing body mass with the square of height
#height is coverted into meters in the formula

bmi = weight / (height / 100) **2

print(f"The BMI is {bmi}")


#notice also python has an integer division operator(//)

x = 3
y = 2

print(f"/Operator = {x/y}")
print(f"//Opertor = {x//y}")

#Numbers as input
input_str = input("Which year where you born? ")
year = int(input_str)
print(f"Your age at the end of the year 2027: {2027 - year}")




# %%
