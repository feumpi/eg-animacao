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
from animacoes import animar_objetos, caminhando, extincao, ao_infinito

# Inicializa os objetos a partir dos arquivos
dino_azul = Objeto('dinossauro.stl', 'royalblue')
dino_amarelo = Objeto('dinossauro.stl', 'gold')
dino_verde = Objeto('dinossauro.stl', 'seagreen')
meteoro = Objeto('meteoro.stl', 'k')

# Cria a figura e os eixos 3D
figura = plt.figure(1, figsize=[7, 7])
eixos = plt.axes(projection='3d')

# Ajusta o tamanho e visualização dos eixos
ajustar_eixos(eixos, azimute=-45, elevacao=30, tamanho_x=500,
              tamanho_y=500, tamanho_z=1000)

# Posição e rotação inicial dos objetos
dino_azul.transformar(rotacao_x(90),
                      rotacao_z(-90),
                      translacao(-350, -300, 0))

dino_amarelo.transformar(rotacao_x(90),
                         rotacao_z(90),
                         translacao(350, 300, 0))

dino_verde.transformar(rotacao_x(90), rotacao_z(135))

meteoro.transformar(translacao(500, 500, 2500))

# Plotagem inicial dos objetos
dino_azul.plotar(eixos)
dino_amarelo.plotar(eixos)
meteoro.plotar(eixos)
dino_verde.plotar(eixos)


animar_objetos(eixos, caminhando, frames=30, intervalo=0.01,
               objetos=(dino_azul, dino_amarelo, dino_verde, meteoro))

animar_objetos(eixos, extincao, frames=10, intervalo=0.01,
               objetos=(dino_azul, dino_amarelo, dino_verde, meteoro))

animar_objetos(eixos, ao_infinito, frames=10, intervalo=0.01,
               objetos=(dino_azul, dino_amarelo, dino_verde, meteoro))

# Exibir a plotagem
plt.show()
