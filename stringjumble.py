"""
stringjumble.py
Author: Suhan Gui
Credit: http://stackoverflow.com/questions/12794141/reverse-input-in-python
http://stackoverflow.com/questions/18078595/how-do-i-reverse-each-word-in-a-string-but-in-the-same-sentence-order

Assignment: String Jumble

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
s=input('Please enter a string of text (the bigger the better): ')
print('You entered "{0}". Now jumble it: '.format(s))

potato=s[::-1]

print("{0}".format(''.join(reversed(s))))
print("{0}".format(' '.join(reversed(s.split(' ')))))
print("{0}".format(' '.join(reversed(potato.split(' ')))))