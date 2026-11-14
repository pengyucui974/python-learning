import numpy as np
# array_1=np.array([1,2,3])
# # array_2=np.array([1.0,2,3])
# # print(array_1)
# # print(array_2)
# # array_1[1]=100.1
# # print(array_1)
# # array_2[1]=100
# # print(array_2)
# # array_3=array_1.astype(float)
# # print(array_3)
# print(array_1*1.0)
# # print(array_1//1+array_1)
# array_1=np.ones(3)
# array_2=np.ones((1,3))
# array_3=np.ones((1,1,3))
# print(array_1)
# print(array_2)
# print(array_3)
# print(type(array_1.shape))
# print(array_2.shape)
# print(array_3.shape)
#
# arr_1=np.arange(10)
# print(arr_1)
# arr_2=arr_1.reshape(2,-1)
# print(arr_2)
# arr_3=arr_2.reshape(-1)
# print(arr_3)

# arr_1=np.array([[1,2,3]])
# print(arr_1)
# arr_2=np.array([[[1,2,3]]])
# print(arr_2)
# arr_3=np.array([[1],[2],[3]])
# print(arr_3)
# arr_3=np.array([[1,2,3],[4,5,6]])
# print(arr_3)

# arr_1=np.arange(10)
# print(arr_1)
# arr_2=np.arange(10,20)
# print(arr_2)
# arr_3=np.arange(1,21,2)
# print(arr_3)

# arr_5=np.zeros((1,2,3))
# print(arr_5)
# print(arr_5.shape)

# arr_1=np.ones((2,3))*3.14
# print(arr_1)
# arr_1=np.random.random((2,3))#0-1均匀分布随机数
# print(arr_1)
# arr_2=np.random.random((2,3))*(100-40)+60
# print(arr_2)

# arr_3=np.random.randint(0,10,(2,3))#整数范围内随机数组
# print(arr_3)
# arr_3=np.random.normal(0,1,(2,3))#normal可以指定均值和标准差
# print(arr_3)
# arr_4=np.random.randn(2,3)#randn默认均值为0，标准差为1
# print(arr_4)

# arr_1=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr_1[2,2]==arr_1[2][2])
# arr_1[1,1]=30
# print(arr_1)

# arr_2=np.arange(20)+20
#
# print(arr_2[[2,6]])#普通索引用一层中括号，花式索引用两层中括号
# arr_3=np.arange(16).reshape(4,-1)
# print(arr_3)
# print(arr_3[[1,2],[3,2]])

# print(arr_3[0:3,0:3])
# print(arr_3[::2,::2])

# print(arr_3[1,:])
# print(arr_3[0:2,:])

# print(arr_3[:,1])
# print(arr_3[:,0:2])
# cut_1=arr_3[:,1]
# cut_1[0]=3000
# print(arr_3)
#
# cut_2=arr_3[:,2].copy()
# cut_2[0]=50000
# print(arr_3)

# arr_1=np.arange(11).reshape(1,-1)
# # arr_1=np.arange(11)
# # print(arr_1.T.shape)
# # print(arr_1.shape)
# arr_2=np.fliplr(arr_1)
# print(arr_2)
# arr_1=np.array([[1,2,3],[4,5,6]])
# arr_2=np.array([[1,2,3],[4,5,6]])
# arr_3=np.concatenate((arr_1,arr_2),axis=0)
# arr_4=np.concatenate((arr_1,arr_2),axis=1)
# print(arr_3)
# print(arr_4)

# arr_1=np.arange(10)
# arr_2,arr_3,arr_4=np.split(arr_1,[2,6])
# print(arr_2)

# arr_1=np.array([1,2,3])
# arr_2=np.arange(9).reshape(3,-1)
# print(arr_1)
# print(arr_2)
# print(arr_1*arr_2)
# arr_1=np.arange(5).reshape(1,-1)
# arr_2=np.arange(5).reshape(-1,1)
# print(arr_1@arr_2)
# print(np.dot(arr_1,arr_2))
# print(np.abs(arr_1))
# print(np.sin(arr_1))
# print(np.exp(arr_1))
# print(2**arr_1)
# print(np.log(arr_1[0,1:4])/np.log(2))

arr_1=np.random.random((2,3))
#
# print(arr_1)
#
# print(np.max(arr_1,axis=0))
# print(np.max(arr_1,axis=1))
# print(np.max(arr_1))
#
# print(np.sum(arr_1,axis=0))
# print(np.sum(arr_1,axis=1))
# print(np.sum(arr_1))
#
# print(np.mean(arr_1,axis=0))
# print(np.mean(arr_1,axis=1))
# print(np.mean(arr_1))
#
# print(np.std(arr_1,axis=0))
# print(np.std(arr_1,axis=1))
# print(np.std(arr_1))

# arr_2=(arr_1>0.5) |(arr_1<0.2)
# print(arr_2)

print(np.where(arr_1>0.5))