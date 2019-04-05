class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # current = current % capcity
    # if i is None, pop(current), insert(current,item), current =+ 1.
    index_tracker = self.current % self.capacity
    storage = self.storage
  
    print(index_tracker)

    storage.pop(index_tracker)
    storage.insert(index_tracker, item)
    self.current += 1


  def get(self):
    # remove Nones from list, then return
    # for i in self.storage:
    #   if self.storage[i] == None:
    #     self.storage.pop(i)
    return print(self.storage)

""" What is a Ring Buffer?
A ring buffer is also known as a circular buffer. 
It is FIXED in size.
It's a queue FIFO.
 """

""" What do we want?
APPEND
If our buffer is filled, we want the newest element to OVERWRITE the oldest element. 

  1. [a, b, c, d], add element(e), now array is [e, b, c, d]
  2. [e, b, c, d], add elemtent(f), now array is [e, f, c, d]

So if an element array is None pop/append like a normal queue.
Add to the list front to back by pop(current)/insert(current, item).
  I'll need to utilized modulo (%)
If it is full SWAP with the oldest item in the queue. (%)

GET
return the array without the Nones.
 """

""" What I know:
The empty array we start with has a size/length. The Nones are counted.
 """

buffer = RingBuffer(3)

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()        # should return ['a', 'b', 'c']

buffer.append('d')  # directly replaces 'a' 

buffer.get()        # should return ['d', 'b', 'c']

buffer.append('e')  # directly replaces 'b'
buffer.append('f')  # directly replaces 'c'

buffer.get()        # should return ['d', 'e', 'f']

buffer.append('g')

buffer.get()