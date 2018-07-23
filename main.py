import os
import csv
from pcb import PCB, PCBQueue
from scheduler import fcfs_scheduler, npp_scheduler, rr_scheduler
from menu import *

ready_queue = PCBQueue()
waiting_queue = PCBQueue()

def pcb_main():
    while True:
        op = pcb_main_menu()
        if op == '1':
            queue = ready_queue if pcb_queue_menu() == '1' else waiting_queue
            add_mode = pcb_add_menu()
            if add_mode == '2':
                insert_to_pid = pcb_sub_menu(1)
            else:
                insert_to_pid = None
            file_path = pcb_sub_menu(0)
            try:
                with open(file_path) as f:
                    reader = csv.reader(f)
                    next(reader, None) # skip the header row
                    for row in reader:
                        pid, arrival_time, burst_time, priority = row
                        pcb = PCB(pid, arrival_time, burst_time, priority)
                        queue.add(pcb, insert_to_pid)
            except Exception as e:
                warn(f'\n{e}\n')
                nav('Press any key to continue...')
        elif op == '2':
            queue = ready_queue if pcb_queue_menu() == '1' else waiting_queue
            add_mode = pcb_add_menu()
            if add_mode == '2':
                insert_to_pid = pcb_sub_menu(1)
            else:
                insert_to_pid = None
            pid = pcb_sub_menu(2)
            arrival_time = pcb_sub_menu(3)
            burst_time = pcb_sub_menu(4)
            priority = pcb_sub_menu(5)
            pcb = PCB(pid, arrival_time, burst_time, priority)
            try:
                queue.add(pcb, insert_to_pid)
            except Exception as e:
                warn(f'\n{e}\n')
                nav('Press any key to continue...')
        elif op == '3':
            queue = ready_queue if pcb_queue_menu() == '1' else waiting_queue
            pid = pcb_sub_menu(6)
            try:
                queue.delete(pid)
            except Exception as e:
                warn(f'\n{e}\n')
                nav('Press any key to continue...')
        elif op == '4':
            queue = ready_queue if pcb_queue_menu() == '1' else waiting_queue
            pid = pcb_sub_menu(6)
            try:
                pcb_info = queue.inspect(pid)
                pcb_print([pcb_info])
            except Exception as e:
                warn(f'\n{e}\n')
            nav('Press any key to continue...')
        elif op == '5':
            queue = ready_queue if pcb_queue_menu() == '1' else waiting_queue
            queue_info = queue.info()
            if queue_info == None:
                warn('\nEmpty Queue!\n')
            else:
                pcb_print(queue_info)
            nav('Press any key to continue...')
        elif op == '6':
            break

def scheduler_main(scheduler_name, scheduler_func, q=None):
    queue = ready_queue
    queue_info = queue.info()
    if queue_info == None:
        warn('\nEmpty Queue!\n')
    else:
        scheduler_menu(scheduler_name, queue_info)
        result, avg_tat, avg_wt = scheduler_func(queue, q=q)
        scheduler_print(result)
        info(f'Average Turn Around Time = {avg_tat}')
        info(f'Average Waiting Time = {avg_wt}')
    nav('Press any key to continue...')

def main():
    while True:
        op = main_menu()
        if op == '1':
            pcb_main()
        elif op == '2':
            scheduler_main('FCFS', fcfs_scheduler)
        elif op == '3':
            scheduler_main('Non-preemptive Priority', npp_scheduler)
        elif op == '4':
            q = int(nav('Please input Q: '))
            scheduler_main('Round-Robin', rr_scheduler, q=q)
        elif op == '5':
            break

def quick_load():
    # quick load processes.txt under the same folder
    with open('processes.txt') as f:
        reader = csv.reader(f)
        next(reader, None) # skip the header row
        queue = ready_queue
        for row in reader:
            pid, arrival_time, burst_time, priority = row
            pcb = PCB(pid, arrival_time, burst_time, priority)
            queue.add(pcb, None)

if __name__ == '__main__':
    quick_load()
    main()
