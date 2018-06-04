#-*- coding: utf-8 -*-

class NodeList(object):

    def __init__(self, value):
        self.val = value
        self.next = None

def print_list(head):
    p = head
    while p is not None:
        print(p.val)
        p = p.next
# 非递归解法
def merge_lists(l1, l2):
    if l1 is None and l2 is None:
        return None
    new_list = NodeList(0)
    pre = new_list
    while l1 is not None and l2 is not None:
        if l1.val <= l2.val:
            pre.next = l1
            l1 = l1.next
        else:
            pre.next = l2
            l2 = l2.next
        pre = pre.next
    if l1 is not None:
        pre.next = l1
    else:
        pre.next = l2
    return new_list.next

# 递归解法
def merge_lists_recursion(l1, l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    else:
        if l1.val <= l2.val:
            l1.next = merge_lists_recursion(l1.next, l2)
            return l1
        else:
            l2.next = merge_lists_recursion(l1, l2.next)
            return l2

def merge_lists_quickly(l1, l2):
    new_list = NodeList(0)
    new_list.next = l1
    pre, head_of_l1, head_of_l2 = new_list, l1, l2
    while head_of_l2:
        if not head_of_l1:
            pre.next = head_of_l2
            break;
        if head_of_l1.val > head_of_l2.val:
            temp = head_of_l2
            head_of_l2 = head_of_l2.next
            pre.next = temp
            temp.next = head_of_l1
            pre = pre.next
        else:
            pre, head_of_l1 = pre.next, head_of_l1.next
    return new_list.next

if __name__ == '__main__':
    a = NodeList(1)
    b = NodeList(2)
    c = NodeList(3)
    d = NodeList(4)
    e = NodeList(5)
    f = NodeList(6)

    a.next = c
    c.next = e

    b.next = d
    d.next = f

    print_list(a)
    print_list(b)

#    print('============= merge_lists============')
#    print_list(merge_lists(a, b))


#    print('============= merge_lists_recursion============')
#    print_list(merge_lists_recursion(a, b))


    print_list(merge_lists_quickly(a, b))
