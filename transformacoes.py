import numpy as np
from math import sin, cos


# Retorna a matriz de translação para as distâncias x, y e z
def translacao(x, y, z):
    matriz = np.array([[1, 0, 0, x],
                       [0, 1, 0, y],
                       [0, 0, 1, z],
                       [0, 0, 0, 1]])
    return matriz


# Retorna a matriz de rotação no eixo x para um ângulo específico, em graus
def rotacao_x(angulo):
    angulo = np.radians(angulo)
    matriz = np.array([[1, 0, 0, 0],
                       [0, cos(angulo), -sin(angulo), 0],
                       [0, sin(angulo), cos(angulo), 0],
                       [0, 0, 0, 1]])
    return matriz


# Retorna a matriz de rotação no eixo y para um ângulo específico, em graus
def rotacao_y(angulo):
    angulo = np.radians(angulo)
    matriz = np.array([[cos(angulo), 0, sin(angulo), 0],
                       [0, 1, 0, 0],
                       [-sin(angulo), 0, cos(angulo), 0],
                       [0, 0, 0, 1]])
    return matriz


# Retorna a matriz de rotação no eixo z para um ângulo específico, em graus
def rotacao_z(angulo):
    angulo = np.radians(angulo)
    matriz = np.array([[cos(angulo), -sin(angulo), 0, 0],
                       [sin(angulo), cos(angulo), 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])
    return matriz
