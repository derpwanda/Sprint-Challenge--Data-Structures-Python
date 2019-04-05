class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    pass

  def get(self):
    pass

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
If it is full SWAP with the oldest item in the queue.

GET
return the array
 """

""" What I know:
The empty array we start with has a size/length. The Nones are counted.
 """