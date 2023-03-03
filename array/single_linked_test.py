import unittest

from sing_linked_list import SingleLinkedList

class TestSingleLinkedList(unittest.TestCase):

    def setUp(self):
        self.sll = SingleLinkedList()

    def test_insert_to_head(self):
        self.sll.insert_to_head(1)
        self.assertEqual(self.sll.find_by_value(1).data, 1)

    def test_insert_after(self):
        self.sll.insert_to_head(1)
        node1 = self.sll.find_by_value(1)
        self.sll.insert_after(node1, 2)
        self.assertEqual(self.sll.find_by_value(2).data, 2)

    def test_insert_before(self):
        self.sll.insert_to_head(1)
        node1 = self.sll.find_by_value(1)
        self.sll.insert_before(node1, 2)
        self.assertEqual(self.sll.find_by_value(2).data, 2)

    def test_delete_by_node(self):
        self.sll.insert_to_head(1)
        node1 = self.sll.find_by_value(1)
        self.sll.insert_after(node1, 2)
        node2 = self.sll.find_by_value(2)
        self.sll.delete_by_node(node2)
        self.assertIsNone(self.sll.find_by_value(2))

if __name__ == '__main__':
    unittest.main()
