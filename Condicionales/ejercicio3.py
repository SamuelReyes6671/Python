#Escribir un programa que pida al usuario dos números y 
#muestre por pantalla su división. Si el divisor es cero el 
#programa debe mostrar un error.

num1=int(input("Ingrese un dividendo: "))
num2=int(input("Ingrese otro divisor: "))

if num2==0:
    print("Hay un error! No se puede dividir por 0")
else:
    print(num1/num2)

    