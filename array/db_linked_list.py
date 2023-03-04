class DblNode:
    def __init__(self, data):
        self.data = data
        self.prior = None
        self.next = None
        
class DblLinkList:
    def __init__(self):
        self.m_head = DblNode(None)
        self.m_length = 0
        
    def ListInsert(self, i, e):
        if i < 1 or i > self.m_length + 1:
            print(f"插入位置{i}不合法，合法的位置是1到{self.m_length+1}之间!")
            return False
        
        p_curr = self.m_head
        for j in range(i-1):
            p_curr = p_curr.next
        
        new_node = DblNode(e)
        new_node.next = p_curr.next
        if p_curr.next != None:
            p_curr.next.prior = new_node
        p_curr.next = new_node
        new_node.prior = p_curr
        self.m_length += 1
        
        print(f"成功在位置{i}插入元素{e}!")
        return True
    
    def ListDelete(self, i):
        if self.m_length < 1:
            print("当前双链表为空，不能删除任何数据!")
            return False
        if i < 1 or i > self.m_length:
            print(f"删除的位置{i}不合法，合法的位置是1到{self.m_length}之间!")
            return False
        
        p_curr = self.m_head
        for j in range(i-1):
            p_curr = p_curr.next
        
        p_willdel = p_curr.next
        p_willdelNext = p_willdel.next
        p_curr.next = p_willdel.next
        if p_willdelNext != None:
            p_willdelNext.prior = p_curr
        
        print(f"成功删除位置为{i}的元素，该元素的值为{p_willdel.data}!")
        self.m_length -= 1
        del p_willdel
        return True
    
    def GetElem(self, i):
        if self.m_length < 1:
            print("当前双链表为空，不能获取任何数据!")
            return False
        if i < 1 or i > self.m_length:
            print(f"获取元素的位置{i}不合法，合法的位置是1到{self.m_length}之间!")
            return False
        
        p_curr = self.m_head
        for j in range(i):
            p_curr = p_curr.next
        
        e = p_curr.data
        print(f"成功获取位置为{i}的元素，该元素的值为{e}!")
        return True
        
    def LocateElem(self, e):
        p_curr = self.m_head
        for i in range(1, self.m_length+1):
            if p_curr.next.data == e:
                print(f"值为{e}的元素在双链表中第一次出现的位置为{i}!")
                return i
            p_curr = p_curr.next
        print(f"值为{e}的元素在双链表中没有找到!")
        return -1
    
    def ListLength(self):
        return self.m_length
    
    def Empty(self):
        if self.m_head.next == None:
            return True
        return False
    
    def DeleteGivenNode(self, node):
        if not node:
            print("Invalid input, node cannot be None.")
            return False
        
        if not node.prior: # Node to be deleted is the first node
            self.m_head = node.next
            if self.m_head:
                self.m_head.prior = None
        elif not node.next: # Node to be deleted is the last node
            node.prior.next = None
        else: # Node to be deleted is in the middle
            node.prior.next = node.next
            node.next.prior = node.prior
        
        self.m_length -= 1
        del node
        return True
