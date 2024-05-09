import random

random=random.randint(1,10)
numero=-1
while numero!=random:
    numero=int(input("Adivina el Numero (1-10):"))
    if numero>random:
        print("Te has pasado")
    elif numero<random:
        print("Te has quedado corto")

print(f"FELICIDADES LO ADIVINASTES... EL NUMERO ERA {random}")
print("Te ganaste un BESO DE TU ESPOSITO")
print("TE amo mi amor...")





