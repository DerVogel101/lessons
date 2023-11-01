# Author: DerVogel101
# Github: https://github.com/DerVogel101
# Date: 20.09.2023
# Description: This is the first solution for the problem, described in task.md.

from typing import Any


class AbstractQueue:
    def __init__(self) -> None:
        self.__queue: list = []
        self.__index: int = self.INDEX

    def add_element(self, element: Any) -> None:
        """Adds an element to the queue."""
        self.__queue.append(element)

    def pop_element(self) -> Any:
        """Returns the element"""
        try:
            return self.__queue.pop(self.__index)
        except IndexError:
            return None


class LifoQueue(AbstractQueue):
    INDEX = -1


class FifoQueue(AbstractQueue):
    INDEX = 0


if __name__ == '__main__':
    lifo = LifoQueue()
    lifo.add_element(1)
    lifo.add_element(2)
    lifo.add_element(3)

    print("Elements = [1, 2, 3]\nLIFO:")
    print(lifo.pop_element())
    print(lifo.pop_element())
    print(lifo.pop_element())
    print(lifo.pop_element())

    print()

    fifo = FifoQueue()
    fifo.add_element(1)
    fifo.add_element(2)
    fifo.add_element(3)

    print("Elements = [1, 2, 3]\nFIFO:")
    print(fifo.pop_element())
    print(fifo.pop_element())
    print(fifo.pop_element())
    print(fifo.pop_element())