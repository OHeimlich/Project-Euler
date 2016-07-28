__author__ = 'oheimlic'
import math
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

num=600851475143
while(1):
    temp=num
    i=1
    while(i<= math.sqrt(num)):
        i+=1
        if num % i ==0:
            num/=i
            break
    if temp == num:
        print num
        break


