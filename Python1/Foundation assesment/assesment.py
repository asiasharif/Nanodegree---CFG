# Question 1

# 1

# python is a powerful, high level, general purpose programming language. It is easy to learn and

# compact and easier understandable to write code.

# 2

# count() is a function that counts the number of time a string/int appears in a given list.

# example

my_list = ["a,b,c,d,e,f,a,b,d"]

print(my_list.count("a"))

# the above example will return the number of time 'a' appears in the list 'my_list' which is 2


# 3

# the function ord() takes a single character and returns its numerical values as defined in ASCII Table

# the chr() function basically does the opposite of ord(). It takes the numerical value and returns

# the chatacter equevalent of it as defined in the ascii table.

# example

x = chr(72)

print(x)

# will return the character 'H'

y = ord('p')

print(y)

# will return the integer '112'


# 4

the_string = '2020-11-10_sales.csv'

new_string = the_string[0:-4]

print(new_string)

# 5

# A List in python can be added to or be subtracted from its values after it has been created and noted by

# square_bracket[] where as a tuple is immutable and is defined by parenthesis '()'

# the values in a tuple cannot be changed. cannot be added to or deleted from its values

# 6

# The difference between an append() and extend() function is that append() takes an argument and adds it to the end of

# a list which increases the length of the list by one, where as extend() takes any iterable list as a parameter and

# and adds to the list, which could increase the list by one or hundreds, depending on the length of the arguments passed.


# 7

# and infinite loop is one where it does not end. for instance:

"""

x = True

while x:

    do



"""

# the above code does not end as the value of x is always true unless its been edited within the while loop

# you can quit the program programmatically by giving it an exit() function within the while loop.

#infinite loop below
"""

x = True

while x:

    do

    exit()



"""

# this will exit as soon as the loop reaches the exit() funtion. You can also quit the program by 'clt + C' on

# the keyboard.


# 8


# a functions parameter boils down to real value thats passed into a function as its argument.


# 9

"""

my_dic = {"Apple":2,"Juice":5"}



my_dic["Strawberry"]=6



"""

# 10

#Bool(immutable), int(mutable), List(mutable), Tuple(immutable), Str(mutable), Set(mutable), Dict(mutable)

# Question2

text = "Actual Read TEXT filE"

print(sum(1 for capital in text if capital.isupper()))

# 3

my_string = "Applepie"

reversed_string = my_string[::-1]

print(reversed_string)

# 4


animals = ['cat', 'horse', 'elephant', 'dog']


def longest_name(x):
    keeping_count = 0

    for name in x:

        if len(name) > keeping_count:
            keeping_count = len(name)

            found = name

    print("The longest named animal is: " + found)


longest_name(animals)

# 5

"""my way"""

first_number = int(input("Please enter a digit for operation: "))

operation = input("Please enter an operation ( + - * /): ")

second_number = int(input("Please enter your second digit for operation: "))

if operation == "*":

    result = first_number * second_number

elif operation == "/":

    result = first_number / second_number

elif operation == "+":

    result = first_number + second_number

elif operation == "-":

    result = first_number - second_number

else:

    result = "Something went wrong. Please check your operation."

print(result)

"""End of my way"""

"""Examinar's way"""

print("Please select operation:\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n")

select = int(input())

num1 = int(input("Please select first number:\n"))

num2 = int(input("Please select second number:\n"))

if select == 3:

    result = num1 + num2

elif select == 4:

    result = num1 / num2

elif select == 1:

    result = num1 + num2

elif select == 2:

    result = num1 - num2

else:

    result = "Something went wrong. Please check your operation."

print(result)

"""End Examinars way"""
