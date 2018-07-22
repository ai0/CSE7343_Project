
class PCB:

    def __init__(self, pid, arrival_time, burst_time, priority, state='ready'):
        self.pid = int(pid)
        self.arrival_time = int(arrival_time)
        self.burst_time = int(burst_time)
        self.priority = int(priority)
        self.state = state

    def info(self):
        return [self.pid, self.arrival_time, self.burst_time, self.priority, self.state]


class DoublyNode:

    def __init__(self, data):
        self.data = data
        self.pre = None
        self.next = None


class PCBQueue:

    def __init__(self):
        self.tail = DoublyNode(None)
        self.pids = set()

    def find(self, pid):
        pid = int(pid)
        if pid not in self.pids:
            return None
        pointer = self.tail
        if pointer.data == None:
            return None
        while pointer:
            if pointer.data.pid == pid:
                return pointer
            pointer = pointer.pre
        return None

    def add(self, pcb, insert_to_pid=None):
        if pcb.pid in self.pids:
            raise Exception('PID Already Exist!')
        if self.tail.data is None and insert_to_pid is None:
            self.tail.data = pcb
        elif insert_to_pid is None:
            new_node = DoublyNode(pcb)
            new_node.pre = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            target = self.find(insert_to_pid)
            if target is None:
                raise Exception('Position PID Not Found!')
            new_node = DoublyNode(pcb)
            new_node.pre = target
            new_node.next = target.next
            target.next.pre = new_node
            target.next = new_node
        self.pids.add(pcb.pid)

    def delete(self, pid):
        target = self.find(pid)
        if target is None:
            raise Exception('Target PID Not Found')
        if target.pre:
            target.pre.next = target.next
        if target.next:
            target.next.pre = target.pre
        if not target.pre and not target.next:
            target.data = None
        else:
            del target
        self.pids.remove(int(pid))

    def inspect(self, pid):
        target = self.find(pid)
        if target is None:
            raise Exception('Target PID Not Found')
        return target.data.info()

    def info(self, reversed=False):
        pointer = self.tail
        if pointer.data == None:
            return None
        if reversed is False:
            pointer = self.tail
            while pointer.pre:
                pointer = pointer.pre
        queue_info = []
        while pointer:
            queue_info.append(pointer.data.info())
            pointer = pointer.pre if reversed else pointer.next
        return queue_info
