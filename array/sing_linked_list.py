from typing import Type

class Node(object):
    """链表结构的Node节点"""

    def __init__(self, data, next_node: Type['Node'] = None) -> None:
        """Node节点的初始化方法.
        参数:
            data:存储的数据
            next:下一个Node节点的引用地址
        """
        self.__data = data
        self.__next = next_node
    
    @property
    def data(self):
        """Node节点存储数据的获取.
        返回:
            当前Node节点存储的数据
        """
        return self.__data

    @data.setter
    def data(self, data):
        """Node节点存储数据的设置方法.
        参数:
            data:新的存储数据
        """
        self.__data = data
    
    @property
    def next_node(self):
        """获取Node节点的next指针值.
        返回:
            next指针数据
        """
        return self.__next
    
    @next_node.setter
    def next_node(self, data):
        """Node节点next指针的修改方法.
        参数:
            next:新的下一个Node节点的引用
        """
        self.__data =data

class SingleLinkedList(object):
    """单向链表"""

    def __init__(self) -> None:
        self.__head = Node(None)
    
    def find_by_value(self, value):
        """按照数据值在单向列表中查找.
        参数:
            value:查找的数据
        返回:
            Node
        """
        node = self.__head
        while node is not None and node.data != value:
            node = node.next_node
        return node

    def find_by_index(self, index):
        """按照索引值在列表中查找.
        参数:
            index:索引值
        返回:
            Node
        """
        node = self.__head
        pos = 0
        while node is not None and pos != index:
            node = node.next_node
            pos += 1
        return node
