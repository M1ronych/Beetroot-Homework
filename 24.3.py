class Stack:
    def __init__(self):
        self._data = []

    def push(self,item):
        self._data.append(item)

    def pop(self):
        if not self._data:
            raise IndexError("Pop from empty stack")
        return self._data.pop()

    def get_from_stack(self,e):
        temp_stack = []
        found = None

        while self._data:
            item = self.pop()
            if item == e and found is None:
                found = item
                break
            temp_stack.append(item)

        while temp_stack:
            self.push(temp_stack.pop())

        if found is None:
            raise ValueError(f"Element {e} is not be found in stack")

        return found

    class Queue:
        def __init__(self):
            self._data = []

        def enqueue(self,item):
            self._data.append(item)

        def dequeue(self):
            if not self._data:
                raise IndexError("Dequeue from empty queue")
            return self._data.pop(0)

        def get_from_queue(self,e):
            size = len(self._data)
            found = None

            for _ in range(size):
                item = self.dequeue()
                if item == e and found is None:
                    found = item
                else:
                    self.enqueue(item)

            if found is None:
                raise ValueError(f"Element {e} is not be found in queue")

            return found

        