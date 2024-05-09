import math
print("Area del Circulo")
def areaCirculo(radio):
    area=math.pi*radio**2
    perimetro=math.pi*2*radio
    return area,perimetro

a,p=areaCirculo(10)

print(f"Area: {a}")
print(f"Perimetro: {p}")


