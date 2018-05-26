# -*- coding: UTF-8 -*-
def sorted(l, reverse=False):
    pass

print('--------------My sorted function(asc)-------------')
a = [4, 2, 1, 3, 5, 7, 6]
sorted(a)
print(a)

print('--------------Default sort function(asc)-------------')
a = [4, 2, 1, 3, 5, 7, 6]
a.sort()
print(a)

print('--------------My sorted function(desc)-------------')
a = [4, 2, 1, 3, 5, 7, 6]
sorted(a, reverse=True)
print(a)

print('--------------Default sort function(desc)-------------')
a = [4, 2, 1, 3, 5, 7, 6]
a.sort(reverse=True)
print(a)
