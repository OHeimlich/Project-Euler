# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit
#  numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# ans= 906609
#0:00:01.025000


__author__ = 'oheimlic'
import datetime
mytime = datetime.datetime.now()
for x in range(999,100,-1):
    for y in range(999,100,-1):
        num=(x*y).__str__()
        digits=len(str(num))/2
        z= num[:digits] == num[:digits-1:-1] , num
        if z>max:
            max=z
print max[1]
print datetime.datetime.now() - mytime









