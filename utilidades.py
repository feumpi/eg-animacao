import numpy as np
import matplotlib.pyplot as plt


# Retorna a figura e os eixos do matplotlib
def criar_eixos():
    figura = plt.figure(1, figsize=[7, 7])
    eixos = plt.axes(projection='3d')
    return figura, eixos


# Ajusta o tamanho dos eixos e a posição de visualização
def ajustar_eixos(eixos, azimute, elevacao, tamanho_x, tamanho_y, tamanho_z):
    eixos.azim = azimute
    eixos.elev = elevacao

    # x e y metade negativo e metade positivo (esquerda e direita da origem)
    eixos.set_xlim3d(-(tamanho_x/2), tamanho_x/2)
    eixos.set_ylim3d(-(tamanho_y/2), tamanho_y/2)

    # z apenas positivo (para cima)
    eixos.set_zlim3d(0, tamanho_z)


# Ajusta a escala dos eixos para as proporções de um objeto
def ajustar_escala(eixos, objeto):
    eixos.auto_scale_xyz(
        objeto.matriz[0, :], objeto.matriz[1, :], objeto.matriz[2, :])


# Normaliza a escala de todos os eixos para não distorcer a plotagem
def normalizar_eixos(eixos):

    # Obter os limites x, y e z atuais
    limites_x = eixos.get_xlim3d()
    limites_y = eixos.get_ylim3d()
    limites_z = eixos.get_zlim3d()

    # Calcular o tamanho e o meio dos eixos
    tamanho_x = abs(limites_x[1] - limites_x[0])
    meio_x = np.mean(limites_x)
    tamanho_y = abs(limites_y[1] - limites_y[0])
    meio_y = np.mean(limites_y)
    tamanho_z = abs(limites_z[1] - limites_z[0])
    meio_z = np.mean(limites_z)

    # Determinar o raio de plotagem (metade do maior eixo)
    raio_plotagem = 0.5 * max([tamanho_x, tamanho_y, tamanho_z])

    # Atualizar os limites x, y e z normalizados
    eixos.set_xlim3d([meio_x - raio_plotagem, meio_x + raio_plotagem])
    eixos.set_ylim3d([meio_y - raio_plotagem, meio_y + raio_plotagem])
    eixos.set_zlim3d([meio_z - raio_plotagem, meio_z + raio_plotagem])
