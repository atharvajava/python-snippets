import queue
import time
import threading

def printing(idx):
    print(idx)

def thread(idx):
    t=threading.Thread(target=printing,args=(idx, ))
    t.start()
q= queue.PriorityQueue()
q.put((1,thread(1)))
q.put((3,thread(3)))
q.put((4,thread(4)))
q.put((2,thread(2)))

for i in range(q.qsize()):
    q.get()[1]