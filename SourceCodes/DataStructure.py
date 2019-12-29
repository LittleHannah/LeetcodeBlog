# 栈
class Stack(object):
    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit


    def isEmpty(self):
        '''
        judge a stack is empty or not
        '''
        if len(self.stack) is 0:
            return True
        return False

    def push(self, data):
        if len(self.stack) >= self.limit:
            raise IndexError('No more room in this stack')
        self.stack.append(data)

    def pop(self):
        if self.isEmpty():
            raise IndexError('Can not pop from an empty stack')
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            raise IndexError('Can not peek from an empty stack')
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def show(self):
        print(self.stack)


# 链表

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self, head=None):
        self.head = head

    def initList(self, l):
        self.head = ListNode(l[0])
        tmp = self.head
        for i in l[1:]:
            node = ListNode(i)
            tmp.next = node
            tmp = tmp.next

    def length(self):
        tmp = self.head
        l = 0
        while tmp is not None:
            l = l+1
            tmp = tmp.next
        return l

    def append(self, newElement):
        cur = self.head
        if self.head:
            while cur.next:
                cur = cur.next
            cur.next = newElement
        else:
            self.head = newElement

    def isEmpty(self):
        return not self.head

    def insert(self, position, newElement):
        if position < 0 or position > self.length():
            raise IndexError('Link list index out of range')
        tmp = self.head
        if position == 0:
            newElement.next = tmp
            self.head = newElement
            return
        count = 0
        while count < position:
            pre = tmp
            tmp = tmp.next
            count += 1
        pre.next = newElement
        newElement.next = tmp


    def remove(self, position):
        if position < 0 or position > self.length()-1:
            raise IndexError('Link list index out of range')
        count = 0
        pre = None
        tmp = self.head
        while tmp is not None:
            if position == 0:
                self.head = tmp.next
                tmp.next = None
                return True
            pre, tmp = tmp, tmp.next
            count += 1
            if count == position:
                pre.next, tmp.next = tmp.next, None
                return True


    def show(self, pos=0):
        tmp = self.head
        ll = []
        while tmp is not None:
            ll.append(tmp.data)
            tmp = tmp.next
        return '->'.join([str(i) for i in ll[pos:]])

# 队列
class Queue(object):
    def __init__(self, limit=10):
        self.queue = []
        self.limit = limit

    def initList(self, l):
        self.queue = l

    def isEmpty(self):
        return len(self.queue) is 0

    def addOne(self, elem):
        self.queue.append(elem)

    def delOne(self):
        if self.isEmpty():
            raise IndexError('Can not del from an empty queue')
        self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            raise IndexError('Can not peek from an empty queue')
        return self.queue[0]

    def show(self):
        print('<-'.join([str(i) for i in self.queue]))

    def length(self):
        return len(self.queue)


# 树
class TreeNode(object):
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None
    def __str__(self):
        return self.item

class Tree(object):
    def __init__(self, treeRoot=None):
        self.root = treeRoot
    def add(self, treeNode):
        if self.root is None:
            self.root = treeNode
        else:
            q = [self.root]
            while True:
                popNode = q.pop(0)
                if popNode.left is None:
                    popNode.left = treeNode
                    return
                elif popNode.right is None:
                    popNode.right = treeNode
                    return
                else:
                    q.append(popNode.left)
                    q.append(popNode.right)
    def findParent(self, item):
        if self.root.item == item:
            return None
        q = [self.root]
        while q:
            popNode = q.pop(0)
            if popNode.left and popNode.left.item == item:
                return popNode
            if popNode.right and popNode.right.item == item:
                return popNode
            if popNode.left is not None:
                q.append(popNode.left)
            if popNode.right is not None:
                q.append(popNode.right)
        return None

    def delSon(self, item):
        if self.root is None:
            return False
        parent = self.findParent(item)
        if parent:
            delNode = parent.left if parent.left.item == item else parent.right
            if delNode.left is None:
                if parent.left.item == item:
                    parent.left = delNode.right
                else:
                    parent.left = delNode.right
                del delNode
                return True
            elif delNode.right is None:
                if parent.left.item == item:
                    parent.left = delNode.right
                else:
                    parent.left = delNode.right
                del delNode
                return True
            else:
                tmpPre = delNode
                tmpNext = delNode.right
                if tmpNext.left is None:
                    tmpPre.right = tmpNext.right
                    tmpNext.left = delNode.left
                    tmpNext.right = delNode.right
                else:
                    while tmpNext.left:
                        tmpPre = tmpNext
                        tmpNext = tmpNext.left
                    tmpPre.left = tmpNext.right
                    tmpNext.left = delNode.left
                    tmpNext.right = delNode.right
                if parent.left.item == item:
                    parent.left = tmpNext
                else:
                    parent.right = tmpNext
                del delNode
                return True
        else:
            return False

    def inOrder(self, node):
        if node is None:
            return []
        result = [node.item]
        leftItem = self.inOrder(node.left)
        rightItem = self.inOrder(node.right)
        return leftItem + result + rightItem

    def postOrder(self, node):
        if node is None:
            return []
        result = [node.item]
        leftItem = self.postOrder(node.left)
        rightItem = self.postOrder(node.right)
        return leftItem + rightItem +result

    def preOrder(self, node):
        if node is None:
            return []
        result = [node.item]
        leftItem = self.postOrder(node.left)
        rightItem = self.postOrder(node.right)
        return result + leftItem + rightItem

# 字典树
class TrieNode:
    def __init__(self):
        self.nodes = dict()
        self.isLeaf = False
    def insert(self, word: str):
        cur = self
        for char in word:
            if char not in cur.nodes:
                cur.nodes[char] = TrieNode()
            cur = cur.nodes[char]
        cur.isLeaf = True
    def insertMany(self, words: [str]):
        for word in words:
            self.insert(word)
    def search(self, word:str):
        cur = self
        for char in word:
            if char not in cur.nodes:
                return False
            cur = cur.nodes[char]

        return cur.isLeaf
