# question 1 - 60nails needed, had to change chairs = '15' from str to int

# chairs = 15
# nails = 4
# total_nails = chairs * nails
# message = 'i need to buy {} nails'.format(total_nails)
# print('you need to buy nails {}'.format(message))


# question 2 - penelope was not defined as a str, so added '' not it is defined
# my_name = 'Penelope'
# my_age = 29
# message = 'My name is {} and I am {} years old'.format(my_name, my_age)
# print(message)

# question 3
#
# omelettes = int(input('how many omelettes do you want to make?'))
# boxes_needed = omelettes * 4 / 6
#
# print('you can make {} with {} boxes of eggs'.format(omelettes, boxes_needed))

# Question 4 - strings
# my_str = "i love coding!" #replace with (!)
# print(my_str)

# task 2 - reassign str so that all letters are lowercase
# my_str_1 = 'EVERY Exercise Brings Me Closer to Completing my GOALS'
# print(my_str_1.lower())

# task 3 - does the string start with A? - uses start with method
# my_str_2 = 'We enjoy travelling'
# ans_1 = (my_str_2.startswith("A"))
# print(ans_1)

# task 4 print lenght of string
# my_str_3 = '1.458.001'
# ans_2 = (len(my_str_3))
# print(ans_2)

# Question 5
# task 1
# wrd = 'Python'
# ans_1 = (wrd[2:])
# print(ans_1)
# or an easier way that also works =
# wrd = 'Python'
# print(wrd[2:])

# task 2
# wrd = 'Python'
# ans_1 = (wrd[4:5])
# print(ans_1)

# task 3
# wrd = 'Python'
# ans_1 = (wrd[2:4])
# print(ans_1)

# task 4 - steps of 2 - excluded first and last letter then with steps of 2
# wrd = 'python'
# ans_1 = wrd[1:5:2]
# print(ans_1)

# question 6 - the program below - the 'o' is a string so when you multiply it by a number it will return the string
# in that amount of numbers, for example it looped through once it will return a single 'o', loops through twice
# it will return 2 lots of 'oo' and so on until it return 100 'o'
# the variable number is being auto incremented in the for loop until it reaches 100 and terminates
#
# for number in range(100):
#      output = 'o'* number
#      print(output)

# question 7 - the problem was - he created a function but did not call the function
# he was also calling the function within the same function
# below is the correct way
# def calculate_vat(amount):
#     total = amount*1.2
#     print(total)
# calculate_vat(100)

# #question 8 - two ways below
# item = "apple"
# item_p = 2
# item_1 = "Grape"
# item_1_p = 3
# item_2 = "Banana"
# item_2_p = 1.5
#
#
# def cashier_receipt(i, j, k):
#     print("{} ________ {}".format(item, i))
#     print("{} ________ {}".format(item_1, j))
#     print("{} ________ {}".format(item_2, k))
#     print("Total ________ {}".format(i + j + k))
# #
# #
# # #
# # #
# cashier_receipt(item_p, item_1_p, item_2_p)

# or way 2 which is the first way i did it also same output but couldnt figure out how to get it to look like receipt  -
# item = {'Apple': 1, 'Banana': 2, 'Grape': 3}
#
#
# def cashier_receipt():
#     for i in item.items():
#         print(i[0], '\t', i[1])
#     print("Total.... {}".format(sum(item.values())))
#
#
# cashier_receipt()


x = chr(72)

print(x)