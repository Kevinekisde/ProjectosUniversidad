t=("foo","bar","baz","qux","quux","corge")
print(t)
print(t[0])
print(t[-1])
print(t[2:4])

t=("foo","bar","baz","qux","quux","corge")
x1,x2,x3,x4,x5,x6 = t
print(t)

##intercabio (swap)
a = "foo"
b = "bar"
a,b = b,a
print("a,b")