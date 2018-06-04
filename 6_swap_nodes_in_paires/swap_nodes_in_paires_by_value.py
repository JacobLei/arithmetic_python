# -*- coding: utf-8 -*-

# ͨ�����������ڵ��ֵ��ʵ��

class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

class Solution(object):

    def swap_pairs(self, head):
        try:
            prev = head
            tail = prev.next
            while True:
                prev.value, tail.value = tail.value, prev.value
                prev = tail.next
                tail = prev.next        # ��Ϊ�����ڵ�ʱ��ִ��finally
        finally:
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
    solution.swap_pairs(a)

    print('after...')
    print_list(a)

