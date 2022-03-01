

from time import sleep, time
import random

# global will take care of both fib and fetch_data
# NOTE: fibo doesn't require global dict.
cache_dict = {}
def cache_it(func):
    global cache_dict
    #cache_dict = {}
    #print(cache_dict.keys())
    def wrapper(*args, **kwargs):
        try:
            #print(args[0])
            #print("calling ...",func.__name__)
            res = cache_dict[args[0]]
        except KeyError:
            res = func(*args,**kwargs)
            #print(res,args[0])
            cache_dict[args[0]] = res
            #print(cache_dict)
        
        return res
    
    return wrapper


def time_it(func):

    def wrapper(*args,**kwargs):
        print("calling...",func.__name__)
        start = time()
        res = func(*args,**kwargs)
        end = time()
        print(f"Excution time: {end - start}")
        return res
    
    return wrapper



@time_it
def fibo(num):
    a = 0
    b = 1
    fib_list = list()
    if num == 1:
        fib_list.append(a)
        #print(f"{a}")
        #return a
    elif num == 2:
        fib_list.extend(range(0,2))
        #print(f"{a} {b}")
    else:
        #print(f"{a} {b} ",end='')
        fib_list.extend(range(0,2))  
        for n in range(0,num-2):
            c = a + b
            fib_list.append(c)
            a = b
            b = c
    #sleep(random.uniform(0.1,5))
    return fib_list[0]


@time_it
@cache_it
def fetch_data(url):
    data = random.randint(1,1000000)
    sleep(random.uniform(0.1,5))
    return data

for num in [1, 5, 10, 15,100000 ]:
    fib = fibo(num)
    print(num, fib)

targets = [ "google.com", "reddit.com", "google.com", "google.com" ]
for url in targets:
    res = fetch_data(url)
    print(res)
            

@time_it
def fibo_top(num):
    return fibo_rec_nth(num)

@cache_it
def fibo_rec_nth(num):

    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        #sleep
        return fibo_rec_nth(num-1) + fibo_rec_nth(num-2)


for num in [1, 10, 20, 50 ]:
#for num in [498]:
    fib = fibo_top(num)
    print(num, fib)
