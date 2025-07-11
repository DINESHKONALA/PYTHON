import math;
# help(math)
# print(abs(10))
# print(abs(0))
# print(abs(9
#           ))
# print(abs(-9))
# print(abs(-0.0))

# print(math.ceil(9.2))
# print(math.ceil(-9.2))
# print(math.ceil(-0))
# print(math.ceil(10.33333333333))


# print(math.floor(20.22))
# print(math.floor(-20.22))
# print(math.floor(-9))

# print(math.log(math.exp(10)))
# print(math.log(10))
# # print(math.log(-10)); #ValueError(-ve no)

# #log10() function (log-value to base-10)
# print(math.log10(10))
# print(math.log10(9))
# print(math.log10(100))
# print(math.log10(1000))
# print(math.log10(-10)) #ValueError: math domain error

# #factorial() function
# print(math.factorial(5))
# print(math.factorial(0))
# print(math.factorial(11))

# #exp() function (e--->Euler's number) (e power x)
# print(math.exp(10))
# print(math.exp(1))

# #fabs() function (float abs +ve val)
# print(math.fabs(10))
# print(math.fabs(0))
# print(math.fabs(-10))
# print(math.fabs(10.33))

# #max() function
# max_val = (10, 20, 30, 40, 50)
# print(max(max_val))

# #min() function
# print(min(10, 20, 30, 40, 50))
# print(a = min (10, 20, 30, 40, 50, 0, -10, -20, -30, -40, -50))

# #pow(x,y) function (x pow y)
# print(math.pow(5, 2))
# print(math.pow(10, -2)) #0.01
# print(math.pow(10, 0)) #1
# print(math.pow(10, 1)) #10

# #sqrt() function (sqr-root-val)
# print(math.sqrt(25))
# print(math.sqrt(100))
# print(math.sqrt(81))
# print(math.sqrt(2))
# # print(math.sqrt(-2)) #ValueError: math domain error







import random
# # **) choice(sequence):- #choice() (works only on index-coll) -->random value from given coll.
# x = [10, 20, 30, 40, 50]
# y = ['nani', 'naveen', 'sai', 'sri', 'sai']
# z = random.choice('nani')
# print(random.choice(x))
# a = random.choice(y)
# print(a)
# print(z)

# ##randrange(start,end,step)  --> random value in given range
# print(random.randrange(10, 20, 2))
# print(random.randrange(10, 21))
# print(random.randrange(-10, -1, 2))

# # **)random() = It generates a random float number b/w 0 to 1
# print(random.random())

# # **) shuffle(list):-
# x = [10, 20, 30, 40, 50]
# random.shuffle(x)
# print(x)

# # **) uniform(x,y) = #uniform(x,y) --->random float-value b/w x & y(not-included)
# print(random.uniform(1,5))

help(random)

