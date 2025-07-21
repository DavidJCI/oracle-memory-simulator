import numpy as np
import matplotlib.pyplot as plt

# Datos proporcionados
# Asegúrate de que ambas arrays tengan la misma longitud
# Para ejemplo, vamos a cortar el exceso de elementos de `x` o `y` según corresponda

# Opción 1: Recortar los valores de x
x = np.array([
2943, 3013, 3043, 3113, 3143, 3213, 3244, 3314, 3344, 3414,
    3444, 3514, 3544, 3614, 3644, 3714, 3744, 3814, 3844, 3914


])

y = np.array([
397, 442, 439, 438, 440, 440, 440, 440, 440, 441,
    441, 441, 442, 442, 434, 438, 450, 466, 472, 481
])


# Ahora ambas arrays tienen 29 elementos, por lo que se pueden usar en np.polyfit sin problemas


# Ajuste de un polinomio de grado 9
grado = 9
coef = np.polyfit(x, y, grado)

# Predicción para un valor específico de x
temp = 3950  # Valor de x para hacer la predicción
prediccion = np.polyval(coef, temp)

print(f"La predicción para x = {temp} con un polinomio de grado 11 es: {prediccion}")

# Crear el espacio de puntos para la gráfica
x1 = np.linspace(min(x), max(x), 1000)
y1 = np.polyval(coef, x1)

# Graficar los datos originales y el polinomio ajustado
plt.figure(figsize=[20, 10])
plt.title("Ajuste del polinomio de grado 11 a los datos")

plt.scatter(x, y, color='blue', label="Datos originales", s=120)
plt.plot(x1, y1, "--", color='orange', linewidth=3, label="Polinomio de grado 9")
plt.scatter(temp, prediccion, color='red', s=200, label=f"Predicción para x = {temp}")

plt.xlabel("$x$")
plt.ylabel("$y$")
plt.legend()
plt.grid(True)
plt.show()
