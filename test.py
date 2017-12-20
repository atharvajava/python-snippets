import queue
li=[1,2,3,4,5,6,7,8,9,10]
i=0
q=queue.Queue()
cq=queue.Queue()
while i<len(li):
    q.put(li[i:i+4])
    i+=4

while q.qsize():
    cl=q.get()
    while i<len(cl):
        q.put(cl[i])