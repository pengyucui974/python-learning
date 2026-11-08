# class student:
    # name=None
    # age=None
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print("已完成类创建")
#
#     def say_hi(self):
#         print(self.name)
#         print(self.age)
#
#     def say_hi2(self,msg):
#         print(msg)
#
#
# stu_1=student("周杰伦",20)
# # stu_1.name="周杰伦"
# stu_1.age=20
# stu_1.say_hi()
# stu_1.say_hi2("hello")
# print(stu_1.name)

#homework
# class Student:
#     def __init__(self,name,age,address,idx):
#         self.name=name
#         self.age=age
#         self.address=address
#         print(f"学生{idx}信息录入完成,学生信息为[姓名：{self.name},年龄：{self.age},地址：{self.address}]")
#
# n=10
# stu=[]
# for i in range(1,n+1):
#     print(f"当前录入第{i}位学生信息，总共需要录入{n}位学生信息")
#     name = input("请输入学生姓名: ")
#     age = int(input("请输入学生年龄: "))
#     address = input("请输入学生地址: ")
#     stu.append(Student(name,age,address,i))


# class Student:
#     __gender="male"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def __str__(self):
#         return f"{self.name} is {self.age} years old, it's a {self.__gender}"

#     def __lt__(self,other):
#         return self.age<other.age
#
#     def __le__(self, other):
#         return self.age<=other.age
#
#     def __eq__(self, other):
#         return self.name==other.name
#
#     def __ageprint(self):
#         print(self.age)
# student=Student("周杰伦",19)
# # print(student.__gender)
# # student.__ageprint()
# print(student)
# # print(str(student))
# # student_2=Student("林俊杰",30)
# # print(student<student_2)

# class Phone:
#     __is_5g_enable=False
#     def __check_5g(self):
#         if self.__is_5g_enable:
#             print("5g开启")
#         else:
#             print("4g开启")
#
#     def call_by_5g(self):
#         self.__check_5g()
#         print("通话中")
#
# phone=Phone()
# phone.call_by_5g()
#
# class Phone2022(Phone):
#     Face_id=True
#     __is_5g_enable = True
#     def call_by_6g(self):
#         print("6g开启")
#
# phone2022=Phone2022()
# phone2022.call_by_5g()
#
# class Phone2023(Phone2022,Phone):
#     pass
# phone2023=Phone2023()
# phone2023.call_by_6g()
#
# class Phone:
#     producer="Huawei"
#     def call_by_5g(self):
#         print("父类的5g")
#
# class Phone2(Phone):
#     producer="Apple"
#     def call_by_5g(self):
#         print("子类的5g")
#         super().call_by_5g()
#         Phone().call_by_5g()
#
# phone=Phone2()
# phone.call_by_5g()
# print(phone.producer)
#
# var_1:list=[1,2,3]
# var_2:tuple=(1,2,3)
# var_3:str="123"
# var_4:int=10
# var_5:bool=True
#
# class Student:
#     pass
#
# stu:Student=Student()
#
# var_6:list[int]=[1,2,3]
# var_7:tuple[int,str,int]=(1,"2",3)
# print(type(var_7[1]))
#
# var_8=1 #type:int
# def func():
#     return 10
# var_9=func() #type:int

# def add(x:int,y:int) ->int:
#     return x+y
# print(add(1,2))
# add()
from typing import Union
my_list:list[Union[int,str]]=[1,'2',3]
my_dict:dict[str,Union[int,str]]={"name":"cpy","age":16}


def func(x:Union[int,str])->Union[int,str]:
    return x
print(func(1))



