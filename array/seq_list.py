class SeqList:
    """
    Array Insert Find Delete Functions
    """

    def __init__(self, capacity: int) -> None:
        self._data = []  # list
        self._capacity = capacity

    def __getitem__(self, position: int) -> object:
        return self._data[position]

    def __setitem__(self, position: int, value: int) -> None:
        self._data[position] = value

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self):
        for item in self._data:
            yield item

    def find(self, position: int) -> object:
        try:
            return self._data[position]
        except IndexError:
            return None

    def delete(self, position: int) -> bool:
        try:
            self._data.pop(position)
            return True
        except IndexError:
            return False

    def insert(self, position: int, value: int) -> bool:
        if len(self) > self._capacity:
            return False
        return self._data.insert(position, value)

    def print_all(self):
        for item in self:
            print(item)


def test_seqlist():
    array = SeqList(10)
    array.insert(0, 3)
    array.insert(0, 4)
    array.insert(1, 5)
    array.insert(3, 9)
    array.insert(3, 10)
    array.insert(0, 100)
    array.print_all()


if __name__ == "__main__":
    test_seqlist()
