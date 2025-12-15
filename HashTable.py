from turtle import TurtleScreen


class HashTable:
    def __init__(self,size=8):
        self._size = size
        self._table = [[] for _ in range(size)]
        self._count = 0

    def _hash(self,key):
        return hash(key) % self._size

    def put(self,key,value):
        index = self._hash(key)
        bucket = self._table[index]

        for i,(k,_) in enumerate(bucket):
            if k == key:
                bucket[i] = (key,value)
                return

        bucket.append((key,value))
        self._count += 1

    def get(self,key):
            index = self._hash(key)
            bucket = self._table[index]

            for k,v in bucket:
                if k == key:
                    return v

            raise KeyError(key)

    def __contains__(self,key):
        index = self._hash(key)
        bucket = self._table[index]

        for k, _ in bucket:
            if key == key:
                return True
            return False

    def __len__(self):
        return self._count

