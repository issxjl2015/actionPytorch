import torch

# 构造一个 5 x 3 矩阵，不初始化
x1 = torch.empty(5, 3)
print(x1)

# 构造一个 5 x 3 随机初始化的矩阵
x2 = torch.rand(5, 3)
print(x2)

# 构造一个 5 x 3 全 0 矩阵，且数据类型为 long
x3 = torch.zeros(5, 3)
print(x3)

