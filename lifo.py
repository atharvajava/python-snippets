import queue

q=queue.LifoQueue() ## LIFO

for i in range(5):
    q.put(i)


while not q.empty():
    print(q.get(), end='   ')