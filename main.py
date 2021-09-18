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

from objeto import Objeto
from utilidades import normalizar_eixos
from transformacoes import translacao, rotacao_x, rotacao_y, rotacao_z


dinossauro = Objeto("dinossauro.stl")

# Criar a plotagem
figura = plt.figure(1, figsize=[7, 7])
eixos = plt.axes(projection='3d')
eixos.azim = -45
eixos.elev = 30

# Rotação inicial do dinosauro
#dinossauro.matriz = np.dot(transformacoes.rotacao_x(90), dinossauro.matriz)
#dinossauro.matriz = np.dot(transformacoes.rotacao_z(45), dinossauro.matriz)
dinossauro.transformar(rotacao_x(90))
dinossauro.transformar(rotacao_z(45))
dinossauro.plotar(eixos, 'seagreen')


# Corrige a escala dos eixos
eixos.auto_scale_xyz(
    dinossauro.matriz[0, :], dinossauro.matriz[1, :], dinossauro.matriz[2, :])
normalizar_eixos(eixos)

# Exibir a plotagem
plt.show()
