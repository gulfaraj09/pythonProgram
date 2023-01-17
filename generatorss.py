"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -
"""

def gen(n):
    for i in range(n):
        yield i # Generator

# for i in range(78):
#     print(i);
g = gen(3)
print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# for i in g:
#     print(i)

h = "Gulfaraj"
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
# print(iter(h))
# for c in h:
#     print(c)