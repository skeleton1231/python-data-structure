class StaticLinkList:
    class Node:
        def __init__(self):
            self.data = None
            self.next = -1

    def __init__(self):
        self.max_size = 1000
        self.data = [self.Node() for i in range(self.max_size)]
        self.head = -1
        self.free = 0
        for i in range(self.max_size - 1):
            self.data[i].next = i + 1
        self.data[self.max_size - 1].next = -1

    def malloc(self):
        if self.free == -1:
            return -1
        node_index = self.free
        self.free = self.data[self.free].next
        self.data[node_index].next = -1
        return node_index

    def free_node(self, index):
        self.data[index].next = self.free
        self.free = index

    def insert(self, index, data):
        if index < 0 or index >= self.max_size:
            return False
        node_index = self.malloc()
        if node_index == -1:
            return False
        self.data[node_index].data = data
        if index == 0:
            self.data[node_index].next = self.head
            self.head = node_index
        else:
            prev_index = self.get_node_index(index - 1)
            self.data[node_index].next = self.data[prev_index].next
            self.data[prev_index].next = node_index
        return True

    def delete(self, index):
        if index < 0 or index >= self.max_size or self.head == -1:
            return False
        if index == 0:
            node_index = self.head
            self.head = self.data[node_index].next
        else:
            prev_index = self.get_node_index(index - 1)
            if self.data[prev_index].next == -1:
                return False
            node_index = self.data[prev_index].next
            self.data[prev_index].next = self.data[node_index].next
        self.free_node(node_index)
        return True

    def get_node_index(self, index):
        if index < 0 or index >= self.max_size or self.head == -1:
            return -1
        node_index = self.head
        while index > 0 and node_index != -1:
            node_index = self.data[node_index].next
            index -= 1
        return node_index

    def get_data(self, index):
        node_index = self.get_node_index(index)
        if node_index == -1:
            return None
        return self.data[node_index].data

    def print_list(self):
        node_index = self.head
        while node_index != -1:
            print(self.data[node_index].data, end=' ')
            node_index = self.data[node_index].next
        print()
