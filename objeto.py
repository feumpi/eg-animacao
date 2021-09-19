from transformacoes import translacao
from stl import mesh
import numpy as np
from mpl_toolkits import mplot3d

from utilidades import ajustar_escala, normalizar_eixos


class Objeto:
    # Inicializa lendo um arquivo STL e extraindo pontos x, y, z, vetores do STL e criando a matriz com os pontos em coordenadas homogêneas
    def __init__(self, arquivo, cor):

        self.objeto = mesh.Mesh.from_file(arquivo)
        self.cor = cor

        self.pontos_x = self.objeto.x.flatten()
        self.pontos_y = self.objeto.y.flatten()
        self.pontos_z = self.objeto.z.flatten()
        self.vetores = self.objeto.vectors
        self.matriz = np.array([self.pontos_x.T, self.pontos_y.T,
                                self.pontos_z.T, np.ones(self.pontos_x.size)])

        # Inicializa as distâncias da origem (pos inicial = 0)
        self.dist_origem_x = 0
        self.dist_origem_y = 0
        self.dist_origem_z = 0

    # Aplica uma matriz de transformação no objeto
    def transformar(self, *matrizes, inc_distancia=True, origem=False):

        # Move para a origem antes de aplicar as transformações, se solicitado
        if origem:
            self.transformar(translacao(-self.dist_origem_x,
                                        -self.dist_origem_y, -self.dist_origem_z), inc_distancia=False)

        # Para cada uma das transformações que a função recebeu
        for matriz in matrizes:

            # Se for uma matriz de translação, incrementa as distâncias da origem
            if inc_distancia and matriz[0][0] == 1 and matriz[1][1] == 1 and matriz[2][2] == 1 and matriz[3][3] == 1:
                self.dist_origem_x += matriz[0][3]
                self.dist_origem_y += matriz[1][3]
                self.dist_origem_z += matriz[2][3]

            # Aplica a transformação na própria matriz
            self.matriz = np.dot(matriz, self.matriz)

            # Aplica a transformação no próprio objeto (Mesh STL) e atualiza os vetores para plotagem das faces
            self.objeto.transform(matriz)
            self.vetores = self.objeto.vectors

        # Restaura a distâncias anterior caso tenha sido movido para a origem
        if origem:
            self.transformar(translacao(self.dist_origem_x,
                                        self.dist_origem_y, self.dist_origem_z), inc_distancia=False)

    def plotar(self, eixos):  # Plota o objeto (pontos e faces) nos eixos especificados

        # Pontos da matriz, em vermelho
        eixos.plot(self.matriz[0, :],
                   self.matriz[1, :], self.matriz[2, :], '.r')

        # Faces do objeto, na cor especificada
        eixos.add_collection3d(mplot3d.art3d.Poly3DCollection(
            self.vetores, facecolors=self.cor))

        # Contornos das faces, em cinza
        eixos.add_collection3d(mplot3d.art3d.Line3DCollection(
            self.vetores, colors='dimgray', linewidths=0.2, linestyles='-'))

        # Normaliza os eixos e ajusta a escala para o próprio objeto
        normalizar_eixos(eixos)
        ajustar_escala(eixos, self)
