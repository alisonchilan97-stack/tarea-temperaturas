Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import random
...
... # Definir datos
... ciudades = ["Quito", "Guayaquil", "Cuenca"]
... dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
... semanas = 4
...
... # Crear matriz 3D: [ciudad][semana][día]
... # Se llenan con temperaturas aleatorias entre 15 y 35 grados
... matriz = [[[random.randint(15, 35) for _ in dias] for _ in range(semanas)] for _ in ciudades]
...
... # Calcular promedios
... for i, ciudad in enumerate(ciudades):  # recorrer ciudades
...     print(f"\nCiudad: {ciudad}")
...     for s in range(semanas):  # recorrer semanas
...         suma = 0
...         for d in range(len(dias)):  # recorrer días
...             suma += matriz[i][s][d]
...         promedio = suma / len(dias)
...         print(f"  Semana {s+1}: Promedio = {promedio:.2f}°C")
...

Ciudad: Quito
  Semana 1: Promedio = 22.43°C
  Semana 2: Promedio = 25.29°C
  Semana 3: Promedio = 27.71°C
  Semana 4: Promedio = 28.00°C

Ciudad: Guayaquil
  Semana 1: Promedio = 26.29°C
  Semana 2: Promedio = 28.57°C
  Semana 3: Promedio = 25.29°C
  Semana 4: Promedio = 24.71°C

Ciudad: Cuenca
  Semana 1: Promedio = 25.57°C
  Semana 2: Promedio = 25.43°C
  Semana 3: Promedio = 24.57°C
  Semana 4: Promedio = 28.71°C
>>>

