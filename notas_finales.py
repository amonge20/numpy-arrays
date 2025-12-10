# Supongamos que tienes un conjunto de calificaciones de un grupo de estudiantes en un
# curso. Cada estudiante tiene cuatro calificaciones: dos exámenes, un trabajo final y una
# participación en clase. Quieres calcular la nota final de cada estudiante, donde los
# exámenes valen un 30% cada uno, el trabajo final vale un 30% y la participación en clase
# vale un 10%. Para ello, puedes usar NumPy para crear un array de 4 columnas y n filas,
# donde n es el número de estudiantes. Cada columna representa una de las calificaciones
# y cada fila representa un estudiante. Luego, puedes usar operaciones de NumPy para
# calcular la nota final de cada estudiante y almacenarla en un nuevo array de una sola
# columna.

import numpy as np 

# Notas finales (examen1, examen2, trabajo final y participación en clase)
# Estudiantes = np.array()
Evaluacion = np.array([[7,5,5,7],
                         [6,4,4,0], 
                         [6,3,2,7],
                         [8,9,10,10]])

# Lista en donde guardamos las notas finales de cada estudiante
Notas_Finales = []

# Puntuación de las notas de los examenes
# Puntuación del trabajo final
# Puntuación de la participación de la clase
for i in Evaluacion:
    examenes = (i[0] / 100 * 30) + (i[1] / 100 * 30)
    trabajo_final = (i[2] / 100 * 30)
    participacion_clase = (i[3] / 100 * 10) 

    # Nota final de cada estudiante
    nota = examenes + trabajo_final + participacion_clase
    Notas_Finales.append(nota)

# Obtenemos la media
Notas_Finales = np.array(Notas_Finales)

# Nota final para cada estudiante
for estudiante, nota in enumerate(Notas_Finales, start=1):
    print(f"Estudiante {estudiante}: {nota:.2f}")