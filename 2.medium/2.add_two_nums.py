class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        tmp = res
        while l1 != None or l2 != None:
            if l2 == None: l2 = ListNode()
            if l1 == None: l1 = ListNode()
            tmp.val += l1.val + l2.val
            if not(l1.next == None and l2.next == None):
                tmp.next = ListNode()
            if tmp.val >= 10:
                tmp.val %= 10
                tmp.next = ListNode(1)

            tmp = tmp.next
            l1, l2 = l1.next, l2.next
        
        return res

l1 = ListNode(2, ListNode(4))
l2 = ListNode(5, ListNode(6))
l3 = Solution.addTwoNumbers(None, l1, l2)

while (l3.next != None):
    print(l3.val, end='')
    l3 = l3.next
print(l3.val)
