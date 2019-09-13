class Dunder():

    def __init__(self, name='None'):
        self.name = name

    def __repr__(self):
        print('this is a dunder class')

    def __len__(self):
        print('length is {}'.format(len(self.name)))


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
