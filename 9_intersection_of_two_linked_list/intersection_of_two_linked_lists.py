
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def node(l1, l2):
    len1, len2 = 0, 0
    l1_temp, l2_temp = l1, l2 
    while l1_temp:
        l1_temp = l1_temp.next
        len1 += 1
    while l2_temp:
        l2_temp = l2_temp.next
        len2 += 1
    if len1 > len2:
        for _ in range(len1 - len2):
            l1 = l1.next
    else:
        for _ in range(len2 - len1):
            l2 = l2.next
    while l1 and l2:
        if l1 == l2:
            return l1
        else:
            l1 = l1.next
            l2 = l2.next

def print_list(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()

if __name__ == '__main__':
    
    a0 = ListNode(1)
    a1 = ListNode(2)
    a2 = ListNode(3)
    a3 = ListNode(7)
    a4 = ListNode(9)
    a5 = ListNode(1)
    a6 = ListNode(5)

    b0 = ListNode(4)
    b1 = ListNode(5)

    a0.next = a1
    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5
    a5.next = a6
    
    b0.next = b1
    b1.next = a3

    print_list(a0)
    print_list(b0)

    print(node(a0, b0).val)

