# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-2yE-4rF9d9p4y-15DHvPlDjPTSH3GZ3
"""

# prompt: #PROGRAMA QUE IDENTIFICA EL CUADRANTE EN EL QUE SE ENCUENTRA EL PUNTO

def obtener_coordenada(nombre_coordenada):
  """Solicita al usuario una coordenada y verifica que no sea cero."""
  while True:
    try:
      coordenada = int(input(f"Ingrese la coordenada {nombre_coordenada}: "))
      if coordenada == 0:
        print("Error: La coordenada no puede ser cero. Intente nuevamente.")
      else:
        return coordenada
    except ValueError:
      print("Error: Ingrese un número entero válido.")

def identificar_cuadrante(x, y):
  """Identifica el cuadrante en el que se encuentra el punto (x, y)."""
  if x > 0 and y > 0:
    return "Cuadrante I"
  elif x < 0 and y > 0:
    return "Cuadrante II"
  elif x < 0 and y < 0:
    return "Cuadrante III"
  elif x > 0 and y < 0:
    return "Cuadrante IV"

# Obtener coordenadas del usuario
x = obtener_coordenada("X")
y = obtener_coordenada("Y")

# Identificar el cuadrante
cuadrante = identificar_cuadrante(x, y)
print(f"El punto ({x}, {y}) se encuentra en el {cuadrante}")