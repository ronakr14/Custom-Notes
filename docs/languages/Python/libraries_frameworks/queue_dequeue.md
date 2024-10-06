# Python `queue` and `collections.deque` Modules: Detailed Overview and Examples

The `queue` and `collections.deque` modules in Python provide robust and efficient implementations of queues. Queues are data structures that follow the First-In-First-Out (FIFO) principle. While the `queue` module is specifically designed for multi-threaded programming, providing safe and synchronized queues, the `collections.deque` class from the `collections` module offers a more general-purpose, highly optimized double-ended queue.

## `queue` Module

The `queue` module includes several classes for creating various types of queues:

1. `Queue`: A FIFO queue.
2. `LifoQueue`: A Last-In-First-Out (LIFO) queue (stack).
3. `PriorityQueue`: A queue where items are sorted based on priority.

### Importing the `queue` Module

```python
import queue
```

### 1. FIFO Queue

#### Creating a FIFO Queue

```python
import queue

# Create a FIFO queue
q = queue.Queue()
```

#### Adding Items to the Queue

```python
# Add items to the queue
q.put("item1")
q.put("item2")
q.put("item3")
```

#### Removing Items from the Queue

```python
# Remove and return an item from the queue
item = q.get()
print(item)  # Output: item1

# Check if the queue is empty
print(q.empty())  # Output: False
```

### 2. LIFO Queue

#### Creating a LIFO Queue

```python
import queue

# Create a LIFO queue
lifo_q = queue.LifoQueue()
```

#### Adding and Removing Items

```python
# Add items to the LIFO queue
lifo_q.put("item1")
lifo_q.put("item2")

# Remove and return an item from the LIFO queue
item = lifo_q.get()
print(item)  # Output: item2
```

### 3. Priority Queue

#### Creating a Priority Queue

```python
import queue

# Create a priority queue
pq = queue.PriorityQueue()
```

#### Adding Items with Priority

Items are added as tuples with the priority as the first element.

```python
# Add items with priority to the queue
pq.put((1, "item1"))  # Priority 1
pq.put((3, "item3"))  # Priority 3
pq.put((2, "item2"))  # Priority 2
```

#### Removing Items Based on Priority

```python
# Remove and return the item with the highest priority (lowest priority number)
item = pq.get()
print(item)  # Output: (1, 'item1')
```

### Thread-Safety and Blocking Operations

The `queue` module provides thread-safe queues, which means they can be used safely in multi-threaded applications. Blocking operations allow threads to wait for items to be available in the queue.

```python
import queue
import threading
import time

def producer(q):
    for i in range(5):
        q.put(f"item {i}")
        print(f"Produced: item {i}")
        time.sleep(1)

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consumed: {item}")

q = queue.Queue()
producer_thread = threading.Thread(target=producer, args=(q,))
consumer_thread = threading.Thread(target=consumer, args=(q,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
q.put(None)  # Stop the consumer
consumer_thread.join()
```

## `collections.deque`

The `collections.deque` class provides a double-ended queue that supports adding and removing elements from both ends with O(1) time complexity.

### Importing the `collections` Module

```python
from collections import deque
```

### Creating a Deque

```python
# Create an empty deque
dq = deque()

# Create a deque with initial items
dq = deque(["item1", "item2", "item3"])
```

### Adding and Removing Items

#### Adding Items

```python
# Add items to the right end
dq.append("item4")

# Add items to the left end
dq.appendleft("item0")
```

#### Removing Items

```python
# Remove and return an item from the right end
item = dq.pop()
print(item)  # Output: item4

# Remove and return an item from the left end
item = dq.popleft()
print(item)  # Output: item0
```

### Iterating Over a Deque

```python
# Iterate over the deque
for item in dq:
    print(item)
```

### Other Deque Methods

#### Extending a Deque

```python
# Extend the deque with multiple items on the right end
dq.extend(["item4", "item5"])

# Extend the deque with multiple items on the left end
dq.extendleft(["item-1", "item-2"])
```

#### Rotating a Deque

```python
# Rotate the deque n steps to the right (positive) or left (negative)
dq.rotate(2)
print(dq)  # Output: deque(['item-1', 'item-2', 'item1', 'item2', 'item3', 'item4', 'item5'])

dq.rotate(-2)
print(dq)  # Output: deque(['item1', 'item2', 'item3', 'item4', 'item5', 'item-1', 'item-2'])
```

## Conclusion

The `queue` and `collections.deque` modules in Python provide powerful and flexible implementations of queues for various use cases. The `queue` module is particularly useful for multi-threaded programming, offering thread-safe and synchronized queues, including FIFO, LIFO, and priority queues. On the other hand, the `collections.deque` class is a highly efficient double-ended queue suitable for general-purpose use.

By leveraging these modules, you can efficiently manage data in a queue structure, handle concurrency with ease, and perform complex operations on sequences of items with optimal performance.