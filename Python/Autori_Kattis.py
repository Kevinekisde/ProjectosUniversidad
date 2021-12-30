
nombre = input()
up = nombre[0]
for i in range(len(nombre)):
    if nombre[i] == "-":
        up += nombre[i+1]
print(up)


#https://open.kattis.com/problems/autori