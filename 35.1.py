import math
import time
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def is_prime(n:int) -> bool:
    if n < 2:
        return False
    if n in (2,3):
        return True
    if n % 2 == 0:
        return False

    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True

NUMBERS = [
    2,
    1099726899285419,
    1570341764013157,
    1637027521802551,
    1880450821379411,
    1893530391196711,
    2447109360961063,
    3,
    2772290760589219,
    3033700317376073,
    4350190374376723,
    4350190491008389,
    4350190491008390,
    4350222956688319,
    2447120421950803,
    5,
]

def filter_primes_sequential(numbers):
    start = time.perf_counter()
    primes = [n for n in numbers if is_prime(n)]
    return primes,time.perf_counter() - start

def filter_primes_threadpool(numbers):
    start = time.perf_counter()
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(is_prime,numbers))
    primes = [n for n,r in zip(numbers,results) if r]
    return primes,time.perf_counter() - start

def filter_primes_processpool(numbers):
    start = time.perf_counter()
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(is_prime,numbers))
    primes = [n for n,r in zip(numbers,results) if r]
    return primes,time.perf_counter() - start

if __name__ == "__main__":
    seq_primes,seq_time = filter_primes_sequential(NUMBERS)
    th_primes,th_time = filter_primes_threadpool(NUMBERS)
    pr_primes,pr_time = filter_primes_processpool(NUMBERS)

    print("Sequential:")
    print(seq_primes)
    print(f"Time:{seq_time:.4f} sec\n")

    print("ThreadPoolExecutor:")
    print(th_primes)
    print(f"Time: {th_time:.4f} sec\n")

    print("ProcessPoolExecutor:")
    print(pr_primes)
    print(f"Time: {pr_time:.4f} sec\n")

    print("All results equal:",
          seq_primes == th_primes == pr_primes)


