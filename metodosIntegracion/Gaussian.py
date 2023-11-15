import time
from scipy import integrate
import numpy as np

# Intervalo
a = 0
b = 2

# Precision
n = 100

def gaussian_quadrature(func, a, b, n):
    start_time = time.time()
    result, _ = integrate.quadrature(func, a, b, maxiter=n)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

def print_results():
    print("** METODO CUADRATURA GAUSSIANA **")
    # Función polinómica
    result_poly_gaussian, time_poly_gaussian = gaussian_quadrature(lambda x: x**2, a, b, n)
    print("Función Polinómica")
    print(f" - La integral de {a} hasta {b} es {round(result_poly_gaussian, 6)}")
    print(f"- En {round(time_poly_gaussian, 6)} segundos con un refinamiento de {n}.\n")

    # Función Racional
    result_rational_gaussian, time_rational_gaussian = gaussian_quadrature(lambda x: 1/(1+x), a, b, n)
    print("Función Racional")
    print(f"- La integral de {a} hasta {b} es {round(result_rational_gaussian, 6)}")
    print(f"- En {round(time_rational_gaussian, 6)} segundos con un refinamiento de {n}.\n")

    # Función Trigonométrica
    result_trig_gaussian, time_trig_gaussian = gaussian_quadrature(np.vectorize(np.sin), 0, np.pi, n)
    print("Función Trigonométrica")
    print(f"- La integral de 0 hasta pi es {round(result_trig_gaussian, 6)}")
    print(f"- En {round(time_trig_gaussian, 6)} segundos con un refinamiento de {n}.\n")

    # Comparación de resultados
    exact_result_poly = 2.666666667
    exact_result_rat = 1.098612289
    exact_result_trig = 2

    # Entre resultados
    print("\nResultados\nExactos vs Aproximaciones")
    print(f"Función polinómica: {exact_result_poly} vs {result_poly_gaussian}")
    print(f"Función racional: {exact_result_rat} vs {result_rational_gaussian}")
    print(f"Función trigonométrica: {exact_result_trig} vs {result_trig_gaussian}")

    # Diferencia absoluta
    print("\nDiferencia entre ambos (valor absoluto)")
    dif_poly_gaussian = abs(exact_result_poly - result_poly_gaussian)
    dif_rat_gaussian = abs(exact_result_rat - result_rational_gaussian)
    dif_trig_gaussian = abs(exact_result_trig - result_trig_gaussian)

    print(f"Diferencia Polinomial: {dif_poly_gaussian}")
    print(f"Diferencia Racional: {dif_rat_gaussian}")
    print(f"Diferencia Trigonometrica: {dif_trig_gaussian}")

    print("-------------------------------------\n")


# Calcular resultados y tiempos
def calculate_differences_and_times(func, exact_result, a, b, n):
    result, execution_time = func(lambda x: x**2, a, b, n)
    abs_diff = abs(exact_result - result)    
    return result, abs_diff, execution_time

print_results()