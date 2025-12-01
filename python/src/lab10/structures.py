from collections import deque

class Stack:
    def __init__(self):
        self._data = []
    def push(self, item):
        self._data.append(item)
    def pop(self):
        if self.is_empty:
            raise IndexError("Пустой Stack")
        return self._data.pop()
    def peek(self):
        if self.is_empty:
            return None
        return self._data[-1]
    def __len__(self):
        return len(self._data)
    @property
    def is_empty(self):
        return not self._data

class Queue:
    def __init__(self):
        self._data = deque()
    @property
    def is_empty(self):
        return not self._data
    def enqueue(self, item):
        self._data.append(item)
    def dequeue(self):
        if self.is_empty:
            raise IndexError("Пустая Queue")
        return self._data.popleft()
    def peek(self):
        if self.is_empty:
            return None
        return self._data[0]
    def __len__(self):
        return len(self._data)
