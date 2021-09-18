from stl import mesh
import numpy as np
from mpl_toolkits import mplot3d


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

    # Aplica uma matriz de transformação no objeto
    def transformar(self, *matrizes):

        for matriz in matrizes:
            # Aplica a transformação na prórpia matriz
            self.matriz = np.dot(matriz, self.matriz)

            # Aplica a transformação no próprio objeto STL e atualiza os vetores
            self.objeto.transform(matriz)
            self.vetores = self.objeto.vectors

    # Plota o objeto (pontos e faces) nos eixos especificados

    def plotar(self, eixos, cor):

        # Pontos da matriz, em vermelho
        eixos.plot(self.matriz[0, :],
                   self.matriz[1, :], self.matriz[2, :], '.r')

        # Faces do objeto, na cor especificada
        eixos.add_collection3d(mplot3d.art3d.Poly3DCollection(
            self.vetores, facecolors=cor))

        # Contornos das faces, em cinza
        eixos.add_collection3d(mplot3d.art3d.Line3DCollection(
            self.vetores, colors='dimgray', linewidths=0.2, linestyles='-'))
