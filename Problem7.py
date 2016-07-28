# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
# ans=104743
__author__ = 'oheimlic'
import time
def prime(list,x):
    if x==0 or x==1:
        return False
    i=x*2
    while(i<len(list)-3):
        if list[i]%x==0:
            list[i]=0
        i+=x
    return True
mytime = time.time()
new=[]
primes=range(0,110000,1)
for num in primes:
    if prime(primes,num):
        new.append(num)
    if len(new)>10001:
        print new[10000]
        break
mytime= time.time() - mytime
print mytime
