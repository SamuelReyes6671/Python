#Escribir un programa que pregunte al usuario su edad 
#y muestre por pantalla si es mayor de edad o no.

edad=int(input("Cual es su edad: "))
if edad<18:
    print("usted es menor de edad")
elif edad>=18:
    print("usted es mayor de edad")