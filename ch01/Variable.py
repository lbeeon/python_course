# -*- coding: UTF-8 -*-
# boolean

a = True
print("variable: {}, type: {}, value: {}".format('a', type(a), a))

# number
b = 1
print("variable: {}, type: {}, value: {}".format('b', type(b), b))

# string
c = 'This is book.'
print("variable: {}, type: {}, value: {}".format('c', type(c), c))

# float
d = 8.7
print("variable: {}, type: {}, value: {}".format('d', type(d), d))

# list/array
# e = list()
e = [1, 2, 2, 3, 4]
print("variable: {}, type: {}, value: {}".format('e', type(e), e))

# tuple
f = (1, 2, 2, 3, 4)
print("variable: {}, type: {}, value: {}".format('f', type(f), f))
# f[2] = 4

# set
g = set(f)
print g

# dictionary
h = {'a': a, 'b':b, 'c':c, 'd': d}
print h
print (h.has_key)('a')
print (h.has_key)('f')
# h = dict()
