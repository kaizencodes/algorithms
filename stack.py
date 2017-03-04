class Stack:

    def __init__(self):
        self.top = None

    def pop(self):
        if self.top is None:
            raise EmptyStackException('Can\'t pop empty stack')
        item = self.top.data
        self.top = self.top.next
        return item

    def push(self, item):
        node = _Node(item)
        node.next = self.top
        self.top = node

    def peek(self):
        if self.top is None:
            raise EmptyStackException('Can\'t peek empty stack')
        return self.top.data

    def is_empty(self):
        return self.top is None

    def __str__(self):
        if self.is_empty():
            return ''
        n = self.top
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


class EmptyStackException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


def main():
    s = Stack()
    print('\nEmpty stack')
    print('Expected: ')
    print('Result: ', s)

    print('\nPush 1, 2, 3')
    s.push(1)
    s.push(2)
    s.push(3)
    print('Expected: 3, 2, 1')
    print('Result: ', s)

    print('\nPeek')
    print('Expected: 3')
    print('Result: ', s.peek())

    print('\nPop')
    print('Expected: 2, 1')
    s.pop()
    print('Result: ', s)

    print('\nCheck emptiness')
    print('Expected: False')
    print('Result: ', s.is_empty())

    print('\nTry to pop when empty')
    print('Expected: Can\'t pop empty stack')
    try:
        s.pop()
        s.pop()
        s.pop()
    except EmptyStackException as e:
        print('Result: ', e)
    else:
        print('Result: no error occured')

    print('\nTry to peek when empty')
    print('Expected: Can\'t peek empty stack')
    try:
        s.peek()
    except EmptyStackException as e:
        print('Result: ', e)
    else:
        print('Result: no error occured')

    print('\nCheck emptiness')
    print('Expected: True')
    print('Result: ', s.is_empty())


if __name__ == "__main__":
    main()
