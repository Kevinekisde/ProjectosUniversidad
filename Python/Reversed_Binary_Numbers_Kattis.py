#https://open.kattis.com/problems/reversebinary

n=int(input(""))

x=bin(n)
m=x[::-1]
z=int(str(m),2)
print(z)