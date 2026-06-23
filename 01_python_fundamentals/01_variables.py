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


