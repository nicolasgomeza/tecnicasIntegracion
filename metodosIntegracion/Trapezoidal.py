import time
from scipy import integrate
import numpy as np

# Intervalo
a = 0
b = 2

# Precision
n = 100

def trapezoidal_rule(func, a, b, n): 
    start_time = time.time()
    h = (b - a) / n
    result = 0.5 * (func(a) + func(b))
    for i in range(1, n):
        result += func(a + i * h)
    result *= h
    end_time = time.time()
    execution_time = round(end_time - start_time, 6)
    return round(result, 6), execution_time

def print_results():
    print("** METODO REGLA DEL TRAPECIO **")
    # Función polinómica
    result_poly_trapez, time_poly_trapez = trapezoidal_rule(lambda x: x**2, a, b, n)
    print("Función Polinómica")
    print(f" - La integral de {a} hasta {b} es {result_poly_trapez}")
    print(f"- En {time_poly_trapez} segundos con un refinamiento de {n}.\n")

    # Función Racional
    result_rational_trapez, time_rational_trapez = trapezoidal_rule(lambda x: 1/(1+x), a, b, n)
    print("Función Racional")
    print(f"- La integral de {a} hasta {b} es {result_rational_trapez}")
    print(f"- En {time_rational_trapez} segundos con un refinamiento de {n}.\n")

    # Función Trigonométrica
    result_trig_trapez, time_trig_trapez = trapezoidal_rule(lambda x: np.sin(x), 0, np.pi, n)
    print("Función Trigonométrica")
    print(f"- La integral de 0 hasta pi es {result_trig_trapez}")
    print(f"- En {time_trig_trapez} segundos con un refinamiento de {n}.\n")

    # Comparación de resultados
    exact_result_poly = 2.666666667
    exact_result_rat = 1.098612289
    exact_result_trig = 2

    # Entre resultados
    print("\nResultados\nExactos vs Aproximaciones")
    print(f"Función polinómica: {exact_result_poly} vs {result_poly_trapez}")
    print(f"Función racional: {exact_result_rat} vs {result_rational_trapez}")
    print(f"Función trigonométrica: {exact_result_trig} vs {result_trig_trapez}")

    # Diferencia absoluta
    print("\nDiferencia absoluta")
    dif_poly_trapez = abs(exact_result_poly - result_poly_trapez)
    dif_rat_trapez = abs(exact_result_rat - result_rational_trapez)
    dif_trig_trapez = abs(exact_result_trig - result_trig_trapez)

    print(f"Diferencia Polinomial: {dif_poly_trapez}")
    print(f"Diferencia Racional: {dif_rat_trapez}")
    print(f"Diferencia Trigonometrica: {dif_trig_trapez}")

    print("-------------------------------------\n")

# Función para calcular las diferencias y tiempos
def calculate_differences_and_times(func, exact_result, a, b, n):
    result, execution_time = func(lambda x: x**2, a, b, n)
    abs_diff = abs(exact_result - result)
    return result, abs_diff, execution_time


# Invocacion de funcion, main.py lo hace
'''
result_poly_trapez, dif_poly_trapez, time_poly_trapez = calculate_differences_and_times(trapezoidal_rule, exact_result_poly, a, b, n)
result_rational_trapez, dif_rat_trapez, time_rational_trapez = calculate_differences_and_times(trapezoidal_rule, exact_result_rat, a, b, n)
result_trig_trapez, dif_trig_trapez, time_trig_trapez = calculate_differences_and_times(trapezoidal_rule, exact_result_trig, 0, np.pi, n)
'''


