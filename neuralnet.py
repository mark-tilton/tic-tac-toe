import torch
import torch.nn as nn
import torch.nn.functional as F


class Net:

    def __init__(self):
        dtype = torch.float
        device = torch.device("cpu")
        ind = 9
        hd = 30
        od = 9
        self.w1 = torch.randn(ind, hd, device=device, dtype=dtype)
        self.w2 = torch.randn(hd, od, device=device, dtype=dtype)

    def forward(self, x):
        # Forward pass: compute predicted y
        h = x.mm(self.w1)
        h_relu = h.clamp(min=0)
        y_pred = h_relu.mm(self.w2)
        return y_pred

    def train(self, x, y):
        learning_rate = 1e-6
        for t in range(500):
            # Forward pass: compute predicted y
            h = x.mm(self.w1)
            h_relu = h.clamp(min=0)
            y_pred = h_relu.mm(self.w2)

            # Compute and print loss
            loss = (y_pred - y).pow(2).sum().item()
            if t % 100 == 99:
                print(t, loss)

            # Backprop to compute gradients of w1 and w2 with respect to loss
            grad_y_pred = 2.0 * (y_pred - y)
            grad_w2 = h_relu.t().mm(grad_y_pred)
            grad_h_relu = grad_y_pred.mm(w2.t())
            grad_h = grad_h_relu.clone()
            grad_h[h < 0] = 0
            grad_w1 = x.t().mm(grad_h)

            # Update weights using gradient descent
            w1 -= learning_rate * grad_w1
            w2 -= learning_rate * grad_w2

# net = Net()
# print(net)
# inp = torch.randn(1, 9)
# print(net(inp))
