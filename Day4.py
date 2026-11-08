# try:
#     f=open('input.txt','r')
# except:
#     f=open('input.txt','w')
#
# try:
#     print(name)
# except NameError as e:
#     print("name未定义")
#     print(e)

# try:
#     print(name)
# except (NameError,ZeroDivisionError) as e:
#     print(e)

# try:
#     f=open('input.txt','r')
# except:
#     print('File not found')
# else:
#     print("yes")
# finally:
#     f.close()

# def func_1():
#     print("func_1")
#     1/0
#
# def func_2():
#     print("func_2")
#     func_1()
#
# def main():
#     try:
#         func_2()
#     except Exception as e:
#         print(e)
#
# main()


# import my_module
# print(my_module.test(1,2))

# from my_module import *
# test_b(3,4)
# test_A(1,2)

import json
list=[{"周杰伦":34,"林俊杰":45}]
list_json=json.dumps(list,ensure_ascii=False)
print(list_json)

list_1=json.loads(list_json)
print(list_1)