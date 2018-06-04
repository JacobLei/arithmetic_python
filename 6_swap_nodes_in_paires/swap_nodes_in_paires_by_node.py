# -*- coding: utf-8 -*-

# 通过交换两个节点来实现

class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

class Solution(object):

    def swap_pairs(self, head):
        if head != None and head.next != None:
            next = head.next
            head.next = self.swap_pairs(next.next)
            next.next = head
            return next
        return head

def print_list(head):
    p = head
    while p != None:
        print(p.value)
        p = p.next

if __name__ == '__main__':
    a = ListNode('a')
    b = ListNode('b')
    c = ListNode('c')
    d = ListNode('d')
    e = ListNode('e')

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    print_list(a)

    solution = Solution()

    print('after...')
    print_list(solution.swap_pairs(a))

