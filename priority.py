import queue
import time

q= queue.PriorityQueue()

q.put((1,'priority 1'))
q.put((3,'priority 3'))
q.put((4,'priority 4'))
q.put((2,'priority 2'))

for i in range(q.qsize()):
    print(q.get()[1])