from pathlib import Path
from console import *

def start_console():
    loop = True

    while loop == True:
        input_str = input(">> ")
        input_lst = input_str.split(" ")
        print(input_lst)
        input_lst = list(filter(None, input_lst))
        print(input_lst)
        command = None

        if not input_lst:
            input_lst = input_lst
        elif input_lst:
            command = Path('./consol/commands_py/con_'+input_lst[0]+'.py')
            print(command)
            if input_lst[0] == 'exit':
                loop = False
            elif command.is_file():
                print("yeah")
