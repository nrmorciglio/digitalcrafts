num1 = int(input('Please enter a number that gives you both Fizz & Buzz\n'))
if (num1 % 3 == 0 and num1 % 5 == 0):
    print('Fizz Buzz')

elif (num1 % 3) == 0:
    print('Fizz')

elif (num1 % 5) == 0:
    print('Buzz')

else:
    print('Sorry! Run this program once more and try again')


