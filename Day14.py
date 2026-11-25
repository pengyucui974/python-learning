# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         volume = []
#         len_list = len(height)
#         for i in range(len_list):
#             for j in range(i + 1, len_list):
#                 volume.append(min([height[j] , height[i]]) * (j - i))
#
#         return max(volume)
#
# sol=Solution()
# # height=[1,8,6,2,5,4,8,3,7]
# height = [1,1]
# print(sol.maxArea(height))

# import math
# print(math.factorial(52)/(math.factorial(5)*math.factorial(52-5)))
#
# print(math.comb(52,5))

# def test1():
#     l=[]
#     for i in range(1000):
#         l=l+[i]
#
# def test2():
#     l=[]
#     for i in range(1000):
#         l.append(i)
#
# def test3():
#     l = [i for i in range(1000)]
#
# def test4():
#     l = list(range(1000))
#
# import timeit
# t1=timeit.Timer(test1)
# print(t1.timeit(number=1000))
# t2=timeit.Timer(test2)
# print(t2.timeit(number=1000))
# t3=timeit.Timer(test3)
# print(t3.timeit(number=1000))
# t4=timeit.Timer(test4)
# print(t4.timeit(number=1000))
# x = list(range(20000))
# def test5():
#     x.pop()
#
# def test6():
#     x.pop(0)
#
# import timeit
# t1=timeit.Timer("test5()","from __main__ import test5")
# print(t1.timeit(10000))
# t2=timeit.Timer("test6()","from __main__ import test6")
# print(t2.timeit(10000))

# import timeit
# import random
#
# for i in range(10000,1000001,20000):
#     t=timeit.Timer("random.randrange(%d) in x" % i,"from __main__ import random, x")
#     x=list(range(i))
#     lst_time=t.timeit(number=1000)
#     x={j:None for j in range(i)}
#     d_time=t.timeit(number=1000)
#     print(d_time)

class Stack(object):
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def isEmpty(self):
        return self.stack == []
    def size(self):
        return self.stack.__len__()

# s=Stack()
# print(s.isEmpty())
# s.push(1)
# print(s.isEmpty())
# s.pop()
# print(s.isEmpty())

#括号匹配检测
def parchecker(symbolString):
    s=Stack()
    balanced = True
    item=0
    while item<len(symbolString) and balanced:
        if symbolString[item]=="(":
            s.push(symbolString[item])
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        item+=1
    if s.isEmpty() and balanced:
        return True
    else:
        return False

#十进制转二进制
def tentotwo(integer):
    s=Stack()
    while integer//2!=0 or integer%2:
        s.push(integer%2)
        integer//=2
    binstring=""
    while not s.isEmpty():
        binstring+=str(s.pop())
    return binstring
# print(tentotwo(10))
# print(tentotwo(100))

#十进制转其他
def tentoAll(integer,index):
    s=Stack()
    while integer//index!=0 or integer%index!=0:
        s.push(integer%index)
        integer//=index
    binstring=""
    while not s.isEmpty():
        binstring+=str(s.pop())
    return binstring
# print(tentotwo(10))
# print(tentotwo(100))

# print(tentoAll(10, 8))
# print(tentoAll(100, 8))


def middletoBackward(string):
    middle_process=Stack()
    outcome=[]
    symbol_dict={"(":1,"+":2,"-":2,"*":3,"/":3,")":3}
    while string:
        if string[0] in symbol_dict:
            if string[0]=="(":
                middle_process.push(string[0])
            elif string[0]==")":
                Flag=True
                while Flag:
                    para=middle_process.pop()
                    if para=="(":
                        Flag=False
                    else:
                        outcome.append(para)
            else:
                if middle_process.isEmpty():
                    middle_process.push(string[0])
                else:
                    while not symbol_dict[middle_process.peek()]<symbol_dict[string[0]]:
                        outcome.append(middle_process.pop())
                        if middle_process.isEmpty():
                            break
                    middle_process.push(string[0])
        else:
            outcome.append(string[0])
        string=string[1:]
    while not middle_process.isEmpty():
        outcome.append(middle_process.pop())
    return "".join(outcome)

# print(middletoBackward("a-b*c-d"))
