
from time import time,sleep

class time_it:

    def __init__(self,func):
        self.func = func

    def __call__(self,*args,**kwargs):
        start = time()
        res = self.func(*args,**kwargs)
        end = time()
        print("Execution time is: ",( end - start ))

        return res



#obj = time_it(nth_fib)
#print("obj is: ",obj)

class cache_it:

    def __init__(self,func):
        self.func = func
        self.cache_dict = {}


    def __call__(self, *args,**kwds):
        try:
            res = self.cache_dict[args[0]]
        except KeyError:
            res = self.func(*args,**kwds)
            self.cache_dict[args[0]] = res
        
        return res

@cache_it
def fibo(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

@time_it
def nth_fib(n):
    return fibo(n)

for n in [5,10,30,50]:
    print(nth_fib(n))

