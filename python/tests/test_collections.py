import pytest
from src.lab10.structures import Stack, Queue
from src.lab10.linked_list import SinglyLinkedList
import random

class TestStack:
    @pytest.mark.benchmark(group="Stack")
    def test_push(self, benchmark):
        def setup():
            s = Stack()
            return (s,), {}
        def push_operations(s):
            for i in range(1000):
                s.push(i)
        benchmark.pedantic(push_operations, setup=setup, rounds=50)
    @pytest.mark.benchmark(group="Stack")
    def test_pop(self, benchmark):
        def setup():
            s = Stack()
            for i in range(1000):
                s.push(i)
            return (s,), {}
        def pop_operations(s):
            for _ in range(1000):
                s.pop()
        benchmark.pedantic(pop_operations, setup=setup, rounds=50)
class TestQueue:
    @pytest.mark.benchmark(group="Queue")
    def test_enqueue(self, benchmark):
        def setup():
            q = Queue()
            return (q,), {}
        def enqueue_operations(q):
            for i in range(1000):
                q.enqueue(i)
        benchmark.pedantic(enqueue_operations, setup=setup, rounds=50)
    @pytest.mark.benchmark(group="Queue")
    def test_dequeue(self, benchmark):
        def setup():
            q = Queue()
            for i in range(1000):
                q.enqueue(i)
            return (q,), {}
        def dequeue_operations(q):
            for _ in range(1000):
                q.dequeue()
        benchmark.pedantic(dequeue_operations, setup=setup, rounds=50)

class TestWrongQueue:
    @pytest.mark.benchmark(group="WrongQueue")
    def test_wrong_enqueue(self, benchmark):
        def setup():
            q = WrongQueue()
            return (q,), {}
        def enqueue_operations(q):
            for i in range(1000):
                q.enqueue(i)
        benchmark.pedantic(enqueue_operations, setup=setup, rounds=50)
    @pytest.mark.benchmark(group="WrongQueue")
    def test_wrong_dequeue(self, benchmark):
        def setup():
            q = Queue()
            for i in range(1000):
                q.enqueue(i)
            return (q,), {}
        def dequeue_operations(q):
            for _ in range(1000):
                q.dequeue()
        benchmark.pedantic(dequeue_operations, setup=setup, rounds=50)

class TestSinglyLinkedList:
    @pytest.mark.benchmark(group="SinglyLinkedList")
    def test_append(self, benchmark):
        def setup():
            l = SinglyLinkedList()
            return (l,), {}
        def append_operations(l):
            for i in range(1000):
                l.append(i)
        benchmark.pedantic(append_operations, setup=setup, rounds=50)
    @pytest.mark.benchmark(group="SinglyLinkedList")
    def test_prepand(self, benchmark):
        def setup():
            l = SinglyLinkedList()
            return (l,), {}
        def prepand_operations(l):
            for i in range(1000):
                l.prepand(i)
        benchmark.pedantic(prepand_operations, setup=setup, rounds=50)

class WrongQueue:
    """
    Неправильная очередь на основе list для тестов и сравнения
    """
    def __init__(self):
        self._data = list()
    @property
    def is_empty(self):
        return not self._data
    def enqueue(self, item):
        self._data.append(item)
    def dequeue(self):
        if self.is_empty:
            raise IndexError("Пустая Queue")
        return self._data.pop(0)
    def peek(self):
        if self.is_empty:
            return None
        return self._data[0]
    def __len__(self):
        return len(self._data)
