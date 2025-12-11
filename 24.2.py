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

def is_balanced(sequence):
        s = Stack()
        pairs = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for ch in sequence:
            if ch in "([{":
                s.push(ch)
            elif ch in ")]}":
                if s.is_empty():
                    return False
                if s.pop() != pairs[ch]:
                    return False

        return s.is_empty()

def main():
    text = input("Enter a subsequence: ")

    if is_balanced(text):
        print("Balanced")
    else:
        print("Not balanced")

if __name__ == "__main__":
    main()
