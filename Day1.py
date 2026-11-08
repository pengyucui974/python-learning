# print("hello world")
# print("零基础，学python")
# 13.14
# name="hello world"
# print(len(name))
#
# def add(a,b):
#     return a+b
#
# print(add(1,2))
from tokenize import endpats

# count = 0
# for i in range(1,100):
#     count+=i
# print(f"count的值是{count}")

# def len1(a):
#     count=0
#     for i in a:
#         count+=1
#     return count
#
# # print(len1("endpats23"))
# name=None
# def say_hi():
#     """
#     该函数用于输出hi和hello
#     :return:
#     """
#     print("hi\nhello")
#
# result=say_hi()
# print(result)
# print(type(result))
#
# if result:
#     print("yes")
# else:
#     print("no")
#
# def add(a,b):
#     """
#     该函数用用于加法
#     :param a: 实数
#     :param b: 实数
#     :return: a+b
#     """
#     if a<b:
#         print(f"{a}+{b}的结果是")
#     else:
#         print("hhh")
#     return a+b
# # print(add(b=3,a=4))
# f=9
# def calculate(a,b,c):
#     d=add(a,b)
#     e=add(c,d)
#     global f
#     f=200
#     return e+f
# print(calculate(1,2,3))
# print(f)

money = 5000
name = None
def how_much():
    print(f"{name}的存款余额为{money}元")

def my_deposit(a):
    global money
    money += a
    print(f"已存款{a}元")
    return money

def my_withdraw(a):
    global money
    money -= a
    print(f"已取款{a}元")
    return money

def main_text():
    while True:
        print("请选择你需要的服务")
        print("查询余额\t请按1")
        print("存款\t\t请按2")
        print("取款\t\t请按3")
        print("退出\t\t请按4")
        func=input()
        if func == "1":
            how_much()
            continue
        elif func == "2":
            print("请输入存款金额")
            a=input()
            a=float(a)
            my_deposit(a)
            how_much()
        elif func == "3":
            print("请输入取款金额")
            a=input()
            a = float(a)
            my_withdraw(a)
            how_much()
        elif func == "4":
            break
        else:
            print("输入错误，请重来")

name=input("请输入你的姓名")
main_text()