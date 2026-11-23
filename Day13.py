# import sympy
# J,w=sympy.symbols("J,w")
# J=w**2
# print(J)
# dJ_dw=sympy.diff(J,w)
# print(dJ_dw)

#检查环境
# import numpy as np
# arr_1=np.array([[1, 2, 3], [4, 5, 6]])
# print(arr_1)


#检查GPU是否可用
# import torch

# print("MPS 是否可用：", torch.backends.mps.is_available())

# device = torch.device(
#     "mps" if torch.backends.mps.is_available() else "cpu"
# )
# print("当前计算设备：", device)

# # 直接在所选设备上创建两个矩阵
# a = torch.randn(1000, 1000, device=device)
# b = torch.randn(1000, 1000, device=device)

# # 矩阵乘法
# c = a @ b

# print("结果形状：", c.shape)
# print("结果所在设备：", c.device)

import torch

# x=torch.arange(12)
# print(x)
# print(x.shape)
# print(x.numel())

# x=x.reshape(3,-1)
# print(x)
# print(x.numel())

rand_para=torch.randn(3,4)
print(rand_para)

x=torch.tensor([[1,2,3],[4,5,6]])
print(x)