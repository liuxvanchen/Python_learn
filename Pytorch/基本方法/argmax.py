import torch

outputs=torch.tensor([[0.1,0.2],
                      [0.3,0.4]])

#沿x轴找谁大，输出位置（最大值下标
print(outputs.argmax(1))
preds=outputs.argmax(1)
targets=torch.tensor([0,1])
print((preds==targets).sum())