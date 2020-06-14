"""Script to profile cpu memory usage during inference for PyTorch."""
import os
import argparse

import torch
import torch.nn as nn
import torchvision.models as models
import psutil

parser = argparse.ArgumentParser()
parser.add_argument('--use-class', action="store_true", help="forward pass inside a module class")
args = parser.parse_args()


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = models.resnet50()

    def forward(self, x):
        return self.model(x)


if args.use_class:
    model = Net()
else:
    model = models.resnet50()
x = torch.randn(2, 3, 224, 224)

process = psutil.Process(os.getpid())
for idx in range(100):
    print(idx, process.memory_full_info().rss / 1024**2)
    with torch.no_grad():
        out = model(x)