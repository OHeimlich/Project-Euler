import itertools

__author__ = 'oheimlic'
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000
z=0
for x in xrange(1000):
    if x % 3==0 or x % 5 ==0:
        z+=x
print z


# Another solve
# print sum(x for x in xrange(1000) if not (x%3 and x%5))