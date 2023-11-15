import time
import numpy as np
from scipy import integrate

# Intervalo
a = 0
b = 2

# Precision
n = 1000

def simpson_rule(func, a, b, n):
    start_time = time.time()
    h = (b - a) / n
    result = func(a) + func(b)
    for i in range(1, n, 2):
        result += 4 * func(a + i * h)
    for i in range(2, n-1, 2):
        result += 2 * func(a + i * h)
    result *= h / 3
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

def printResults():
    print("** METODO REGLA DE SIMPSON **")
    # Función polinómica
    result_poly_simpson, time_poly_simpson = simpson_rule(lambda x: x**2, a, b, n)
    print("Función Polinómica")
    print(f"- La integral de {a} hasta {b} es {result_poly_simpson}")
    print(f"- En {time_poly_simpson} segundos con un refinamiento de {n}.\n")

    # Función Racional
    result_rational_simpson, time_rational_simpson = simpson_rule(lambda x: 1/(1+x), a, b, n)
    print("Función Racional")
    print(f"- La integral de {a} hasta {b} es {result_rational_simpson}")
    print(f"- En {time_rational_simpson} segundos con un refinamiento de {n}.\n")

    # Función Trigonométrica
    result_trig_simpson, time_trig_simpson = simpson_rule(lambda x: np.sin(x), 0, np.pi, n)
    print("Función Trigonométrica")
    print(f"- La integral de 0 hasta pi es {result_trig_simpson}")
    print(f"- En {time_trig_simpson} segundos con un refinamiento de {n}.\n")

    # Comparación de resultados
    exact_result_poly = 2.666666667
    exact_result_rat = 1.098612289
    exact_result_trig = 2

    # Entre resultados
    print("\n** Resultados **\nExactos vs Aproximaciones")
    print(f"Función polinómica: {exact_result_poly} vs {result_poly_simpson}")
    print(f"Función racional: {exact_result_rat} vs {result_rational_simpson}")
    print(f"Función trigonométrica: {exact_result_trig} vs {result_trig_simpson}")

    # Diferencia absoluta
    print("\nDiferencia absoluta")
    dif_poly_simpson = abs(exact_result_poly - result_poly_simpson)
    dif_rat_simpson = abs(exact_result_rat - result_rational_simpson)
    dif_trig_simpson = abs(exact_result_trig - result_trig_simpson)

    print(f"Diferencia Polinomial: {dif_poly_simpson}")
    print(f"Diferencia Racional: {dif_rat_simpson}")
    print(f"Diferencia Trigonometrica: {dif_trig_simpson}")

    print("-------------------------------------\n")

# Función para calcular las diferencias y tiempos
def calculate_differences_and_times(func, exact_result, a, b, n):
    result, execution_time = func(lambda x: x**2, a, b, n)
    abs_diff = abs(exact_result - result)
    return result, abs_diff, execution_time


printResults()
