'''exp = [2250, 3210, 1250, 3500, 2340]
total=0
for i in range(len(exp)):
    print("Month",(i+1), "Expenses:",exp[i])
    total=total+exp[i]
print("Total expenses:" ,total)'''

key="closet"
locations=["kitchen", "Living room", "closet", "bathroom"]
for i in locations:
    if i==key:
        print("key is found in", i)
        break
    else:
        print("key is not found in", i)





