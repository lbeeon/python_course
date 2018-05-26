l = [1, 2, 3, 4]
print(l)

l = [1, 2, 3, 4]
l[0] = 999
print(l)

l.append(5)
print(l)

l.insert(0, 0)
print(l)

a = l.pop()
print(a)
print(l)

a = l.pop(0)
print(a)
print(l)

l.sort()
print(l)

l.sort(reverse=True)
print(l)
