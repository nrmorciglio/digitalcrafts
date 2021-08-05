greeting = input('Welcome to this calculator program. What is your name?\n')

print(f'Hello ' + greeting + ' ,lets begin!')

print('This calculator is designed to compute up to three numbers. You will be asked if your equation requires a third number. Please follow the prompts to complete your calculation. PLEASE KEEP PEMDAS IN MIND WHEN ENTERING OPERATIONS')
num1 = int(input('Please enter your first number\n'))
op1 = input('enter an operation: + , - , * , /\n')
num2 = int(input('Please enter your second number\n'))

if op1 == '+':
    print(num1+num2)
if op1 == '-':
    print(num1-num2)
if op1 == '*':
    print(num1*num2)
if op1 == '/':
    print(num1/num2)

thirdintegerq = input('Does your equation require a third number? Enter Y for Yes or N for no\n')

if thirdintegerq == 'N':
    op2 = ''
    print('Calculation complete - End of program')
    

elif thirdintegerq == 'Y':

    op2 = input('enter another operation: + , - , * , /\n')

    num3 = int(input('Please enter your third number\n'))



if op1 =='+' and op2 == '+':
    print(num1+num2+num3)

if op1 =='-' and op2 == '-':
    print(num1-num2-num3)

if op1 =='*' and op2 == '*':
    print(num1*num2*num3)

if op1 =='/' and op2 == '/':
    print(num1/num2/num3)

if op1 =='+' and op2 == '-':
    print(num1+num2-num3)

if op1 =='+' and op2 == '*':
    print(num1+num2*num3)

if op1 =='+' and op2 == '/':
    print(num1+num2/num3)

if op1 =='-' and op2 == '+':
    print(num1-num2+num3)

if op1 =='-' and op2 == '*':
    print(num1-num2*num3)

if op1 =='-' and op2 == '/':
    print(num1-num2/num3)

if op1 =='*' and op2 == '+':
    print(num1*num2+num3)

if op1 =='*' and op2 == '-':
    print(num1*num2-num3)

if op1 =='*' and op2 == '/':
    print(num1*num2/num3)

if op1 =='/' and op2 == '+':
    print(num1/num2+num3)

if op1 =='/' and op2 == '-':
    print(num1/num2-num3)

if op1 =='/' and op2 == '*':
    print(num1/num2*num3)
