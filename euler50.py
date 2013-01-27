__author__ = 'liuminzhao'
import math

prime= [x for x in range(2,1000000) if not [t for t in range(2,int(math.sqrt(x))+1) if not x%t]]
prime2 = [x for x in range(2,1000) if not [t for t in range(2,int(math.sqrt(x))+1) if not x%t]]
# prime = [x for x in range(2,100) if not [t for t in range(2,int(math.sqrt(x))+1) if not x%t]]

term = 1000

#def ep50():
#        for i in range(term, 2, -1):
#            if not i%2:
#                if sum(prime[0:i]) in prime:
#                    return sum(prime[0:i])
#            else:
#                for j in range(1, len(prime)-i):
#                    a = sum(prime[j:(j+i)])
#                    if a in prime:
#                        return a
#            if i%100 == 0 :
#                print i
#
#print "ANSWER TO EULER PROJECT PROBLEM 50 is " , ep50()

##### from http://blog.dreamshire.com/2009/04/12/project-euler-problem-50-solution/
primes = prime
prime_sum = [0]
max = 1000000
sum = 0
count = 0
while (sum<max):
    sum+=primes[count]
    prime_sum.append(sum)
    count+=1

terms = 1
for i in range(count):
    for j in range(i+terms, count):
        n = prime_sum[j] - prime_sum[i]
        if (j-i>terms and n in prime):
            (terms,max_prime) = (j-i,n)

print "Answer to Problem 50 = ",max_prime," with ",terms," terms\n";