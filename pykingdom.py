#! /usr/bin/python
import sys
sys.path.insert(1,sys.path[0]+'/strings')
print('Choose your name:')
name=raw_input('Name: ')
print('')

print('Please enter type number:')
try:
    type=input('Type: ')
except:
    print('Please enter a number!')
print('')
print('Choose World: ')
print('1 - Castalem')

print('Please enter world number:')
try:
    world=input('World: ')
except:
    print('Please enter a number!')
print('')
if world==1:
    import world1
    world1.play(name,type)




print('Thanks for playing!')
