import sys

import torch
import torchvision.models as models
import torch.nn as nn
import cv2
import numpy as np

class Resnet18WithFwdHook(nn.Module):

    def __init__(self):
        super().__init__()
        # define resnet18 module
        self.net = models.resnet18(pretrained=True)
        # register forward hook for conv1 output from layer3 of the network
        self.module_to_vis = self.net._modules['layer3']._modules['0']._modules['relu']
        self.remove_handle = self.module_to_vis.register_forward_hook(self.visualize)

    def visualize(self, module, input, output):
        print(module)
        print(output.size())
        for idx in range(output.size(1)):
            torch_image = output[0][idx]*255
            #print(torch.min(torch_image), torch.max(torch_image))
            cv2.imwrite('/tmp/vis/{}.png'.format(idx), torch_image.detach().numpy())

    def forward(self, input):
        return self.net(input)


if __name__ == '__main__':
    
    r18 = Resnet18WithFwdHook()
    input_image = cv2.imread(sys.argv[1])
    #input_image.shape = (input_image.shape[2], input_image.shape[0], input_image.shape[1])
    input_image = np.transpose(input_image, (2, 0, 1))
    input_image = torch.tensor(input_image[None], dtype=torch.float32)
    r18(input_image)