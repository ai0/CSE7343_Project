import os
from pcb import PCB, PCBQueue
from menu import *
from helper import *

def pcb_main():
    ready_queue = PCBQueue()
    waiting_queue = PCBQueue()

    while True:
        op = pcb_main_menu()
        if op == '1':
            queue = ready_queue if pcb_queue_menu() == '1' else waiting_queue
            add_mode = pcb_add_menu()
            if add_mode == '2':
                insert_to_pid = pcb_sub_menu(0)
            else:
                insert_to_pid = None
            pid = pcb_sub_menu(1)
            priority = pcb_sub_menu(2)
            state = pcb_sub_menu(3)
            pcb = PCB(pid, priority, state)
            try:
                queue.add(pcb, insert_to_pid)
            except Exception as e:
                warn(f'\n{e}\n')
                nav('Press any key to continue...')
        elif op == '2':
            queue = ready_queue if pcb_queue_menu() == 1 else waiting_queue
            pid = pcb_sub_menu(4)
            try:
                queue.delete(pid)
            except Exception as e:
                warn(f'\n{e}\n')
                nav('Press any key to continue...')
        elif op == '3':
            queue = ready_queue if pcb_queue_menu() == 1 else waiting_queue
            pid = pcb_sub_menu(4)
            try:
                pcb_info = queue.inspect(pid)
                pcb_print([pcb_info])
            except Exception as e:
                warn(f'\n{e}\n')
            nav('Press any key to continue...')
        elif op == '4':
            queue = ready_queue if pcb_queue_menu() == 1 else waiting_queue
            queue_info = queue.info()
            if queue_info == None:
                warn('\nEmpty Queue!\n')
            else:
                pcb_print(queue_info)
            nav('Press any key to continue...')
        elif op == '5':
            break

def main():
    while True:
        op = main_menu()
        if op == '1':
            pcb_main()
        elif op == '2':
            fcfs_main()
        elif op == '3':
            break


if __name__ == '__main__':
    main()
