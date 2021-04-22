
max = max2 = -101
for n in map(int,input().split()):
    if n > max2:
        if n > max:
            max,max2 = n,max
        elif n < max:
            max2 = n
print(max2)