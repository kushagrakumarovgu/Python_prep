from time import time
import numpy as np
from functools import wraps

class ntimer:

    def __init__(self,n):
        self.n = n

    def __call__(self,func):
        self.func = func
        @wraps(self.func)
        def wrapper(*args,**kwargs):
            t_list = []
            for _ in range(self.n):
                start = time()
                res = self.func(*args,**kwargs)
                end = time()
                t_list.append(end - start)
            print("Execution time is: ",( np.mean(t_list) ))
            return res

        return wrapper


time_it = ntimer(1)