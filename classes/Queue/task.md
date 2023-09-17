# LifoQueue and FifoQueue

The commonalities between the two classes should be inherited from a third class, `AbstractQueue`.

The two classes, `FifoQueue` and `LifoQueue`, should have the methods:
- `pop_element()`
- `add_element(element)`

## Method Descriptions

### pop_element()

This method should return and delete the corresponding element from the queue. If the queue is empty, it should return `None`.

### add_element(element)

This method should append a new element to the queue.

## Solutions
The content of the files "1st solution.py" and "2nd solution.py" are Python scripts that define three classes: `AbstractQueue`, `LifoQueue`, and `FifoQueue`.
They bot include a test case that creates a queue, adds some elements to it, and pops some elements from it.
`python 1st_solution.py` and `python 2nd_solution.py` should print the following output:
> Elements = [1, 2, 3]\
> LIFO:\
> 3\
> 2\
> 1\
> None\
> \
> Elements = [1, 2, 3]\
> FIFO:\
> 1\
> 2\
> 3\
> None

Here's a brief description of each class in both solutions:

### 1st Solution

- `AbstractQueue`: This is the base class for the other two classes. It initializes an empty list `__queue` and provides two methods:
  - `add_element(element)`: This method appends an element to the end of the queue.
  - `_list()`: This method returns the current state of the queue.

- `LifoQueue`: This class inherits from `AbstractQueue` and represents a Last-In-First-Out (LIFO) queue. It provides a method:
  - `pop_element()`: This method removes and returns the last element from the queue. If the queue is empty, it returns `None`.

- `FifoQueue`: This class also inherits from `AbstractQueue` and represents a First-In-First-Out (FIFO) queue. It provides a method:
  - `pop_element()`: This method removes and returns the first element from the queue. If the queue is empty, it returns `None`.

### 2nd Solution

- `AbstractQueue`: This is the base class for the other two classes. It initializes an empty list `__queue` and an index `__index`. It provides two methods:
  - `add_element(element)`: This method appends an element to the end of the queue.
  - `pop_element()`: This method removes and returns the element at index `__index` from the queue. If the queue is empty, it returns `None`.

- `LifoQueue`: This class inherits from `AbstractQueue` with `-1` as index, representing a Last-In-First-Out (LIFO) queue.

- `FifoQueue`: This class also inherits from `AbstractQueue` with `0` as index, representing a First-In-First-Out (FIFO) queue.

The main difference between these two solutions is how they implement LIFO and FIFO operations. The first solution uses separate classes with different implementations for popping elements, while the second solution uses a common implementation in the base class with different indices for LIFO and FIFO operations.