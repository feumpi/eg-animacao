import matplotlib.pyplot as plt
from transformacoes import translacao, rotacao_x, rotacao_y, rotacao_z
from utilidades import ajustar_eixos


# Executa uma função de animação para os objetos nos eixos com duração e intervalo especificados
def animar_objetos(eixos, func_animacao, frames, intervalo, objetos):

    dinossauro, meteoro = objetos

    # Iteração de frames
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


# Rotaciona no próprio eixo, translada e depois rotaciona em relação a origem
def anim_teste(i, frames, objetos):

    dinossauro, meteoro = objetos

    # Incrementos por frame
    inc_r = 180 / (frames/3)
    inc_t = 200 / (frames/3)

    if(i < frames/3):  # Até 1/3 da animação
        dinossauro.transformar(rotacao_z(inc_r), origem=True)
        meteoro.transformar(rotacao_z(inc_r), origem=True)

    elif(i < 2*frames/3):  # Até 2/3 da animação
        dinossauro.transformar(translacao(inc_t, inc_t, inc_t))
        meteoro.transformar(translacao(-inc_t, -inc_t, -inc_t))

    else:  # Restante da animação
        dinossauro.transformar(rotacao_z(inc_r))
        meteoro.transformar(rotacao_z(inc_r))
