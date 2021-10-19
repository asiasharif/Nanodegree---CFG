### EXERCISE 1 ###
"""
You have a budget of £10 and want to write a program to decide which burger restaurant to go to.

Input the price of a burger using input()
Check whether the price is less than or equal (<=) 10.00
Print the result in the format below
Burger is within budget: True

Hint: remember to convert the input from a string to a decimal with float()

"""
# current_price = input("what is the current price?")
# within_budget = float(current_price) <= 10.00
# print("the burger is within budget: {}".format(within_budget))




### EXERCISE 2 ###
"""
Add code to your burger program to input whether the restaurant has a vegetarian option

The output should say whether the cost is within budget AND has a vegetarian option

    Restaurant meets criteria: True
# 
# """
# price = input('how much is a burger?')
# vegetarian = input('is there a vegetarian option? (y/n)')
#
# within_budget = float(price) <= 10.00
# has_vegetarian = vegetarian == 'y'
# is_good_choice = within_budget and has_vegetarian
# print('restaurant meets criteria: {}'.format(is_good_choice) )
#
# ### EXERCISE 3 ###
# """
# Rewrite the output of your burger program to use if statements
#
# If it is a good choice it should be:
#
#     "This restaurant is a great choice!"
#
# If it is not a good choice it should be:
#
#     "Probably not a good idea"
#
# """
# if (is_good_choice):
#     print('it is good choice')
# if not (is_good_choice):
#     print("i should eat here")

### EXERCISE 4 ###
"""
Complete these exercises together with your instructor and the group

1 Else exercise:

Now that you've finished your burger, you want to pay for your food. 
Let's write a program to calculate your meal and apply a discount if applicable.
If your total meal costs more than £20 and you have a discount, the price will be reduced by 10%. 
The program should print "Discount applied" or "No discount" depending on whether the discount criteria was met.
"""

# meal_price = float(input('How much did the meal cost? '))
#
# discount_choice = input('Do you have a discount? y/n ')
# discount_applicable = discount_choice == 'y'
#
# ### write your code here


"""
2 Elif Exercise:

You're cooking a pizza and need to check that the oven is at the right temperature.

Write a program to:

Ask the user to input the temperature
Prints "The oven is too hot" if the temperature is over 200
Prints "The oven is too cold" if the temperature is under 150
Prints "The oven is at the perfect temperature" if the temperature is 180
Prints "The temperature is close enough" for any other temperature
"""

# temperature = float(input('What is the temperature of the oven? '))
#
# ### your code goes here


### EXERCISE 5 ###
"""
This program uses random to simulate a coin flip.

To finish the program you will need to add the following:

If the random coin flip matches the choice input by the user then they win
Otherwise if the random coin flip does not match the choice input by the user then they lose
"""

# import random
#
# def flip_coin():
#     # your code goes here
#
# choice = input('heads or tails: ')
# result = flip_coin()
#
# print('The coin landed on {}'.format(result))


################################################
###           PALINDROME EXERCISE            ###
################################################

"""
Palindrome Check

Write a function that takes a non-empty string 
and that returns a boolean representing whether the string is a palindrome.

Think and plan your solution first. 
If helps, write a pseudo-code.
"""

# def isPalindrome(string):
#
#     # your solution here
#
#
# print(isPalindrome('hannah'))  # should return True
#
# print(isPalindrome('mummy'))  # should return False
#
# print(isPalindrome('I'))  # should return True