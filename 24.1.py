class Stack:
    def __init__(self):
        self._data = []

    def push(self,item):
        self._data.append(item)

    def pop(self):
        if not self.is_empty():
            return self._data.pop()
        raise IndexError("pop from empty stack")

    def is_empty(self):
        return len(self._data) == 0

def reverse_input():
    s = Stack()
    text = input("Enter a string:")

    for ch in text:
        s.push(ch)

    reversed_text = ""
    while not s.is_empty():
        reversed_text += s.pop()

    print(reversed_text)

if __name__ == "__main__":
    reverse_input()

