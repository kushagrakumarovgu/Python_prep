from cache_class import cache_it
from ntimer_class import ntimer, time_it
from time import sleep
import random

@cache_it
def fibo(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

@ntimer(3)
def nth_fib(n):
    return fibo(n)

@time_it
def fetch_data(url):
    data = random.randint(1,1000000)
    sleep(random.uniform(0.1,5))
    return data

# print(help(nth_fib))
# print(help(fibo))
# print(help(fetch_data))


for n in [5,10,30,50]:
    print(f"{n}th Fibonacci no. is {nth_fib(n)}")


targets = [ "google.com", "reddit.com", "google.com", "twitter.com" ]
for url in targets:
    res = fetch_data(url)
    print(f"data is: {res}")
