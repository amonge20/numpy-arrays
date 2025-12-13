# Supongamos que tienes un conjunto de datos de clima que contiene información sobre la
# temperatura, la humedad y la presión atmosférica en una ciudad durante un año. Quieres
# analizar estos datos para determinar cuál fue la temperatura promedio de cada mes, cuál
# fue la humedad promedio y la presión atmosférica promedio durante todo el año. Para
# ello, puedes usar NumPy para cargar los datos en un array de 3 columnas y n filas, donde
# n es el número de mediciones. Luego, puedes usar operaciones de NumPy para filtrar los
# datos por mes y calcular las medias de temperatura, humedad y presión atmosférica
# correspondientes.

import numpy as np

# Datos de los meses
meses = np.array([
    '2024-01-15', '2024-02-15', '2024-03-15', '2024-04-15',
    '2024-05-15', '2024-06-15', '2024-07-15', '2024-08-15',
    '2024-09-15', '2024-10-15', '2024-11-15', '2024-12-15'
    ])

# Datos del año
# Datos del clima (temperatura, humedad y presión atmosférica durante un año)
clima = np.array([
    [20, 50, 1012],  # Enero
    [22, 55, 1010],  # Febrero
    [25, 60, 1008],  # Marzo
    [28, 65, 1005],  # Abril
    [30, 70, 1003],  # Mayo
    [32, 72, 1001],  # Junio
    [35, 75, 1000],  # Julio
    [34, 74, 1002],  # Agosto
    [29, 68, 1005],  # Septiembre
    [25, 60, 1008],  # Octubre
    [22, 55, 1010],  # Noviembre
    [20, 50, 1012]   # Diciembre 
])

# Recorremos un bucle para calcular la media de cada mes
for mes in np.unique(meses):
    # Filtramos los datos de los meses
    datos_mes = clima[meses == mes]
    
    # Calculamos la media de cada mes
    temperatura = datos_mes[:,0].mean()
    humedad = datos_mes[:,1].mean()
    presion_atmosferica = datos_mes[:,2].mean()
    print(f"Mes {mes}: temperatura: {temperatura}; humedad: {humedad}; Presición Atmosferica: {presion_atmosferica}")

print("")

# Calculamos la media del promedio anual
Temperaturanual = clima[:,0].mean()
Humedad_anual = clima[:,1].mean()
Presion_atmosfericanual = clima[:,2].mean()

print("Promedio anual")
print(f"Temperatura = {Temperaturanual:.1f} ºC")
print(f"Humedad = {Humedad_anual:.1f}")
print(f"Presión = {Presion_atmosfericanual:.1f}")