#!/usr/bin/env python
# coding: utf-8

# In[254]:


import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

user = input("Do you want strong or weak password? ")
if user == 'strong':
    password = []
    while len(password)<7:
        letter = random.choice(letters)
        password.append(letter)
    
    while len(password)<10:
        number = random.choice(numbers)
        password.append(number)
    print(''.join(password))
    
if user == 'weak':
    password = []
    while len(password)<5:
        letter = random.choice(letters)
        password.append(letter)
    
    while len(password)<6:
        number = random.choice(numbers)
        password.append(number)
    print(''.join(password))


# # 

# In[ ]:




