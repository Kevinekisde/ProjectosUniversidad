from collections import Counter


nombre = input().split
contador= Counter(nombre)
palabra=contador.most_common()[0][0]


print(palabra)