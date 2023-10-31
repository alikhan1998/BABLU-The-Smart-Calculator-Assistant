# This list contains predefined responses by the Smart Calculator assistant BABLU
responses = ['***Welcome to this console of Smart Calculator***',
             'my name is BABLU, Your Own Smart Calculator Assistant',
             'Thanks for using Smart Calculator. I hope you would Love to use my services again. CHEERS!',
             'Sorry! I could not able to make sense of what you typed in']

# Add a global variable to store calculation history
calculation_history = []


def extract_numbers_from_text(text):
    listt = []
    for word in text.split(' '):
        try:
            listt.append(float(word))
        except ValueError:
            pass
    return listt


def LCM(a, b):
    n = a if a > b else b
    while n <= a * b:
        if n % a == 0 and n % b == 0:
            return n
        n += 1


def HCF(a, b):
    n = a if a < b else b
    while n >= 1:
        if a % n == 0 and b % n == 0:
            return n
        n -= 1


def Add(a, b):
    return a + b


def Sub(a, b):
    return b - a


def Multiply(a, b):
    return a * b


def Divide(a, b):
    return a / b


def Exit():
    print('\n')
    print(f'BABLU : {responses[2]}')
    input("BABLU : Press Enter key to exit...")
    exit()


def name():
    print(f'BABLU : {responses[1]}')


def Apology():
    print(f'BABLU : {responses[3]}')


def perform_calculation(expression):
    result = eval(expression)
    calculation_history.append((expression, result))
    return result


def view_history():
    if not calculation_history:
        print("No calculations in history.")
    else:
        print("Calculation History:")
        for i, (expression, result) in enumerate(calculation_history, 1):
            print(f"{i}. {expression} = {result}")


# operations = {
#     Add : ['ADD','ADDITION','PLUS','SUM','+'],
#     Sub : ['SUBTRACT','SUBTRACTION','DIFFERENCE','SUB','-'],
#     Multiply : ['MULTIPLY','MULTIPLICATION','PRODUCT','X','*'],
#     Divide : ['DIVIDE','DIVISION','/'],
#     LCM : 'LCM',
#     HCF : 'HCF'
# }

operations = {
    'ADD': Add,
    'ADDITION': Add,
    'PLUS': Add,
    'SUM': Add,
    '+': Add,

    'SUBTRACT': Sub,
    'SUBTRACTION': Sub,
    'DIFFERENCE': Sub,
    'SUB': Sub,
    '-': Sub,

    'MULTIPLY': Multiply,
    'MULTIPLICATION': Multiply,
    'PRODUCT': Multiply,
    'X': Multiply,
    '*': Multiply,

    'DIVIDE': Divide,
    'DIVISION': Divide,
    '/': Divide,

    'LCM': LCM,
    'HCF': HCF
}

commands = {
    'NAME': name,
    'EXIT': Exit,
    'END': Exit,
    'CLOSE': Exit,
    'TERMINATE': Exit,
    'HISTORY': view_history  # Added command to view history
}

while True:
    user_input = input("You : ").upper()
    if user_input in commands.keys():
        if user_input == 'EXIT':
            commands[user_input]()
        else:
            commands[user_input]()
    elif user_input in operations.keys():
        numbers = extract_numbers_from_text(input("You : "))
        if len(numbers) >= 2:
            print(f'BABLU : {perform_calculation(f"{numbers[0]} {user_input} {numbers[1]}")}')
        else:
            print("Please provide at least two numbers for the operation.")
    else:
        Apology()
