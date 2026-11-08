# list_1=[1,2,3]
# list_2=[]
# print(list_1)
# print(list_2)

# name_list=['Tom','Jack','Jane']
# print(name_list)
# print(type(name_list))
# name_list[-1]='Bob'
# print(name_list)
# name_list.insert(1,'William')
# print(name_list)
# name_list.append("Mack")
# print(name_list)
# my_list_2=[1,2,3]
# name_list.extend(my_list_2)
# print(name_list)
# del name_list[0]
# print(name_list)
# element = name_list.pop(0)
# print(name_list)
# print(type(element))
# name_list.remove('Jack')
# print(name_list)
# # name_list.remove('Jack')
# # print(name_list)
# a=name_list.count('Jack')
# print(a)
# count=len(name_list)
# print(count)
# name_list.clear()
# print(name_list)


# my_list=['Tom',666,True]
# print(my_list[0:3])
# print(type(my_list))
# c=my_list.index(667)
# print(c)
# print("\n")
#
# my_list=[[1,2,3],[4,5,6]]
# print(my_list[0][0])
# print(type(my_list))


#homework
# student_age=[21,25,21,23,22,20]
# student_age.append(31)
# list_1=[29,33,30]
# student_age.extend(list_1)
# element_1=student_age[0]
# print(element_1)
# element_2=student_age[-1]
# print(element_2)
# index=student_age.index(21)
# print(index)
# for i in student_age:
#     print(i)
# j=0
# print("\n")
# while j<len(student_age):
#     print(student_age[j])
#     j=j+1
#
# index=0
# while index<len(student_age):
#     print(student_age[index])
#     index=index+1


# list_2=[1,2,3,4,5,6,7,8,9,10]
# i=0
# new_list=[]
# while i<len(list_2):
#     if list_2[i]%2==0:
#         new_list.append(list_2[i])
#     i=i+1
# print(new_list)
#
# new_list_2=[]
# for j in list_2:
#     if j%2==0:
#         new_list_2.append(j)
# print(new_list_2)

#列表可以修改，但元组不可以修改

# tuple_1=(1,2,3)
# tuple_2=(1,True,'Tom')
# tuple_3=()
# tuple_4=('Tom')
# tuple_5=(1,)
# #定义还有一个元素的元组时，需要在后面加上一个单独的逗号，否则会蜕变为单个元素。
# print(tuple_1)
# print(tuple_2)
# print(tuple_3)
# print(type(tuple_1))
# print(type(tuple_4))
# print(type(tuple_5))

# tuple_6=((1,2,3),(4,4,5))
# print(tuple_6)
# print(tuple_6[1][2])
# count_1=tuple_6.count((1,2,3))
# len_1=len(tuple_6)
# print(len_1)
# print(count_1)
# print(tuple_6.index((1,2,3)))

# tuple_7=([0,1,2],2,3,4)
# index_1=0
# while index_1<len(tuple_7):
#     print(tuple_7[index_1])
#     index_1+=1
#
# for i in tuple_7:
#     print(i)
#
# tuple_7[0][1]=8

#homework
# tuple_1=("周杰伦",11,['football','music'])
# print(f"年龄所在的下标位置为{tuple_1.index(11)}")
# print(f"学生姓名为{tuple_1[0]}")
# del tuple_1[-1][0]
# tuple_1[-1].append('coding')
# print

#字符串不可以修改，除非建立新字符串
# name='Cuipengyu'
# print(name[0])
# print(name.index('peng'))
# name_2=name.replace('Cui','Da')
# print(name_2)
# list_1=name.split( )
# print(type(type(list_1)))

# name_2=name.strip("y")
# print(name_2)
# count_1=name.count('u')
# print(count_1)
# len_1=len(name)
# print(len_1)

# for i in name:
#     print(i)
#
# index=0
# while index<len(name):
#     print(name[index])
#     index+=1

