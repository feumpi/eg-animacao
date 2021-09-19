import matplotlib.pyplot as plt
from transformacoes import translacao, rotacao_x, rotacao_y, rotacao_z
from utilidades import ajustar_eixos


def animar_objetos(eixos, func_animacao, frames, intervalo, objetos):

    dinossauro, meteoro = objetos

    for i in range(frames):

        # Limpa a plotagem atual e reajusta os eixos
        plt.cla()
        ajustar_eixos(eixos, azimute=-45, elevacao=30, tamanho_x=500,
                      tamanho_y=500, tamanho_z=1000)

        # Aplica a função de animação para o frame atual
        func_animacao(i, frames, objetos=(dinossauro, meteoro))

        # Plota os novos objetos
        for objeto in objetos:
            objeto.plotar(eixos)

        # Pausa após o frame o intervalo especificado
        plt.pause(intervalo)


def anim_teste(i, frames, objetos):

    dinossauro, meteoro = objetos

    inc = 180 / (frames/2)
    inc_t = 200 / (frames/2)

    if(i < frames/3):

        dinossauro.transformar(rotacao_z(inc), origem=True)
        meteoro.transformar(rotacao_z(inc), origem=True)

    elif(i < 2*frames/3):
        dinossauro.transformar(translacao(inc_t, inc_t, inc_t))
        meteoro.transformar(translacao(-inc_t, -inc_t, -inc_t))

    else:
        dinossauro.transformar(rotacao_z(inc))
        meteoro.transformar(rotacao_z(inc), origem=True)
