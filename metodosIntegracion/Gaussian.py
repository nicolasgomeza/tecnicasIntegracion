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

print("-------------------------------------\n** METODO CUADRATURA GAUSSIANA **")

# Función polinómica
result_poly, time_poly = gaussian_quadrature(lambda x: x**2, a, b, n)
print("Función Polinómica")
print(f" - La integral de {a} hasta {b} es {round(result_poly, 6)}")
print(f"- En {round(time_poly, 6)} segundos con un refinamiento de {n}.\n")

# Función Racional
result_rational, time_rational = gaussian_quadrature(lambda x: 1/(1+x), a, b, n)
print("Función Racional")
print(f"- La integral de {a} hasta {b} es {round(result_rational, 6)}")
print(f"- En {round(time_rational, 6)} segundos con un refinamiento de {n}.\n")

# Función Trigonométrica
result_trig, time_trig = gaussian_quadrature(np.vectorize(np.sin), 0, np.pi, n)
print("Función Trigonométrica")
print(f"- La integral de 0 hasta pi es {round(result_trig, 6)}")
print(f"- En {round(time_trig, 6)} segundos con un refinamiento de {n}.\n")


# Comparación de resultados
exact_result_poly = 2.666666667
exact_result_rat = 1.098612289
exact_result_trig = 2

# Entre resultados
print("\nResultados\nExactos vs Aproximaciones")
print(f"Función polinómica: {exact_result_poly} vs {result_poly}")
print(f"Función racional: {exact_result_rat} vs {result_rational}")
print(f"Función trigonométrica: {exact_result_trig} vs {result_trig}")

# Diferencia absoluta
print("\nDiferencia entre ambos (valor absoluto)")
dif_poly = abs(exact_result_poly - result_poly)
dif_rat = abs(exact_result_rat - result_rational)
dif_trig = abs(exact_result_trig - result_trig)

print(f"Diferencia Polinomial: {dif_poly}")
print(f"Diferencia Racional: {dif_rat}")
print(f"Diferencia Trigonometrica: {dif_trig}")

print("-------------------------------------\n")

# Metodos públicos para main.py
def gaussian_quadrature(func, a, b, n):
    start_time = time.time()
    result, _ = integrate.quadrature(func, a, b, maxiter=n)
    end_time = time.time()
    execution_time = round(end_time - start_time, 6)
    return round(result, 6), execution_time