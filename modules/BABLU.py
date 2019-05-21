#This list contains predefined responses by the Smart Calculator assistant BABLU 
responses = ['***Welcome to this console of Smart Calculator***','my name is BABLU ,Your Own Smart Calculator Assistant','Thanks for using Smart Calculator. I hope you would Love to use my services again. CHEERS!',
            'Sorry! I could not able to make sense what you typed in',]

def extract_numbers_from_text(text):
    listt = [] # an empty list and can't use list as var name coz of the name conflict
    for word in text.split(' '):       # here text would contain the input by the user and we will split it out by delimter space and we know that split function will return a list of strings
        try:
            listt.append(float(word))
        except ValueError:
            pass
    return listt

def LCM(a,b):
    n = a if a>b else b 
    while n <= a * b:
        if n % a == 0 and n % b == 0:
            return n
        n += 1

def HCF(a,b):
    n = a if a<b else b 
    while n >= 1:
        if a % n == 0 and b % n == 0:
            return n
        n -= 1 # eqv. to n = n - 1

def Add(a,b):
    return a + b

def Sub(a,b):
    return b - a

def Multiply(a,b):
    return a * b

def Divide(a,b):
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

# operations = {
#     Add : ['ADD','ADDITION','PLUS','SUM','+'],
#     Sub : ['SUBTRACT','SUBTRACTION','DIFFERENCE','SUB','-'],
#     Multiply : ['MULTIPLY','MULTIPLICATION','PRODUCT','X','*'],
#     Divide : ['DIVIDE','DIVISION','/'],
#     LCM : 'LCM',
#     HCF : 'HCF'
# }

operations = {
    'ADD' : Add,
    'ADDITION' : Add,
    'PLUS' : Add,
    'SUM' : Add,
    '+' : Add,

    'SUBTRACT' : Sub,
    'SUBTRACTION' : Sub,
    'DIFFERENCE' : Sub,
    'SUB' : Sub,
    '-' : Sub,

    'MULTIPLY' : Multiply,
    'MULTIPLICATION' : Multiply,
    'PRODUCT' : Multiply,
    'X' : Multiply,
    '*' : Multiply,

    'DIVIDE' : Divide,
    'DIVISION' : Divide,
    '/' : Divide,

    'LCM' : LCM,
    'HCF' : HCF
}

commands = {
   'NAME' :  name,
    #Exit : ['EXIT','END','CLOSE','TERMINATE']
    'EXIT' : Exit,
    'END' : Exit,
    'CLOSE' : Exit,
    'TERMINATE' : Exit
}
