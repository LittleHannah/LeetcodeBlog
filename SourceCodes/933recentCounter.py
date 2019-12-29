'''
leetcode 933 最近的请求

题目说的是，在时间点 t 进行一次 ping 操作，加上之前在 [t-3000, t] 范围内的 ping 操作的次数，并将次数返回。
例如，例子中第一次 ping 的 t = 1， 返回 1；
第二次 ping 的 t = 100, 第一次 ping 的时间点 1 在本次允许范围 [100-3000, 100] 之内，所以返回2；
第三次 ping 时，前两次的 ping 都在允许范围[3000-3000, 3000] 之内，所以返回 3；
第四次 ping 时，第一次 ping 的 t = 1 不在允许范围[3002-3000, 3000] 之内，所以返回 3。
'''
# example input
inputs = [[],[1],[100],[3001],[3002]]
# example output
# [null,1,2,3,3]

from DataStructure import Queue
q = Queue()
def ping(t):
    q.addOne(t)
    if t - q.peek() > 3000 and q.length()>1:
        q.delOne()
    print('现在的队列为')
    q.show()
    return q.length()


solution = [ping(i[0]) if i != [] else 'null' for i in inputs]
print('最终结果为',solution)
