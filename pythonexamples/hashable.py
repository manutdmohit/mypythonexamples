import collections
l=[10,20,30]
t=(10,20,30)
print(isinstance(l,collections.Hashable))
print(isinstance(t,collections.Hashable))
print(hash(t))
