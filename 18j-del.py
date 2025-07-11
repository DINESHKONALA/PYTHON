a = 10
b = 20
print(id(a),id(b))
# del a,b
# print(a,b)

c = 10
d = 10
print(id(c),id(d), id(a), id(b))
print(c,d)
del c
print(d)
# print(c)  # NameError: name 'c' is not defined

