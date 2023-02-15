'''A palindrome is a word or a text that reads the same backward as forward.
Create a program that checks if the word is a palindrome.'''

a_word = input()

if a_word == a_word[::-1] :
    print('Palindrome')
else:
    print('Not Palindrome')