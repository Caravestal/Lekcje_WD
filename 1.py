import numpy as py
a = py.array( [[20,30,40],[50,4,7],[2,5,4]] )
b = py.array( [[20,30,40,1],[50,4,7,11],[2,5,4,9],[1,2,3,4]] )
print(a.min(axis=1))
print(b.min(axis=1))
print(a.min(axis=0))
print(b.min(axis=0))