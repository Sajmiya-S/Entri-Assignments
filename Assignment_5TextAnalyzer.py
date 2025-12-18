# Write a Python program that works with text. 
# The program should be able to: Find all email addresses in a text. 
# Find all phone numbers in a text. 
# Replace a word in the text with another word.

import re

email = r'[a-z]+@[a-z]+.[a-z]+'
phone = r'[0-9()]+[\s-][0-9-]+[0-9]+'

print('\nWelcome to Text Analyzer!!!')
text = input('\nEnter your text: ')
print('\n 1. Find all email addresses\n 2. Find all phone numbers\n 3. Replace word ')

n = int(input('\nEnter your choice: '))

if n == 1:
    result = re.findall(email,text)
    print('\nEmail Addresses : ',result)
elif n == 2:
    result = re.findall(phone,text)
    print('\nPhone Numbers : ',result)
elif n == 3:
    word = input('Select the word to be replaced: ')
    new_word = input('Enter the word to replace : ')
    result = re.sub(word,new_word,text)
    print('\nNew text: ',result)
else:
    print('Invalid choice')
