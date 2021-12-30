a=int(input(""))

qaly=0

for i in range (a):
    a,s=input("").split(" ")
    a=float(a)
    s=float(s)
    qaly += a*s
print(qaly)

#https://open.kattis.com/problems/qaly