import threading
import time

def sleeper(n , name):
    print('Hi I am {}. Going to sleep for 5 secs'.format(name))
    time.sleep(n)
    print('{} has woken up from '.format(name))

t = threading.Thread(target=sleeper, name='thread1', args = (5, 'thread1'))
t.start()
t.join()

print('hello')
print('hello')