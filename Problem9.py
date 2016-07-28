"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Ans:
abc = 31875000

Another solution:
a= 2mn; b= m^2 -n^2; c= m^2 + n^2;
a + b + c = 1000;

2mn + (m^2 -n^2) + (m^2 + n^2) = 1000;
2mn + 2m^2 = 1000;
2m(m+n) = 1000;
m(m+n) = 500;

"""
__author__ = 'oheimlic'

import math

for a in range(1000):
    for b in range(a,1000,1):
        if (a+b+(math.sqrt(a**2 + b**2))) == 1000:
            c = 1000 - a - b
            print "a = {0}, b = {1}".format(a,b)
            print "{0} + {1} = {2}".format(a**2, b**2, a**2 + b**2)
            print "a * b * c = {0}".format(a*b*c)

for n in range(500):
    for m in range(n+1, 500, 1):
        if m * (m+n) == 500:
            print "m: {0}, n: {1}".format(m, n)
            print "a: {}, b: {}, c:{} ".format(2*m*n, (m**2 - n**2), (m**2 + n**2))
