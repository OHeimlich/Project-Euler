"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
Ans == 142913828922
"""

import math
import time

primes = [2]


def is_prime(x):
    sqrt_x = int(math.sqrt(x))
    if x % 2 == 0:
        return False
    for num in range(1,sqrt_x+1,2):
        if num != 1:
            if x % num == 0:
                return False
    return True


def is_prime_2(x):
    for num in primes:
        if x % num == 0:
            return False
    return True


def main():
    num = 3
    max_prime = 2000000
    while num < max_prime:
        if is_prime(num):
            primes.append(num)
        num += 2
    print sum(primes)
start_time = time.time()
main()
print "{} seconds".format(time.time() - start_time)