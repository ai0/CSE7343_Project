import os
import tableprint as tp

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
nav = lambda msg: input(f'\033[42m{msg}\033[0m ')
info = lambda msg: print(f'\033[94m{msg}\033[0m')
guide = lambda msg: print(f'\033[93m{msg}\033[0m')
warn = lambda msg: print(f'\033[91m{msg}\033[0m')

def banner(msg, style='banner'):
    print('\033[92m', end='')
    tp.banner(msg, width=60, style=style)
    print('\033[0m', end='')

def pcb_print(pcb_info):
    print('\033[96m', end='')
    tp.table(pcb_info, headers=['PID', 'Arrival Time', 'Burst Time', 'Priority', 'State'], width=12)
    print('\033[0m', end='')

def scheduler_print(result):
    print('\033[96m', end='')
    tp.table(result, headers=['PID', 'Arrival Time', 'Burst Time', 'Priority', 'Completion Time', 'Turn Around Time', 'Waiting Time'], width=12)
    print('\033[0m', end='')

def main_menu():
    clear()
    banner('CSE 7343 Course Project - Summer 18')
    banner('<Jing Su> (47528095)', style='clean')
    info('\nProject parts:\n')
    guide('1) PCB Queue Manipulation')
    guide('2) Run FCFS Scheduler on the Ready queue')
    guide('3) Run Non-preemptive Priority Scheduler on the Ready queue')
    guide('4) Run Round-Robin Scheduler on the Ready queue')
    guide('5) Exit\n')
    return nav('Please input part index: ')

def pcb_menu_header():
    clear()
    banner('PCB Queue Manipulation')
    banner('<Jing Su> (47528095)', style='clean')

def scheduler_menu_header(title):
    clear()
    banner(f'Run {title} Scheduler on the Ready queue')
    banner('<Jing Su> (47528095)', style='clean')

def pcb_main_menu():
    pcb_menu_header()
    info('\nManipulation Operations:\n')
    guide('1) Import processes from text file')
    guide('2) Add a PCB to a queue')
    guide('3) Delete a PCB from a queue')
    guide('4) Insepect a specific PCB')
    guide('5) Print a queue')
    guide('6) Back to main menu\n')
    return nav('Please input operation index: ')

def pcb_queue_menu():
    pcb_menu_header()
    info('\nProcess Queues:\n')
    guide('1) Ready Queue')
    guide('2) Waiting Queue\n')
    return nav('Please input queue index: ')

def pcb_add_menu():
    pcb_menu_header()
    info('\nAdd a PCB to a queue:\n')
    guide('1) To tail (default)')
    guide('2) Next to a given PCB\n')
    return nav('Please input operation index: ')

def pcb_sub_menu(idx=0):
    prompt_text = (
        'What is the input text file path: ',
        'What is the insert position PCB PID: ',
        'What is the new Process PID: ',
        'What is the new Process Arrival Time: ',
        'What is the new Process Burst Time: ',
        'What is the new Process Priority: ',
        'What is the Target PCB PID: '
    )[idx]
    return nav(prompt_text)

def scheduler_menu(scheduler, queue_info):
    scheduler_menu_header(scheduler)
    info('\nThe initial Ready queue:\n')
    pcb_print(queue_info)
    info(f'\n{scheduler} output:\n')