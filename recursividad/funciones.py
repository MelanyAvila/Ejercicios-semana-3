# 1 - Calcular mediante recursividad la potencia de un número, mediante una función que
# recibe un número base de tipo entero y un exponente de tipo entero. Utilizar parámetros
# opcionales para definir que si la función no recibe ningún parámetro devolverá 2 al
# cuadrado.
def calcular_potencia(base: int, exponente: int = 0)-> int:
    if exponente == 0:
        return 1
    return base * calcular_potencia(base, exponente - 1)

# 2 - Resolver mediante recursividad el problema de las torres de Hanoi
def resolver_torres_hanoi(disco: int, poste_inicial: str = 'A', poste_intermedio: str = 'B', poste_final: str = 'C')-> None:
    if disco == 1:
        print(f'mover el disco 1 de {poste_inicial} a {poste_final}')
    else:
        # del poste inicial al intermedio
        resolver_torres_hanoi(disco - 1, poste_inicial, poste_intermedio, poste_final)
        
        # del poste inicial al final
        print(f'mover el disco {disco} de {poste_inicial} a {poste_final}')
        
        # del poste intermedio al final
        resolver_torres_hanoi(disco - 1, poste_intermedio, poste_final, poste_inicial)

