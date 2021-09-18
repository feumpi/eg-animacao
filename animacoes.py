import matplotlib.pyplot as plt
from transformacoes import translacao, rotacao_x, rotacao_y, rotacao_z


def meia_volta_descer(i, objeto, frames, eixos):

    # Incrementos/frame de rotação e translação (total desejado / parte dos frames em que elas ocorrem, nesse caso metade)
    inc_rot = 180 / (frames / 2)
    inc_t = 100 / (frames / 2)

    # Até a metade
    if i < (frames/2):
        objeto.transformar(rotacao_z(inc_rot))

    # Depois da metade
    else:
        objeto.transformar(translacao(-inc_t, -inc_t, -inc_t))

    return objeto.plotar(eixos, 'seagreen')


def ao_infinito(i, objeto, frames, eixos):

    inc_t = 1000 / frames

    objeto.transformar(translacao(inc_t, inc_t, inc_t))

    return objeto.plotar(eixos, 'seagreen')
