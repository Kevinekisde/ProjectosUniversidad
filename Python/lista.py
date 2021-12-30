a = ["foo","bar","baz","qux","quux","corge"]
print(a[1:4])
a[1:4] = [1.1,2.2,3.3,4.4,5.5] ### AGREGO ELEMENTOS ALA LISTA

a[1:6] = ["bark"] ### BORRO LOS ELEMENTOS DEL 1 AL 6 Y AGREGO BARK 


### CREAR LISTA USANDO EL RANGE()

a=[]

a = [None for i in range (10)]

a = [None]*10

a = [[[None]*10]*10]

for row_index in range(len(a)):
    for col_index in range (len(a[row_index])):
        print(a[row_index][col_index])