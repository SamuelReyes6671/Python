nombre=input("Cual es tu nombre: ")
print(f"Hola {nombre}")
edad=int(input ("Cuantos años tienes: "))
if edad<18:
    print(f"Eres menor de edad {nombre}")
elif edad>=18:
    print(f"Eres mayor de edad {nombre}")

