import random

start = [.12, .15, .18, .09, .13]
out = []

increase = True
for i in range(0,156):
    if increase:
        out.append(round(start[random.randint(0,4)],2))
        start[random.randint(0,4)] += .03
        increase = False 
    else:
        out.append(round(start[random.randint(0,4)],2))
        increase = True

for num in out:
    print(num)