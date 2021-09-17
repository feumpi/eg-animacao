# Segundo Trabalho de Expressão Gráfica para Engenharia Elétrica - 2021/01
# Professora: Raquel Frizera Vassallo
# Aluno: Felipe Pereira Umpierre

# Instruções e documentação adicional em README.pdf ou README.md

""" 
Faça uma animação 3D em Python, usando Numpy e Matplotlib. Os requisitos do trabalho são:
 
1- Animar ao menos dois objetos que não sejam simplesmente uma esfera, um cubo ou objeto simétrico. Os objetos devem ser tais que seja fácil perceber as transformações sendo aplicadas e os resultados da sua movimentação.
2- Aplicar as transformações ensinadas em sala se aula. Os objetos devem realizar pelo menos translações e rotações em mais de um eixo. Outras transformações, como mudança de escala e cisalhamento, também podem ser utilizadas.
3- Utilizar coordenadas homogêneas para aplicar as transformações aos objetos.
4- O arquivo principal do código deve ser feito em Python, usando programação direta (*.py) ou Google Colab (*.ipynb). No caso de se usar a programação direta em Python, o arquivo principal deverá ter o nome de main.py e deverá chamar automaticamente qualquer outro arquivo e funções auxiliares necessárias. Quanlquer arquivo adicional como, por exemplo o arquivo com os pontos dos objetos, deverá ser entregue junto com os códigos.
5- Os códigos devem estar devidamente comentados para facilitar o entendimento e correção. 
"""

# Importar bibliotecas
from stl import mesh
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import pyplot


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


# Carregar o arquivo do dinossauro
dinossauro_stl = mesh.Mesh.from_file('dinossauro.stl')

# Separar os vetores e os pontos x, y e z
dinossauro_x = dinossauro_stl.x.flatten()
dinossauro_y = dinossauro_stl.y.flatten()
dinossauro_z = dinossauro_stl.z.flatten()
vetores_dinossauro = dinossauro_stl.vectors

# Criar a matriz do dinossauro em coordenadas homogêneas
dinossauro = np.array([dinossauro_x.T, dinossauro_y.T,
                      dinossauro_z.T, np.ones(dinossauro_x.size)])

# Criar a plotagem
figura = plt.figure(1, figsize=[10, 10])
eixos = plt.axes(projection='3d')

# Faces do objeto
eixos.add_collection3d(mplot3d.art3d.Poly3DCollection(vetores_dinossauro))

# Contornos das faces
eixos.add_collection3d(mplot3d.art3d.Line3DCollection(
    vetores_dinossauro, colors='k', linewidths=0.2, linestyles='-'))

# Vertices
eixos.plot(dinossauro[0, :], dinossauro[1, :], dinossauro[2, :], 'r.')

# Corrige a escala dos eixos
eixos.auto_scale_xyz(dinossauro[0, :], dinossauro[1, :], dinossauro[2, :])
normalizar_eixos(eixos)

# Exibir a plotagem
plt.show()
