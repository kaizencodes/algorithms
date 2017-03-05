class Queue:

    def __init__(self):
        self.first = None
        self.last = None

    def remove(self):
        if self.first is None:
            raise EmptyQueueException('Can\'t remove from empty queue')
        item = self.first.data
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return item

    def add(self, item):
        node = _Node(item)
        if self.last is not None:
            self.last.next = node
        self.last = node
        if self.first is None:
            self.first = self.last

    def peek(self):
        if self.first is None:
            raise EmptyQueueException('Can\'t peek empty queue')
        return self.first.data

    def is_empty(self):
        return self.first is None

    def __str__(self):
        if self.is_empty():
            return ''
        n = self.first
        result = str(n.data)
        while n.next is not None:
            n = n.next
            result += ', ' + str(n.data)
        return result


class _Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class EmptyQueueException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


def main():

    q = Queue()
    print('\nEmpty queue')
    print('Expected: ')
    print('Result: ', q)

    print('\nAdd 1, 2, 3')
    q.add(1)
    q.add(2)
    q.add(3)
    print('Expected: 1, 2, 3')
    print('Result: ', q)

    print('\nPeek')
    print('Expected: 1')
    print('Result: ', q.peek())

    print('\nRemove')
    print('Expected: 2, 3')
    q.remove()
    print('Result: ', q)

    print('\nCheck emptiness')
    print('Expected: False')
    print('Result: ', q.is_empty())

    print('\nTry to remove when empty')
    print('Expected: Can\'t remove from empty queue')
    try:
        q.remove()
        q.remove()
        q.remove()
    except EmptyQueueException as e:
        print('Result: ', e)
    else:
        print('Result: no error occured')

    print('\nTry to peek when empty')
    print('Expected: Can\'t peek empty queue')
    try:
        q.peek()
    except EmptyQueueException as e:
        print('Result: ', e)
    else:
        print('Result: no error occured')

    print('\nCheck emptiness')
    print('Expected: True')
    print('Result: ', q.is_empty())


if __name__ == "__main__":
    main()
