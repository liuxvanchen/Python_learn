import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# 生成随机数据
x_train = np.random.rand(100, 1) * 10  # 输入数据，100个样本，每个样本1个特征
y_train = 2 * x_train + 3 + np.random.randn(100, 1) * 0.5  # 输出数据，目标值

# 将数据转换为PyTorch张量
x_train = torch.tensor(x_train, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32)


# 定义模型
class LinearRegressionModel(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        return self.linear(x)


input_dim = x_train.shape[1]
output_dim = y_train.shape[1]
model = LinearRegressionModel(input_dim, output_dim)

# 定义损失函数和优化器
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 训练模型
num_epochs = 100
for epoch in range(num_epochs):
    # 前向传播
    outputs = model(x_train)
    loss = criterion(outputs, y_train)

    # 反向传播和优化
    optimizer.zero_grad()  # 清空梯度
    loss.backward()  # 反向传播，计算梯度
    optimizer.step()  # 更新权重

    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

    # 测试模型
with torch.no_grad():
    x_test = torch.tensor([[7.0]], dtype=torch.float32)
    y_pred = model(x_test)
    print(f'Predicted output for x=7: {y_pred.item()}')