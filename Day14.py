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