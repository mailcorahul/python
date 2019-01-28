""" Test program for docopt
Usage: run.py --name=<> <age>

Options:
  -h --help Test
"""
from docopt import docopt

if __name__ == '__main__':
    args = docopt(__doc__, version=0.1)
    print(args);
    if args['--name'] != 'raghul':
      option = input('Error');