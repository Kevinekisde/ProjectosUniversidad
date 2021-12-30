lineas=int(input(""))

for i in range(lineas):
    x=input("")
    if x.startswith("Simon says"):
        print (" ".join(x.split()[2:])) ##### elimina las palabras 
    else:
        print("")


#https://open.kattis.com/problems/simonsays