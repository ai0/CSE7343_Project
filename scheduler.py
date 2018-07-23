from functools import cmp_to_key

avg_time = lambda reuslt, idx: round(sum([p[idx] for p in reuslt]) / len(reuslt), 5)

def get_queue_data(queue_info):
    return [dict(zip(
        ['pid', 'arrival_time', 'burst_time', 'priority'],
        row
    )) for row in queue_info]

def npp_sort_cmp(x, y):
    if x['priority'] == y['priority']:
        return x['arrival_time'] - y['arrival_time']
    else:
        return x['priority'] - y['priority']

def fcfs_scheduler(queue, **kwargs):
    timer = 0
    result = []
    while len(queue.pids) > 0:
        # find the earliest arrive process
        pointer = queue.tail
        earliest_time = pointer.data.arrival_time
        run_pid = pointer.data.pid
        while pointer:
            if pointer.data.arrival_time <= earliest_time:
                run_pid = pointer.data.pid
                earliest_time = pointer.data.arrival_time
            pointer = pointer.pre
        pcb = queue.find(run_pid).data
        timer += pcb.burst_time
        completion_time = timer
        trun_around_time = completion_time - pcb.arrival_time
        waiting_time = trun_around_time - pcb.burst_time
        result += [pcb.info()[:-1] + [completion_time, trun_around_time, waiting_time]]
        queue.delete(run_pid)
    avg_tat = avg_time(result, 5)
    avg_wt = avg_time(result, 6)
    return result, avg_tat, avg_wt

def npp_scheduler(queue, **kwargs):
    timer = 0
    result = []
    while len(queue.pids) > 0:
        # find the highest priority process
        pointer = queue.tail
        highest_priority = pointer.data.priority
        run_pid = pointer.data.pid
        run_arrival_time = pointer.data.arrival_time
        while pointer:
            if pointer.data.priority < highest_priority:
                run_pid = pointer.data.pid
                run_arrival_time = pointer.data.arrival_time
                highest_priority = pointer.data.priority
            elif pointer.data.priority == highest_priority:
                if pointer.data.arrival_time < run_arrival_time:
                    run_pid = pointer.data.pid
                    run_arrival_time = pointer.data.arrival_time
            pointer = pointer.pre
        pcb = queue.find(run_pid).data
        timer += pcb.burst_time
        completion_time = timer
        trun_around_time = completion_time - pcb.arrival_time
        waiting_time = trun_around_time - pcb.burst_time
        result += [pcb.info()[:-1] + [completion_time, trun_around_time, waiting_time]]
        queue.delete(run_pid)
    avg_tat = avg_time(result, 5)
    avg_wt = avg_time(result, 6)
    return result, avg_tat, avg_wt

def rr_scheduler(queue, **kwargs):
    q = kwargs['q']
    queue_data = get_queue_data(queue.info())
    sorted_queue = sorted(queue_data, key=lambda row: row['arrival_time'])
    timer = 0
    result = []
    while len(queue.pids) > 0:
        for pcb_info in sorted_queue:
            pcb = queue.find(pcb_info['pid']).data
            if pcb.remaining_time <= q:
                timer += pcb.remaining_time
                completion_time = timer
                trun_around_time = completion_time - pcb.arrival_time
                waiting_time = trun_around_time - pcb.burst_time
                result += [pcb.info()[:-1] + [completion_time, trun_around_time, waiting_time]]
                queue.delete(pcb.pid)
                sorted_queue.remove(pcb_info)
            else:
                timer += q
                pcb.remaining_time -= q
    avg_tat = avg_time(result, 5)
    avg_wt = avg_time(result, 6)
    return result, avg_tat, avg_wt