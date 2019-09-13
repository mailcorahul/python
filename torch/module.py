import torch
import torch.nn as nn

class DebugModule(nn.Module):

    def __init__(self):        
        super().__init__()
        print(self._modules)

        ## every attribute assignment will invoke '__setattr__' inside 'nn.Module' and
        ## update its '_modules' attribute - an OrderedDict which contains
        ## ('attrname', module) as an entry
        self.linear = nn.Linear(20, 10)
        self.seq = nn.Sequential(
                    nn.Linear(20, 5),
                    nn.ReLU(inplace=True)
                    )
        print(self._modules)
        
        modules = self.__dict__['_modules']
        modules["gul"] = "asokan"
        print(self.__dict__)


    def forward(self, input):
        print('inside child forward')
        return self.seq(input)


if __name__ == '__main__':

    debug = DebugModule()
    input = torch.Tensor(20)
    print(input)

    ## every nn.Module object is callable(i.e has __call__ method)
    ## always call a nn.Module object instead of directly using forward method
    ## since __call__ takes care of invoking forward/backward hooks along with calling
    ## the module's forward method.
    output = debug(input)    
    print(output)