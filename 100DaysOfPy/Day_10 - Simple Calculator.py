# TITLE: Simple Calculator
# DESCRIPTION: Calculator app that takes 2 number inputs, and a math operator input to output a result. 
# Can continue operations with another input and math operator using the previous result.
# DATE: 06Feb2023

def addTwo(x,y): return x+y

def subTwo(x,y): return x-y

def multTwo(x,y): return x*y

def divTwo(x,y): 
    if y==0: return 'Error, cannot divide by 0'
    else: return x/y

skipNum1 = False    # tracks if the first number is reused from previous resultant

while True:
    # Prompts User inputs
    if skipNum1 == False: num1 = int(input('Enter first number:\n'))
    mathOp = input('Pick an operation: +, -, *, /\n')
    num2 = int(input('Enter second number:\n'))
    
    # Performs Calculations
    try:
        match mathOp:
            case '+': result = addTwo(num1,num2)
            case '-': result = subTwo(num1, num2)
            case '*': result = multTwo(num1, num2)
            case '/': result = divTwo(num1, num2)
    except: 
        print('Error, please try again.')
        skipNum1 = False
        continue
    print('Result:', result)
    
    # Prompts User to continue calculation or stop
    if input('Continue calcuations? Y or N \n').lower() == 'n': break
    
    # Prompts User to reuse resultant or use new value
    if type(result) !=str:
        if input(f"Continue continue calculating with {result}(Y) or start new calculation?(N): Y or N\n").lower() == 'y':
            num1= result
            skipNum1 =True

# Reflection:
# Can add new math operations or inputs. Has very limited usage but good practice for displaying usage of functions.
