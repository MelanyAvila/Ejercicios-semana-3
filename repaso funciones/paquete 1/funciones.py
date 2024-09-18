# 1- Elabore un módulo que contenga 3 funciones:
# a- una función que calcule el área de un círculo. Utilizar parámetros opcionales para definir
# que en caso de no recibir un radio el valor del mismo será 3.
def calcular_area_circulo(radio: float = 3)-> float:
    pi = 3.1416
    return pi * (radio ** 2)

# b- una función que calcule el área de un cuadrado y reciba la longitud del lado como
# parámetro, sin parámetros opcionales.
def calcular_area_cuadrado(lado: float)-> float:
    return lado ** 2
    
# c- una función que calcule el área de un triángulo recibiendo base y altura por parámetro
def calcular_area_triangulo(base: float, altura: float) -> float:
    return (base * altura) / 2

