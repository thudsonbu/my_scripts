import math

print("What are you looking for? (t l d p)")
print("t = elapsed time")
print("l = decay constant")
print("d = measurable amount of daugheter isotope at time t")
print("p = measurable amount of the parent isotope at time t")

var_to_find = input()

if var_to_find != "t":
    print("What is t?")
    t = float(input())

if var_to_find != "l":
    print("What is l?")
    l = float(input())

if var_to_find != "d":
    print("What is d?")
    d = float(input())

if var_to_find != "p":
    print("What is p?")
    p = float(input())


if var_to_find == 't':
    out = (1.0/l) * ( (math.log(d/p)) + 1.0)

if var_to_find == 'l':
    out = (1.0/t) * ( (math.log(d/p)) + 1.0)

if var_to_find == 'd':
    out = ( (math.exp(t*l)) - 1.0 ) * p

if var_to_find == 'p':
    out = d / ( (math.exp(t*l)) -1)

print(out)