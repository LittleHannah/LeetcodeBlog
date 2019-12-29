'''
leetcode 21 合并两个有序链表

将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
'''

from DataStructure import linkedList, ListNode

l1 = linkedList()
l2 = linkedList()

# 测试样例一
# l2.initList([1,3,4])
# 测试样例二
l1.initList([1,2,4])
l2.initList([1,3,4])

def solution(l1, l2):
    tmp1 = l1.head
    tmp2 = l2.head
    l = linkedList()
    l.head = ListNode(-1)
    tmp = l.head
    if l1.isEmpty():
        print('yes')
        return l2.show()
    elif l2.isEmpty():
        return l1.show()
    else:
        while tmp1 is not None and tmp2 is not None:
            if tmp1.data < tmp2.data:
                tmp.next = tmp1
                tmp1 = tmp1.next
            else:
                tmp.next = tmp2
                tmp2 = tmp2.next
            tmp = tmp.next
    tmp = tmp2 if l1.isEmpty() else tmp1
    return l.show(1)

print('合并后的链表为', solution(l1, l2))
