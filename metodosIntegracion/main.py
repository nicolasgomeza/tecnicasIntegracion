# Import necessary libraries
import numpy as np

# Import values from Trapezoidal file
from Trapezoidal import result_poly_trapez, time_poly_trapez
from Trapezoidal import result_rational_trapez, time_rational_trapez
from Trapezoidal import result_trig_trapez, time_trig_trapez

# Import values from Simpson file
from Simpson import result_poly_simpson, time_poly_simpson
from Simpson import result_rational_simpson, time_rational_simpson
from Simpson import result_trig_simpson, time_trig_simpson

# Import values from Gaussian file
from Gaussian import result_poly, time_poly
from Gaussian import result_rational, time_rational
from Gaussian import result_trig, time_trig

# Display the imported values
print("Trapezoidal Results:")
print(f"Polynomial: {result_poly_trapez}, Time: {time_poly_trapez} seconds")
print(f"Rational: {result_rational_trapez}, Time: {time_rational_trapez} seconds")
print(f"Trigonometric: {result_trig_trapez}, Time: {time_trig_trapez} seconds\n")

print("Simpson Results:")
print(f"Polynomial: {result_poly_simpson}, Time: {time_poly_simpson} seconds")
print(f"Rational: {result_rational_simpson}, Time: {time_rational_simpson} seconds")
print(f"Trigonometric: {result_trig_simpson}, Time: {time_trig_simpson} seconds\n")

print("Gaussian Results:")
print(f"Polynomial: {result_poly}, Time: {time_poly} seconds")
print(f"Rational: {result_rational}, Time: {time_rational} seconds")
print(f"Trigonometric: {result_trig}, Time: {time_trig} seconds")
