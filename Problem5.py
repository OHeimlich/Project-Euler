# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# Ans= 232792560
# 0:00:11.695000
__author__ = 'oheimlic'
import datetime
mytime = datetime.datetime.now()
i=20
while(1):
    counter=0
    for n in range(20,10,-1):
        if i % n ==0:
            counter+=1
        else:
            break
    if counter == 10:
        print i
        break
    i+=20
print datetime.datetime.now() - mytime
