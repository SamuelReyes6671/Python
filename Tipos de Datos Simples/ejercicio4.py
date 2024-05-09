#Escribir un programa que pregunte al usuario por el número 
#de horas trabajadas y el coste por hora. 
#Después debe mostrar por pantalla la paga que le corresponde.

horas=int(input("horas trabajadas: "))
costo=int(input("costo por hora: "))

paga=horas*costo
 
print(f"La paga que le corresponde es : {paga}")
