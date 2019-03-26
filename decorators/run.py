import time

def naive_timer(func, x, y):
    start_time = time.time()
    func(x, y)
    print('Time taken -- {}'.format(time.time() - start_time))

def functor_timer(func):
    def f(*args, **kwargs):
        print('inside functor...')
        start_time = time.time()
        res = func(*args, **kwargs)
        print('Time taken -- {}'.format(time.time() - start_time))
        return res
    return f

@functor_timer
def pow(x, y=10):
    print('in pow...')
    return x**y

def floor_div(x, y=5):
    print('in div...')
    return 0 if y==0 else x//y

if __name__ == '__main__':

    x = 10
    y = 3
    print('Power of {} and {} -- {}'.format(x, y, pow(x, y)))
    print('Floor division of {} and {} -- {}'.format(x, y, floor_div(x, y)))


    print('\nUsing naive wrapper function...')
    #naive_timer(pow, x, y)
    #naive_timer(floor_div, x, y)

    print('\nUsing functor to change definition of actual method(without decorator)...'\
        )
    print(pow(x, y))

