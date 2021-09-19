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
from utilidades import ajustar_eixos, ajustar_escala, normalizar_eixos
from transformacoes import translacao, rotacao_x, rotacao_y, rotacao_z
from animacoes import animar_objetos, anim_teste

# Inicializa os objetos a partir dos arquivos
dinossauro = Objeto('dinossauro.stl', 'seagreen')
meteoro = Objeto('meteoro.stl', 'k')

# Cria a figura e os eixos 3D
figura = plt.figure(1, figsize=[7, 7])
eixos = plt.axes(projection='3d')

# Ajusta o tamanho e visualização dos eixos
ajustar_eixos(eixos, azimute=-45, elevacao=30, tamanho_x=500,
              tamanho_y=500, tamanho_z=1000)

# Posição e rotação inicial dos objetos
dinossauro.transformar(rotacao_x(90), rotacao_z(45))
meteoro.transformar(translacao(250, 250, 800))

# Plotagem inicial dos objetos
dinossauro.plotar(eixos)
meteoro.plotar(eixos)

# Animação de teste
animar_objetos(eixos, anim_teste, frames=30, intervalo=0.01,
               objetos=(dinossauro, meteoro))

# Exibir a plotagem
plt.show()
