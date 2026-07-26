# %%
#Statement
#below it's a print and assignment statement within a conditional statement.

name = 'Ann'
if name == 'Ann':
    print('Hi!')
    number = 1

# %%
#Block
age = int(input('What is your age? '))
#define age before using it!
if age > 17:
    #beginning of a conditional block
    print('You are of age!')
    age = age + 1
    print('You are now a year older.....')

print('This here belongs to another block..')

# %%
#Expressions
#Because all expressions have types they can be assigned to variables

#The variable x is assigned to the value of the expression 1 + 2

x = 1 + 2

3 * x + x ** 2

# %%
#Finding out the data type

print(type('Anna'))
print(type(100))

# %%
#Debugging

#Refers to finding the causes of bugs.
hourly_wage = float(input('Hourly wage: '))
hours = int(input('Hours worked: '))
day = input('Day of the week: ')

daily_wages = hourly_wage * hours
if day == 'sunday':
    daily_wages * 2

print(f'Daily wages: {daily_wages} euros')



# %%
hourly_wage = float(input("Hourly wage: "))
hours = int(input("Hours worked: "))
day = input("Day of the week: ").lower()

daily_wages = hourly_wage * hours

if day == "sunday":
    daily_wages *= 2  # Reassigning the doubled value back to daily_wages

print(f"Daily wages: {daily_wages} euros")
# %%
#More conditionals
num = int(input('Please type in number: '))

if num < 0:
    print('The number is negative.')

if num > 0:
    print('The number is positive.')

# %%
num = int(input("Please enter in a number: "))

if num < 0:
    print('The number is a negative.')
else:
    print("The number is either a positive or zero")

# %%
#checking whether the number is even or odd,
#Parity can be checked using the module operator %
num = int(input('Please enter in a number: '))
 
if num % 2 == 0:
    print('The number is even.')
else:
    print('The number is odd.')
# %%
correct = 'kittycat'
password = input('Please enter in a password: ')

if password == correct:
    print("You are welcome!")
else:
    print('No adimittance!....')
# %%
#Am going to write a programme asking the user for their age.


age = int(input('What is your age: '))
if age > 18:
    print('You are of age!.')
else:
    print('You are not of age!')
# %%
#Alternative branches using the elif statement

goals_home = int(input('Home goals scored: '))
goals_away = int(input('Away goals scored: '))

if goals_home > goals_away:
    print('Home team won!.')
elif goals_away > goals_home:
    print('Away team won!')
else:
    print("It's a tie!.")


# %%
#There's no limit to the number of elif statements

print('The Holiday calender!')

date = input("What's the date today?")
if date == "Dec 26":
    print('It is boxing day!')
elif date == "Dec 31":
    print('Hogmanay')
elif date == "Jan 1":
    print("It's new years!")
# %%
