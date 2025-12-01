class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self._last = None
        self._size = 0
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self._last = self.head
        else:
            self._last.next = Node(value)
            self._last = self._last.next
        self._size += 1
    def prepand(self, value):
        new_node = Node(value, self.head)
        if self._size == 1:
            self._last = self.head
        self.head = new_node
        self._size += 1
    def insert(self, idx, value):
        if idx < 0:
            raise IndexError("Индекс меньше нуля")
        if idx == 0:
            self.prepand(value)
            return
        if idx == self._size:
            self.append(value)
            return
        if idx > self._size:
            raise IndexError("Индекс больше длины коллекции")
        curr = self.head
        for _ in range(idx - 1):
            curr = curr.next
        new_node = Node(value, next=curr.next)
        curr.next = new_node
        self._size += 1
    def __iter__(self):
        curr = self.head
        while curr.next:
            yield curr.value
            curr = curr.next
    def __len__(self):
        return self._size
    def __str__(self):
        return " -> ".join(f"[{node}]" for node in self) + " -> None" if self.head else "None"
    def __repr__(self):
        vals = list(self)
        return f"SinglyLinkedList({vals})"
