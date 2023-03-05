# 定义一个链表节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 创建一个虚拟头结点dummy，连接到原始头结点head
        dummy = ListNode(0, head)
        # 初始化slow指针为dummy节点
        slow = dummy
        # 初始化fast指针为头结点head
        fast = head
        # 遍历链表，直到到达链表的末尾
        while fast is not None:
            # 如果fast节点的值和下一个节点的值相等
            if fast.next is not None and fast.val == fast.next.val:
                # 跳过所有重复节点，直到找到不同的节点为止
                while fast.next is not None and fast.val == fast.next.val:
                    fast = fast.next
                # 将fast指向不同的节点
                fast = fast.next
                # 如果fast已经指向链表的末尾，将slow的next指向None
                if fast is None:
                    slow.next = None
            # 如果fast节点的值和下一个节点的值不相等
            else:
                # 将slow的next指向当前的fast节点
                slow.next = fast
                # 移动slow指针到当前的fast节点
                slow = slow.next
                # 移动fast指针到下一个节点
                fast = fast.next
        # 返回去重后的链表头节点
        return dummy.next
