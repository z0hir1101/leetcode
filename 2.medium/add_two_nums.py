class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_nums(l1, l2):
    res = ListNode()
    cur = res
    while l1 or l2:
        if not l2: l2 = ListNode()
        if not l1: l1 = ListNode()
        cur.val += l1.val + l2.val

        if l1.next or l2.next:
            cur.next = ListNode()
        if cur.val >= 10:
            cur.val %= 10
            cur.next = ListNode(1)

        cur = cur.next
        l1, l2 = l1.next, l2.next
        return res


l1 = ListNode(2, ListNode(4))
l2 = ListNode(5, ListNode(6))
l3 = add_two_nums(l1, l2)

while (l3.next != None):
    print(l3.val, end='')
    l3 = l3.next
print(l3.val)
