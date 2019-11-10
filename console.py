from pathlib import Path
from console_pac.con_help import help_con

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
                if input_lst[0] == 'help':
                    help_con(input_lst)
