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

x4 = torch.tensor([5.5, 3])
print(x4)

# 创建一个 tersor 基于已经存在的 tensor
x4 = x4.new_ones(5, 3, dtype=torch.double)

print(x4)

x5 = torch.randn_like(x4, dtype=torch.float)

print(x5)
# torch.Size 是一个元组，所以支持左右的元组操作
print(x5.size())

# 加法操作
y6 = torch.rand(5, 3)
print(x5 + y6)

# adds x5 to y6
"""
注意：任何使张量会发生变化的操作都有一个前缀 '_'
例如： x.copy_(y), x.t_() 将会改变
"""
y6.add_(x5)
print(y6)

# 改变大小：使用 torch.view
x7 = torch.randn(4, 4)
y7 = x7.view(16)
z7 = x7.view(-1, 8) # size 为 -1 表示大小由另一个维度来决定
print(x7.size(), y7.size(), z7.size())

# 有一个元素 tensor， 使用 .item() 来获取这个 value
x8 = torch.randn(1)
print(x8)
print(x8.item())