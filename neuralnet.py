import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(9, 9)


    def forward(self, x):
        x = self.fc1(x)
        return x

# net = Net()
# print(net)
# inp = torch.randn(1, 9)
# print(net(inp))