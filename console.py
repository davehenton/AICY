from pathlib import Path
from console import *

def start_console():
    loop = True

    while loop == True:
        input_str = input(">> ")
        input_lst = input_str.split(" ")
        input_lst = list(filter(None, input_lst))
        command = None

        if not input_lst:
            input_lst = input_lst
        elif input_lst:
            command = Path('./console_pac/con_'+input_lst[0]+'.py')
            if input_lst[0] == 'exit':
                loop = False
            elif command.is_file():
                input_lst[0]+_con(input_lst)
