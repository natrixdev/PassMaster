import random
import string 
import os  # importing modules.

letters = string.ascii_letters


password = input('Type something to create a password >')#            |----------------|-|--------------|           
number = input ('Choose :\n [1] > Simple\n [2] > Strong\n >')         #    [1]  >  choice               #
if number <= 1: #                                                     |                                 |
    print('Simple Password') #                                        |                                 |
    print ( ''.join(random.choice(letters) for i in range(5)) )#      |                                 |
elif number <= 2:                                                     #    [2]  > password generating   #
    print("Strong Password:")#                                        |                                 |
    print ( ''.join(random.choice(letters) for i in range(10)) )#     |                                 |
else: #                                                               |                                 |
    print('Not A Good Choice')#                                       |                                 |
    #                                                                 |                                 |
os.create_file('./password_manager.txt')                              #    [3]  > password saving       #
os.write(password, 'password_manager.txt')#                           |----------------|-|--------------|
