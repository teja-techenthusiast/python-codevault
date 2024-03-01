# Data Structures in Python

This repository contains implementations of various data structures in Python, including a doubly linked list, deque, queue, and stack.

## Doubly Linked List (_DoublyLinkedList)

The `_DoublyLinkedList` class provides a basic implementation of a doubly linked list, which supports insertion, deletion, and traversal operations.

## LinkedDeque (LinkedDeque)

`LinkedDeque` extends the `_DoublyLinkedList` class to implement a deque (double-ended queue) with operations for adding/removing elements from both ends.

## LinkedQueue (LinkedQueue)

`LinkedQueue` implements a queue using a singly linked list, providing operations for enqueueing and dequeueing elements.

## LinkedStack (LinkedStack)

`LinkedStack` implements a stack using a singly linked list, supporting push, pop, and top operations.

## Usage

To use these data structures, import the respective classes into your Python code and instantiate them as needed. Here's an example:

```python
from linked_deque import LinkedDeque
from linked_queue import LinkedQueue
from linked_stack import LinkedStack

def main():
    # Create instances of data structures
    my_linked_deque = LinkedDeque()
    my_linked_queue = LinkedQueue()
    my_linked_stack = LinkedStack()

    # Perform operations
    my_linked_deque.insert_first(10)
    my_linked_deque.insert_last(20)
    print(my_linked_deque.first())  # Output: 10

    my_linked_queue.enqueue(30)
    print(my_linked_queue.dequeue())  # Output: 30

    my_linked_stack.push(40)
    print(my_linked_stack.pop())  # Output: 40

if __name__ == "__main__":
    main()
