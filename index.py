import sys
sys.path.append('/modules/')
import modules
from modules.BABLU import *

print()
print(responses[0])
print()

name = input('BABLU : Please type in your name here so that I can refer you = ').upper()
print()
print(f'''BABLU : {name},that is a very nice name of yours! BTW {responses[1]}
        I would love to help you out with your math calculations''')
while True:
    print() #to change the line
    text = input(f'{name} : ')
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                extracted_num = extract_numbers_from_text(text)
                operation_result = operations[word.upper()](extracted_num[0],extracted_num[1])
                print(f'BABLU : Its {operation_result}!')
            except:
                print('BABLU : Its not making sense what you typed in')
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break 
    else:
        Apology()
