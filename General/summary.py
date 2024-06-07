a=20 # integer
b=20
b=30
print(id(a), id(b))

f=3.14 #float
print(type(f))

c=5+3j  #complex value
print(c.real)
print(c.imag)

s="sandeep" #string

lst=[1,2,3,4,5]
print(type(lst))
b=bytes(lst) #bytes
print(type(b))

ba=bytearray(lst) #bytarray
print(type(ba))

t=(1,2,3,4) #tuple
print(type(t))

s={1,2,20,20,1,40} # set - can not keep duplicate - mutable
print(type(s))
print(s)

fs=frozenset(s) # frozonset - immutable
print(type(s))

dict={1:100,2:200,3:300}
print(type(dict))