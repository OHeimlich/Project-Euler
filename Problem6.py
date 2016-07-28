# The sum of the squares of the first ten natural numbers is,
#
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# ans= 25164150

__author__ = 'oheimlic'
sum1=0
sum2=0
for i in xrange(101):
    sum1+= i**2
print abs(((100*(1+100))/2)**2-sum1)