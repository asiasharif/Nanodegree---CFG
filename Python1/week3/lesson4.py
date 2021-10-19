import random
### EXERCISE 1 ###
"""
When I'm travelling in the winter I often forget to pack warm clothes.
Let's write a program to help me to remember the right clothes.

The program should check if the first item in the clothes list is "shorts".
If it is it should change the value to "warm coat".
"""

clothes = [
    "shorts",
    "shoes",
    "t-shirt",
]


#check first item
# if clothes[0] == 'shorts':
#     clothes[0] = 'warm coat' #changes value
# print(clothes)

#exercise 2
# game_scores = [3, 5, 50, 60, 70, 80, 90, 100, 110, 200]
# number_of_scores = len(game_scores)
# highest_score = max(game_scores)
# lowest_score = min(game_scores)
# all_scores = sorted(game_scores)
#
# print("number of scorees: {}".format(number_of_scores))
# print("highest score:{}".format(highest_score))
# print("lowest score:{}".format(lowest_score))
# all_scores.reverse()
# print("all score:{}".format(all_scores))

#exercise 3
# shopping_list = [
#     'bread',
#     'cheese',
#     'pop tarts',
#     'carrots',
# ]
#
# if 'bread' in shopping_list:
#     shopping_list.append('butter')
# print(shopping_list)



#exercise 4
# costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
# total_cost = 0
#
# for i in costs:
#     total_cost += i #adding total in for loop - incrementing
#
# print(total_cost)

#exercise 5
# write a list comprehension expression to build a new list of EVEN numbers ONLY from range(5)
#
# your sample output should be [0, 2, 4]
# """
# #
# new_list = [even for even in [0, 2, 4, 6, 8] if even in range(5)]
# print(new_list)
#
# new_list = [even for even in range(5) if even % 2 == 0]
# print(new_list)

# #exercise 6
# place = {
#     'name': 'The Anchor',
#     'post_code': 'E14 6HY',
#     'street_number': '54',
#     'location': {
#         'longitude': 127,
#         'latitude': 63,
#     }
# }
# print(place['name'])
# print(place['post_code'])
# print(place['street_number'])
# #how to access dict inside dict
# print(place['location']['longitude'])
# print(place['location']['latitude'])

#exercise 7
# fruits = [
#     {'name': 'apple', 'colour': 'red', 'price': 0.12},
#     {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
#     {'name': 'pear', 'colour': 'green', 'price': 0.19},
# ]
#
# for fruits in fruits:
#     print(fruits['name'])
#     print(fruits['colour'])
#     print(fruits['price'])


#
# first_name= ['asia', 'abdul', 'ben']
# surname = ['sharif', 'jameli', 'govin']
# chosen_first = random.choice(first_name)
# chosen_last = random.choice(surname)
#
# print("{} {}".format(chosen_first, chosen_last))

### EXERCISE 2 ###
#
# Make a list of game scores. Using list functions write code to output information of the scores in the following format:
#
#     Number of scores: 10
#     Highest score: 200
#     Lowest score: 3
#
# Extension: Output all of the scores in descending order
# """
#
#
# ### EXERCISE 3 ###
# """
# Whenever I'm shopping and I buy some bread I always forget to buy butter.
# Create a list and if 'bread' is in the list, add 'butter' to the shopping list.
#
# Try running the program with and without bread in the list to check that your program works.
#
# Remember the in operator checks if an item is in a list and the .append() method adds an item to a list.
"""
# shopping_list = [
#     'bread',
#     'cheese',
#     'pop tarts',
#     'carrots',
# ]

'''
# ### EXERCISE 4 ###
# """
# I want to work out how much money I've spent on lunch this week. I've created a list of what I spent each day.
# Write a program that uses a for loop to calculate the total cost
# """
#
# # costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
# # total_cost = 0
#
# '''
# ### EXERCISE 5 ###
# """
# write a list comprehension expression to build a new list of EVEN numbers ONLY from range(5)
#
# your sample output should be [0, 2, 4]
# """
#
# # new_list = # your solution to be added here
#
# '''
# ### EXERCISE 6 ###
# """
#  Print the values of name, post_code and street_number from the dictionary
# """
# # place = {
# #     'name': 'The Anchor',
# #     'post_code': 'E14 6HY',
# #     'street_number': '54',
# #     'location': {
# #         'longitude': 127,
# #         'latitude': 63,
# #     }
# # }
#
# '''
# ### EXERCISE 7 ###
# """
# Using a for loop, output the values name, colour and price of each dictionary in the list
# """
# # fruits = [
# #     {'name': 'apple', 'colour': 'red', 'price': 0.12},
# #     {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
# #     {'name': 'pear', 'colour': 'green', 'price': 0.19},
# # ]
#
# '''
# ### EXERCISE 8 ###
# """
# Write a program to create a random name.
# You should have a list of random first-names and a list of last-names.
# Choose a random item from each and display the result.
#
# Extension: Using list of verbs and a list of nouns, create randomised sentences
# """