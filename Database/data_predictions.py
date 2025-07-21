import numpy as np
import matplotlib.pyplot as plt

# Nuevos datos
x = np.array([
    2943, 3013, 3043, 3113, 3143, 3213, 3244, 3314, 3344, 3414,
    3444, 3514, 3544, 3614, 3644, 3714, 3744, 3814, 3844, 3914
])

y = np.array([
    240, 310, 180, 290, 330, 270, 210, 250, 300, 340, 280, 310, 290, 330, 270, 310, 250, 290, 310, 320


])


# Función para calcular el polinomio
def fx(x1, coef):
    fx = 0
    n = len(coef) - 1
    for p in coef:
        fx += p * x1 ** n
        n -= 1
    return fx


# Predicción y gráfica para varios grados
temp = 3944  # valor de entrada
for i in range(0, 10):
    coef = np.polyfit(x, y, i)
    p = np.polyval(coef, temp)

    print(f"Para grado {i} la predicción es {p}")

    # Ajuste de x1 para que se acomode al rango de x
    x1 = np.linspace(min(x), temp + 1, 1000)  # Usa el rango de los datos de entrada
    y1 = fx(x1, coef)  # Calcula el polinomio

    # Graficar
    plt.figure(figsize=[20, 10])
    plt.title(f"Cantidad de litros vs Año. Para grado: {i}")
    plt.scatter(x, y, s=120, c='blueviolet', label="Datos originales")
    plt.plot(x1, y1, "--", linewidth=3, color='orange', label="Aproximación")
    plt.scatter(temp, p, s=200, c='red', label=f"Predicción: {p:.2f}")
    plt.yticks(range(100, 200, 310))  # Ajusta el rango de los ticks de y
    plt.grid(True)
    ax = plt.gca()
    ax.set_xlabel("$Cantidad de bytes$")
    ax.set_ylabel("$Cantidad litros$")
    plt.legend()
    plt.show()

# Predicción para 2000 y cálculo de MSE
temp = 12  # Valor de entrada para predicción
grado = np.arange(0, 30 + 1, 1)  # De 0 a 30
aproxi = np.array([])
errores = []

for i in grado:
    coef = np.polyfit(x, y, i)
    p = np.polyval(coef, temp)
    aproxi = np.append(aproxi, p)

    # Calcular MSE
    y_pred_vec = []
    for j in x:  # Evaluar los puntos para el MSE
        y_pred = np.polyval(coef, j)
        y_pred_vec.append(y_pred)
    y_pred_vec = np.array(y_pred_vec)

    # Calcular MSE
    MSE = np.sum((y - y_pred_vec) ** 2) / len(y)
    errores.append(MSE)
    print(f"Para grado {i} El MSE es: {round(MSE, 4)}")

# Gráfica de grados vs predicciones
plt.figure(figsize=[20, 10])
plt.title("Grado del polinomio vs Predicción")
plt.plot(grado, aproxi, "--", linewidth=3, color='red', label="Predicción")
plt.grid(True)
plt.xlabel("Grado del polinomio")
plt.ylabel("Predicción")
plt.legend()
plt.show()

# Gráfica de grados vs MSE
plt.figure(figsize=[20, 10])
plt.title("Grado del polinomio vs Error Cuadrático Medio (MSE)")
plt.plot(grado, errores, "-", linewidth=3, color='blue', label="MSE")
plt.grid(True)
plt.xlabel("Grado del polinomio")
plt.ylabel("MSE")
plt.legend()
plt.show()
