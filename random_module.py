import random
import math

a = random.seed()
b = random.random()
print(b)
c = random.uniform(21.2,12.2)
print(c)

#Returns a value between 0 and 1 from the Beta distribution. alpha > -1 and beta >-1.
m = random.betavariate(alpha= 3, beta=3.4)
print("betavariate:", c)

#Circular uniform distribution. mean is the mean angle, and arc is the range of the distribution, centered around the mean angle. Both of these values must be specified in
#radians in the range between 0 and pi. Returned values are in the range (mean
#- arc/2, mean + arc/2).
#n = cunifvariate(mean= 2.2, arc= 1.4)
#print(n)

#Exponential distribution. lambd is 1.0 divided by the desired mean. Returns values in the range [0, +Infinity)
o = random.expovariate(lambd= 4)
print("expovariate:", o)

#Gamma distribution. alpha > -1, beta > 0
p = random.gammavariate(alpha=3, beta=3.4)
print("gammavariate:", p)

#Gaussian distribution with mean mu and standard deviation sigma. Slightly faster than
#normalvariate().
q = random.gauss(mu=32, sigma=3)
print("gauss:", q)

#Log normal distribution.Taking the natural logarithm of this distribution results in a
#normal distribution with mean mu and standard deviation sigma.
r = random.lognormvariate(mu=3, sigma=32)
print("lognormvariate:", r)

#Normal distribution with mean mu and standard deviation sigma.
s = random.normalvariate(mu=3, sigma=6)
print("normalvariate:", s)

#Creates a long integer containing k random bits
t = random.getrandbits(24)
print(t)

#Returns a random integer, x, in the range a <= x <= b
u = random.randint(23,32)
print(u)

#Returns a random integer in range(start,stop,step). Does not include the endpoint
v = random.randrange(13,233, 2)
print(v)

#Returns a random element from the nonempty sequence seq
w = random.choice(seq=[1,2,2,3,4,5,5])
print(w)

#Returns a sequence length, len, containing elements chosen randomly from the
#sequence s.The elements in the resulting sequence are placed in the order in which
#they were selected.
#x = random.sample(s=[1,1], len=6)
#print(x)

#Randomly shuffles the items in the list x in place. random is an optional argument that
#specifies a random generation function. If supplied, it must be a function that takes no
#arguments and returns a floating-point number in the range [0.0, 1.0).
#y = random.shuffle(x [2.2,23,3,2,3,2])
#print(y)


#Pareto's distribution with shape parameter alpha
z = random.paretovariate(alpha=32)
print("paretovariate:", z)

#Triangular distribution.A random number n in the range low <= n < high with
##mode mode. By default, low is 0, high is 1.0, and mode is set to the midpoint of low
#nd high
#d = random.triangular([2 ,[ 4 ,[23]]])
#print(d)

#von Mises distribution, where mu is the mean angle in radians between 0 and 2 * pi
#and kappa is a nonnegative concentration factor. If kappa is zero, the distribution
#reduces to a uniform random angle over the range 0 to 2 * pi.
e = random.vonmisesvariate(mu=3, kappa=22)
print("vonmisesvariate:", e)

#Weibull distribution with scale parameter alpha and shape parameter beta
f = random.weibullvariate(alpha=22, beta=42)
print("weibullvariate:", f)

help(random)
