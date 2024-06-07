## Set does't allow duplicates

s={10,20,34,57}


s.update([22,25])
#print(s)
print(type(s))
s.remove(34)
print(s)

f=frozenset(s)
print(type(f))
f.update([19,29])
print(s)