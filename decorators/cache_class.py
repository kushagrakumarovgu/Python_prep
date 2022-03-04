
#from functools import wraps
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