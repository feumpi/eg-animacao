from stl import mesh
import numpy as np


class Objeto:
    def __init__(self, objeto):  # Inicializa extraindo pontos x, y, z, vetores do STL e criando a matriz com os pontos em coordenadas homogêneas
        self.pontos_x = objeto.x.flatten()
        self.pontos_y = objeto.y.flatten()
        self.pontos_z = objeto.z.flatten()
        self.vetores = objeto.vectors
        self.matriz = np.array([self.pontos_x.T, self.pontos_y.T,
                                self.pontos_z.T, np.ones(self.pontos_x.size)])


# Lê um arquivo STL com o nome recebido e retorna um objeto com seus pontos x, y, z, seus vetores e a matriz com coordenadas homogêneas
def carregar_stl(nome):
    objeto = mesh.Mesh.from_file(nome)
    return Objeto(objeto)


# Normaliza a escala de todos os eixos para não distorcer o objeto
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
