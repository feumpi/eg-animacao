import matplotlib.pyplot as plt
from transformacoes import translacao, rotacao_x, rotacao_y, rotacao_z
from utilidades import ajustar_eixos


# Executa uma função de animação para os objetos nos eixos com duração e intervalo especificados
def animar_objetos(eixos, func_animacao, frames, intervalo, objetos):

    dino_azul, dino_amarelo, dino_verde, meteoro = objetos

    # Iteração de frames
    for i in range(frames):

        # Limpa a plotagem atual e reajusta os eixos
        plt.cla()
        ajustar_eixos(eixos, azimute=-45, elevacao=30, tamanho_x=500,
                      tamanho_y=500, tamanho_z=1000)

        # Aplica a função de animação para o frame atual
        func_animacao(i, frames, objetos=(
            dino_azul, dino_amarelo, dino_verde, meteoro))

        # Plota os novos objetos
        for objeto in objetos:
            objeto.plotar(eixos)

        # Pausa após o frame o intervalo especificado
        plt.pause(intervalo)


def caminhando(i, frames, objetos):
    dino_azul, dino_amarelo, dino_verde, meteoro = objetos

    inc_t = 600 / (frames/3)
    inc_r = -90 / (frames/3)

    inc_r2 = 180 / (frames/3)
    inc_t2 = 400 / (frames/3)

    if(i < frames/3):  # Até 1/3 da animação
        dino_azul.transformar(translacao(0, inc_t, 0))
        dino_amarelo.transformar(translacao(0, -inc_t, 0))
        dino_verde.transformar(rotacao_z(inc_r2), origem=True)

    elif(i < 2*frames/3):  # Até 2/3 da animação
        dino_azul.transformar(rotacao_z(inc_r), origem=True)
        dino_amarelo.transformar(rotacao_z(inc_r), origem=True)

    else:  # Restante da animação
        dino_azul.transformar(translacao(inc_t, 0, 0))
        dino_amarelo.transformar(translacao(-inc_t, 0, 0))
        dino_verde.transformar(translacao(-inc_t2, inc_t2, 0))


def extincao(i, frames, objetos):

    dino_azul, dino_amarelo, dino_verde, meteoro = objetos

    inc_t = 500 / frames
    inc_tz = 2500 / frames
    inc_r = (360*5) / frames

    meteoro.transformar(translacao(-inc_t, -inc_t, -inc_tz))
    meteoro.transformar(rotacao_z(inc_r), rotacao_x(inc_r), origem=True)


def ao_infinito(i, frames, objetos):

    dino_azul, dino_amarelo, dino_verde, meteoro = objetos

    inc_t = 500 / frames
    inc_tz = 1500 / frames
    inc_r = 180 / frames

    dino_azul.transformar(translacao(inc_t, inc_t, inc_tz))
    dino_azul.transformar(rotacao_x(inc_r), rotacao_z(inc_r), origem=True)

    dino_amarelo.transformar(translacao(-inc_t, -inc_t, inc_tz))
    dino_amarelo.transformar(rotacao_x(-inc_r), rotacao_z(-inc_r), origem=True)

    dino_verde.transformar(translacao(-inc_t, inc_t, inc_tz))
    dino_amarelo.transformar(rotacao_y(inc_r), origem=True)
