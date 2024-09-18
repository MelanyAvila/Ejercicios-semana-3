# 2- Elaborar un módulo que contenga 3 funciones. Pero este deberá calcular los perímetros
# de las mismas figuras que el punto 1.
def calcular_perimetro_circulo(diametro: float)-> float:
    pi = 3.1416
    return pi * diametro 

def calcular_perimetro_circulo_con_radio(radio: float = 3)-> float:
    pi = 3.1416
    return pi * (radio * 2)
# no sabia si hacerlo con la condicion del punto 1 asi que hice los dos!

def calcular_perimetro_cuadrado(lado: float) -> float:
   return lado * 4

def calcular_perimetro_triangulo(lado1: float, lado2: float, lado3: float) -> float:
    perimetro = lado1 + lado2 + lado3
    return perimetro

