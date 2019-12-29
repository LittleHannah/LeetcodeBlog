'''
leetcode 20 有效的括号

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
'''

from DataStructure import Stack

left = ['[', '(', '{']
right = [']', ')', '}']
str = '(]'
def solution(str):
    mystack = Stack()
    for s in str:
        if s in left:
            mystack.push(s)
        if s in right:
            if mystack.size() is 0:
                return False
            if right.index(s) == left.index(mystack.peek()):
                mystack.pop()
            else:
                return False
    return mystack.isEmpty()

print('括号可以匹配' if solution(str) else '括号不能匹配')
