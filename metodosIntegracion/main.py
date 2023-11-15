import numpy as np

# Importar funciones de los módulos de Gauss, Trapezoidal y Simpson
from Gaussian import gaussian_quadrature as metodo_gaussiano
from Trapezoidal import trapezoidal_rule as metodo_trapezoidal
from Simpson import simpson_rule as metodo_simpson

# Resultados precisos integracion
exact_result_poly = 2.666666667
exact_result_rat = 1.098612289
exact_result_trig = 2


# Definir los límites de integración y la precisión
a = 0
b = 2
n = 100

# Realizar cálculos para cada método y función
# Método Gaussiano
resultado_polinomial_gaussiano, tiempo_polinomial_gaussiano = metodo_gaussiano(lambda x: x**2, a, b, n)
resultado_racional_gaussiano, tiempo_racional_gaussiano = metodo_gaussiano(lambda x: 1/(1+x), a, b, n)
resultado_trig_gaussiano, tiempo_trig_gaussiano = metodo_gaussiano(np.sin, 0, np.pi, n)

# Método Trapezoidal
resultado_polinomial_trapezoidal, tiempo_polinomial_trapezoidal = metodo_trapezoidal(lambda x: x**2, a, b, n)
resultado_racional_trapezoidal, tiempo_racional_trapezoidal = metodo_trapezoidal(lambda x: 1/(1+x), a, b, n)
resultado_trig_trapezoidal, tiempo_trig_trapezoidal = metodo_trapezoidal(np.sin, 0, np.pi, n)

# Método Simpson
resultado_polinomial_simpson, tiempo_polinomial_simpson = metodo_simpson(lambda x: x**2, a, b, n)
resultado_racional_simpson, tiempo_racional_simpson = metodo_simpson(lambda x: 1/(1+x), a, b, n)
resultado_trig_simpson, tiempo_trig_simpson = metodo_simpson(np.sin, 0, np.pi, n)

# Crear un diccionario para almacenar los resultados
resultados_dict = {
    "Gaussiano - Polinomial": {"resultado": resultado_polinomial_gaussiano, "tiempo": tiempo_polinomial_gaussiano},
    "Gaussiano - Racional": {"resultado": resultado_racional_gaussiano, "tiempo": tiempo_racional_gaussiano},
    "Gaussiano - Trigonométrico": {"resultado": resultado_trig_gaussiano, "tiempo": tiempo_trig_gaussiano},
    "Trapezoidal - Polinomial": {"resultado": resultado_polinomial_trapezoidal, "tiempo": tiempo_polinomial_trapezoidal},
    "Trapezoidal - Racional": {"resultado": resultado_racional_trapezoidal, "tiempo": tiempo_racional_trapezoidal},
    "Trapezoidal - Trigonométrico": {"resultado": resultado_trig_trapezoidal, "tiempo": tiempo_trig_trapezoidal},
    "Simpson - Polinomial": {"resultado": resultado_polinomial_simpson, "tiempo": tiempo_polinomial_simpson},
    "Simpson - Racional": {"resultado": resultado_racional_simpson, "tiempo": tiempo_racional_simpson},
    "Simpson - Trigonométrico": {"resultado": resultado_trig_simpson, "tiempo": tiempo_trig_simpson}
}

# Imprime todos los resultados
def print_data(dict):
    for key, value in resultados_dict.items():
        print(f"\n{key}")
        print(f"Resultado: {value['resultado']}, Tiempo: {value['tiempo']} segundos")
# print(resultados_dict)

# Imprime los resultados organizados por tiempo
def print_sorted_times(dict):
    # Agrupar los resultados por función
    functions = set(key.split(' - ')[1] for key in dict.keys())

    for func in functions:
        results_for_func = {key: value for key, value in dict.items() if func in key}
        sorted_results = sorted(results_for_func.items(), key=lambda x: x[1]["tiempo"])

        print(f"\nComparación de Métodos para la Función {func}")
        for i in range(len(sorted_results)):
            key, value = sorted_results[i]

            if i == 0:
                print(f"+ Método más rápido: {key.split(' - ')[0]} con un tiempo de {value['tiempo']} segundos")
            else:
                prev_key, prev_value = sorted_results[i - 1]
                time_difference_prev = prev_value["tiempo"] - value["tiempo"]
                print(f"+ Seguido de: {key.split(' - ')[0]} con una diferencia de {abs(time_difference_prev)} segundos respecto al método más rápido")

# Imprime todos los resultados
print_sorted_times(resultados_dict)



# Método con la aproximación más cercana para cada función
metodo_min_dif_polinomial = min([k for k, v in resultados_dict.items() if 'Polinomial' in k])
metodo_min_dif_racional = min([k for k, v in resultados_dict.items() if 'Racional' in k])
metodo_min_dif_trig = min([k for k, v in resultados_dict.items() if 'Trigonométrico' in k])

print(f"\nAproximación más cercana para la función Polinomial: {metodo_min_dif_polinomial}")
print(f"Aproximación más cercana para la función Racional: {metodo_min_dif_racional}")
print(f"Aproximación más cercana para la función Trigonométrica: {metodo_min_dif_trig}")
