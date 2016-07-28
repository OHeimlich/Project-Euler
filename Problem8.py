# The four adjacent digits in the 1000-digit number that have the greatest product are 9 x 9 x 8 x 9 = 5832.
#
# 73167176531330624919225119674426574742355349194934
# 96983520312774506326239578318016984801869478851843
# 85861560789112949495459501737958331952853208805511
# 12540698747158523863050715693290963295227443043557
# 66896648950445244523161731856403098711121722383113
# 62229893423380308135336276614282806444486645238749
# 30358907296290491560440772390713810515859307960866
# 70172427121883998797908792274921901699720888093776
# 65727333001053367881220235421809751254540594752243
# 52584907711670556013604839586446706324415722155397
# 53697817977846174064955149290862569321978468622482
# 83972241375657056057490261407972968652414535100474
# 82166370484403199890008895243450658541227588666881
# 16427171479924442928230863465674813919123162824586
# 17866458359124566529476545682848912883142607690042
# 24219022671055626321111109370544217506941658960408
# 07198403850962455444362981230987879927244284909188
# 84580156166097919133875499200524063689912560717606
# 05886116467109405077541002256983155200055935729725
# 71636269561882670428252483600823257530420752963450
#Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
#  What is the value of this product?
#ans=23514624000
__author__ = 'oheimlic'
import time

def sumOfPro(list):
    sum=1
    for x in list:
        sum*=int(x)
    return sum
thenum="731671765313306249192251196744265747423553491949349698352031277450632623957831801698480186947" \
"88518438586156078911294" \
"94954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950" \
"4452445231617318564030" \
"98711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077" \
"2390713810515859307960866" \
"7017242712188399879790879227492190169972088809377665727333001053367881220235421809751254540594752243525849077116705" \
"560136048395864467063244157221553975369781797784617406495514929086256932197846862248283972241375657056057490261407" \
"97296865241453510047482166370484403199890008895243450658541227588666881164271714799244429282308634656748139191231" \
"628245861786645835912456652947654568284891288314260769004224219022671055626321111109370544217506941658960408071984" \
"038509624554443629812309878799272442849091888458015616609791913387549920052406368991256071760605886116467109405077" \
"54100225698315520005593572972571636269561882670428252483600823257530420752963450"
mytime = time.time()
max=0
i=0
for x in thenum:
    if (thenum[i:i + 13].__str__()).__contains__('0'):
        i+=1
        continue
    s=sumOfPro(thenum.__str__()[i:i + 13])
    if s>max:
        max=s
        #list=new[i:i+13]
    i+=1
mytime= time.time() - mytime
print(max)
print mytime