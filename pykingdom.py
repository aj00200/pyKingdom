#! /usr/bin/python

print('Choose your name:')
name=raw_input('Name: ')
print('')
print('Choose your type:')
print('1 - Sorcorer')
print('2 - Warrior')

print('Please enter type number:')
try:
    type=input('Type: ')
except:
    print('Please enter a number!')
