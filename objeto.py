from numpy.core.fromnumeric import repeat
from transformacoes import rotacao_z, translacao
from stl import mesh
import numpy as np
from mpl_toolkits import mplot3d
from matplotlib import animation
import matplotlib.pyplot as plt

from utilidades import normalizar_eixos


class Objeto:
    # Inicializa lendo um arquivo STL e extraindo pontos x, y, z, vetores do STL e criando a matriz com os pontos em coordenadas homogêneas
    def __init__(self, arquivo):

        self.objeto = mesh.Mesh.from_file(arquivo)

        self.pontos_x = self.objeto.x.flatten()
        self.pontos_y = self.objeto.y.flatten()
        self.pontos_z = self.objeto.z.flatten()
        self.vetores = self.objeto.vectors
        self.matriz = np.array([self.pontos_x.T, self.pontos_y.T,
                                self.pontos_z.T, np.ones(self.pontos_x.size)])

    def transformar(self, *matrizes):  # Aplica uma matriz de transformação no objeto

        for matriz in matrizes:
            # Aplica a transformação na prórpia matriz
            self.matriz = np.dot(matriz, self.matriz)

            # Aplica a transformação no próprio objeto STL e atualiza os vetores
            self.objeto.transform(matriz)
            self.vetores = self.objeto.vectors

    def plotar(self, eixos, cor):  # Plota o objeto (pontos e faces) nos eixos especificados

        # Pontos da matriz, em vermelho
        pontos = eixos.plot(self.matriz[0, :],
                            self.matriz[1, :], self.matriz[2, :], cor)

        """ # Faces do objeto, na cor especificada
        eixos.add_collection3d(mplot3d.art3d.Poly3DCollection(
            self.vetores, facecolors=cor))

        # Contornos das faces, em cinza
        eixos.add_collection3d(mplot3d.art3d.Line3DCollection(
            self.vetores, colors='dimgray', linewidths=0.2, linestyles='-')) """

        normalizar_eixos(eixos)
        return pontos

    # Aplica uma função de animação no objeto
    def animar(self, pontos, figura, eixos, animacao, frames):

        # Remove os pontos plotados anteriormente
        for p in pontos:
            p.remove()

        def init():
            eixos.set_xlim3d(-250, 250)
            eixos.set_ylim3d(-250, 250)
            eixos.set_zlim3d(-250, 250)

            return self.plotar(eixos, 'seagreen')

        return animation.FuncAnimation(figura, animacao, fargs=(self, frames, eixos), init_func=init,
                                       frames=frames, interval=20, blit=True, repeat=False)
