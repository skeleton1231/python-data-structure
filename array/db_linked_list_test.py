import unittest
from db_linked_list import DblLinkList

class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.dll = DblLinkList()

    def test_ListInsert(self):
        self.assertEqual(self.dll.ListInsert(1, 'apple'), True)
        self.assertEqual(self.dll.ListInsert(2, 'banana'), True)
        self.assertEqual(self.dll.ListInsert(3, 'orange'), True)
        self.assertEqual(self.dll.ListInsert(5, 'watermelon'), False)
        self.assertEqual(self.dll.ListLength(), 3)

    def test_list_delete(self):
        self.dll.ListDelete(1, 'apple')
        self.dll.ListDelete(2, 'banana')
        self.dll.ListDelete(3, 'orange')
        self.assertEqual(self.dll.ListDelete(2), True)
        self.assertEqual(self.dll.ListDelete(4), False)
        self.assertEqual(self.dll.ListLength(), 2)

    def test_get_elem(self):
        self.dll.ListInsert(1, 'apple')
        self.dll.ListInsert(2, 'banana')
        self.dll.ListInsert(3, 'orange')
        self.assertEqual(self.dll.get_elem(2), 'banana')
        self.assertEqual(self.dll.get_elem(4), None)

    def test_locate_elem(self):
        self.dll.ListInsert(1, 'apple')
        self.dll.ListInsert(2, 'banana')
        self.dll.ListInsert(3, 'orange')
        self.assertEqual(self.dll.locate_elem('banana'), 2)
        self.assertEqual(self.dll.locate_elem('watermelon'), -1)

    def test_length(self):
        self.dll.ListInsert(1, 'apple')
        self.dll.ListInsert(2, 'banana')
        self.dll.ListInsert(3, 'orange')
        self.assertEqual(self.dll.length(), 3)

    def test_empty(self):
        self.assertEqual(self.dll.empty(), True)
        self.dll.ListInsert(1, 'apple')
        self.assertEqual(self.dll.empty(), False)

if __name__ == '__main__':
    unittest.main()
