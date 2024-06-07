#print 1 to 20 numbers and skip multiples of 3

x=0
for i in range(1,21):
    x+=1
    if x%3 == 0:
        continue
    print(x)

