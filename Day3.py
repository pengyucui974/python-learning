# print('abd'>'abc')
# print('ab'>'a')
# print('a'>'A')
# print('key1'>'key2')

# def test_return():
#     return 1, 2
#
# x,y=test_return()
# print(x)
# print(y)

# def user_name(name,age,gender='man'):
#     print(name,age,gender)
#
# user_name("cpy",17,"woman")

# def user_func(*args):
#     print(args)
#
# user_func(1,2,3,4,5,6,7,8,9)
#
# def user_dict_func(**kwargs):
#     print(kwargs)
#
# user_dict_func(zhou=1,hang=2)
#
# def test_func(compute):
#     result=compute(1,2)
#     print(result)
#
# # def compute(x,y):
# #     return x+y
# test_func(lambda x,y:x+y)
# test_func(lambda x,y:x/y)
# test_func(lambda x,y:x*y)
#lambda函数为匿名函数

#文件操作：打开、关闭、读写
# f=open("text.txt",'r',encoding="utf-8")
# print(type(f))
# print(f.read(2))
# print(f.read())
# lines=f.readlines()
# print(type(lines))
# print(lines)

# line1 = f.readline()
# line2 = f.readline()
#
# print(line1)
# print(line2)

# for line in open('text.txt','r'):
#     print(line)

# f.close()
# time.sleep(10)

# with open('text.txt','r') as f:
#     content = f.read()
#     num=content.count('你好')
#     print(num)
#
#     #自动close
# f=open('text.txt','a',encoding='utf-8')
# f.write('\nhello')
# f.flush()
# f.close()
# with open('text.txt','r') as f:
#     print(f.read())

#homework
f=open('text.txt.bak','w')
for line in open('text.txt','r'):
    line_content = line.strip()
    if "正式" in line_content:
        f.write("\n)")
        f.write(line_content)
    else:
        continue
f.flush()
f.close()#写出文件调用close会自动flush,所以可以不用调用flush

