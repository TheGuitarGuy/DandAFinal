from queue import Queue
 
my_queue = Queue()

my_queue.put(123)

my_queue.put(124)

print(my_queue.get())
print(my_queue.get())