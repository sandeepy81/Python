dict1={1:"bob",2:"bill",3:"john"}
print(dict1)

k=dict1.keys()
for i in k:
    print(i)

v=dict1.values()
for i in v:
    print(i)

print(dict1[2])
print(dict1[1])

del dict1[2]
print(dict1)


