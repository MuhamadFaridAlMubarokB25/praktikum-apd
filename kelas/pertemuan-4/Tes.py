#akumau = int(input("Mau berapa? : "))
#
## Baris pertama: header
#print("*", end=" ")
#for i in range(1, akumau + 1):
#    print(i, end=" ")
#print()
#
## Baris-baris berikutnya: perkalian
#for i in range(1, akumau + 1):
#    print(i, end=" ")
#    for j in range(1, akumau + 1):
#        print(i * j, end=" ")
#    print()

#def farid(A):
#    B = int(input("Berapa yang ingin anda mau?"))
#    print(A*B)
#A = str(input("Mau apa yang diulang?: "))
#farid(A)

def cetak (a,b):
    for i in range(a):
        print(a,end='')

cetak('!',3)
cetak('@',6)
cetak('#',9)
cetak('$',12)