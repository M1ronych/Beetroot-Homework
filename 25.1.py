#Реалізація

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    class UnsortedList:
        def __init__(self):
            self.head = None
            self._size = 0

        def is_empty(self):
            return self.head is None

        def size(self):
            return self._size

#Добавляємо елемент в кінець списку

        def append(self,item):
            new_node = Node(item)

            if self.head is None:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node

            self._size += 1

#Повертаємо індекс першого входження елемента.Якщо елемент не знайдено - ValueError

        def index(self,item):
            current = self.head
            pos = 0

            while current:
                if current.data == item:
                    return pos
                current = current.next
                pos += 1

            raise ValueError(f"{item} is not in list")

#Без аргументу видаляє та повертає останній елемент. С аргументом видаляє елемент по індексу. pop(pos=None)

        def pop(self, pos=None):
            if self.is_empty():
                raise IndexError("Pop from empty list")

            if pos is None:
                pos = self._size - 1

            if pos < 0 or pos >= self._size:
                raise IndexError("Index out of range")

            current = self.head
            previous = None
            index = 0

            while index < pos:
                previous = current
                current = current.next
                index += 1

            if previous is None:
                self.head = current.next
            else:
                previous.next = current.next

            self._size -= 1
            return current.data

#Вставляємо елемент на вказану позицію

        def insert(self,pos,item):
            if pos < 0 or pos > self._size:
                raise IndexError("Index out of range")

            new_node = Node(item)

            if pos == 0:
                new_node.next = self.head
                self.head = new_node
            else:
                current = self.head
                index = 0

                while index < pos - 1:
                    current = current.next
                    index += 1

                new_node.next = current.next
                current.next = new_node

            self._size += 1

#Повертаємо новий UnsortedList. Елементи зі start включно, до stop не включно

        def slice(self,start,stop):
            if start < 0 or stop > self._size or start > stop:
                raise IndexError("Invalid slice indices")

            sliced = UnsortedList()
            current = self.head
            index = 0

            while current and index < stop:
                if index >= start:
                    sliced.append(current.data)
                current = current.next
                index += 1

            return sliced


#append,index,insert,pop,slice >>> O(n)


