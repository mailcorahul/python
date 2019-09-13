class Dunder():

    def __init__(self, name='None'):
        self.name = name
        self.count = None

    def __repr__(self):
        print('this is a dunder class')

    def __len__(self):
        print('length is {}'.format(len(self.name)))

    def __setattr__(self, name, value):
        print(name, value)


if __name__ == '__main__':

    dunder = Dunder('dunder_tutorial')

    ##########################################################################
    ## dir method: attributes - list of variables and methods of an object ###
    ##########################################################################
    print(dir(dunder))

    
    ####################################################################################
    ## __dict__ attribute: a dictionary containing mapping of variables to its values ##
    ######                          for an object                                #######
    ####################################################################################
    print(dunder.__dict__)

    dunder.name = "raghul"
    dunder.count = 4