#homework
# str_1="itheima itcast boxuegu"
# count_it=str_1.count("it")
# print(f"字符串中'it'出现了{count_it}次")
# str_2=str_1.replace(" ","/")
# print(str_2)
# list_1=str_2.split("/")
# print(list_1)

# my_list=[0,1,2,3,4,5,6]
# list_1=my_list[1:4]
# print(list_1)
#
# tuple_1=(0,1,2,3,4,5,6)
# result_2=tuple_1[:]
# print(result_2)

#
# str_1='cuipengyu'
# print(str_1[::2])

# str_2='01234567'
# print(str_2[3:1:-1])
# print(str_2[::-2])

#homework
# str_1="学python 来黑马程序员 月薪过万"
# str_2=str_1[::-1]
# print(str_2)
# print(str_2[9])
# print(str_2[9:4:-1])
# str_3=str_2.split(" ")
# str_4=str_3[1].replace("来","")
# print(str_4[::-1])

# set_1={1,2,3,'Tom','Jack'}
# set_2={1,1,1}
# print(set_1)
# print(set_2)
# set_3=set()
# print(set_3)
# set_3.add('Tom')
# print(set_3)
# set_3.remove('Tom')
# print(set_3)

# element=set_1.pop()
# print(element)
# print(set_1)
# set_1.clear()
# print(set_1)

# set_1={1,2,3}
# set_2={2,3,4}
# # set_3=set_1.difference(set_2)
# # print(set_3)
# # set_1.difference_update(set_2)
# # print(set_1)
# set_3=set_1.union(set_2)
# print(set_3)
#
# print(len(set_3))
#
# #集合不支持下标索引，所以不能用while循环遍历
#
# for i in set_3:
#     print(i)

#homework
# set_1=set()
# list_1=["黑马程序员", "传智播客", "黑马程序员", "传智播客", "itheima", "itcast", "itheima", "itcast","best"]
# for i in list_1:
#     set_1.add(i)
# print(set_1)

# dict_1={"王力宏":99, "周杰伦":98,"林俊杰":77}
# dict_2={}
# print(dict_1)
# print(dict_2)
# # dict_3={"王力宏":99, "周杰伦":98,"林俊杰":77,"林俊杰":79}
# # print(dict_3)
# print(dict_1["王力宏"])

# dict_4={"王力宏":{"语文":77,"数学":66,"英语":33},"周杰伦":{"语文":88,"数学":86,"英语":55},"林俊杰":{"语文":99,"数学":96,"英语":66}}
# print(dict_4)
# print(dict_4["王力宏"]["语文"])
# dict_4["王力宏"]["语文"]=100
# dict_4["王力宏"]["地理"]=100
# print(dict_4)
# element=dict_4["王力宏"].pop("地理")
# # print(element)
# # print(dict_4)
# # dict_4["王力宏"].clear()
# # print(dict_4)
# # print(dict_4.keys())
#
# for i in dict_4.keys():
#     print(dict_4[i])
#
# for key in dict_4:
#     print(dict_4[key])

#字典不能while循环
# num=len(dict_4)
# print(num)

#homework
# dict_1={"王力宏":{"部门":"科技部","工资":3000,"级别":1},
#         "周杰伦":{"部门":"市场部","工资":5000,"级别":2},
#         "林俊杰":{"部门":"市场部","工资":7000,"级别":3},
#         "张学友":{"部门":"科技部","工资":4000,"级别":1},
#         "刘德华":{"部门":"市场部","工资":6000,"级别":2},
#         }
#
# print(dict_1)
#
# for key in dict_1:
#     if dict_1[key]["级别"] == 1:
#         dict_1[key]["级别"] += 1
#         dict_1[key]["工资"] += 1000
#
# print(dict_1)

list_1=[1,2,9,4,5]
# print(max(list_1))
# print(min(list_1))
set_1=set(list_1)
# print(set_1)
# tuple_1=tuple(set_1)
# print(tuple_1)
# str_1=str(list_1)
# print(str_1)
# print(type(str_1))

a=sorted(set_1,reverse=True)
print(a)
#排序结果为list