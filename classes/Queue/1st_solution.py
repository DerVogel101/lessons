# Author: DerVogel101
# Github: https://github.com/DerVogel101
# Date: 15.09.2023
# Description: This is the first solution for the problem, described in task.md.

from typing import Any


class AbstractQueue:
    def __init__(self) -> None:
        self.__queue: list = []

    def add_element(self, element) -> None:
        """Adds an element to the queue.
        :param element: The element to add.
        """
        self.__queue.append(element)

    def _list(self) -> list:
        """Returns the queue. This method is protected. It should only be used by the subclasses."""
        return self.__queue


class LifoQueue(AbstractQueue):
    def __init__(self) -> None:
        """Initializes the queue."""
        super().__init__()

    def pop_element(self) -> Any:
        """Returns the last element of the queue.
        :return: The last element of the queue. If the queue is empty, None is returned."""
        try:
            return self._list().pop(-1)
        except IndexError:
            return None


class FifoQueue(AbstractQueue):
    def __init__(self) -> None:
        """Initializes the queue."""
        super().__init__()

    def pop_element(self) -> Any:
        """Returns the first element of the queue.
        :return: The first element of the queue. If the queue is empty, None is returned."""
        try:
            return self._list().pop(0)
        except IndexError:
            return None


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
