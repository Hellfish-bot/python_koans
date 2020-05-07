#!/usr/bin/env python
print('Hello, Overwatch')
name = input('Enter your Overwatch name: ')
print('Hello', name)
rank = input('What is your rank at competitive level?: ')
number = int(input('Enter your SR: '))
if number < 2500:
    print('Your rank is Gold!')
elif number < 3000:
    print('Your rank is Plat!')
else:
    print('Your rank is Diamond!')
    print('Keep playing!')
print('Goodbye', name)