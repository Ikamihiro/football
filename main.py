import random
import time
# from datetime import datetime
from functions import *
from data import acoes
from classes import *


try:
    times = iniciar_times()
    time_mandante = times.get("mandante")
    time_visitante = times.get("visitante")
    jogo = iniciar_jogo(time_mandante, time_visitante)

    i = 1
    while i <= 90:
        acao = None
        time_selecionado = None
        jogador = None
        time_beneficiado = None
        acao_aleatorio = 0

        if i == 1:
            print('\nApito inicial! O jogo começou!\n')
        elif i == 45:
            print(f'\n {i} minutos. Hora do Intervalo!\n')
            time.sleep(3.5)

        acao_aleatorio = pegar_acao_aleatoria(i)

        lance = acoes.get(acao_aleatorio)

        if lance == 'Gol':
            time_selecionado = pegar_time_aleatorio([time_mandante, time_visitante])
            jogador = pegar_jogador_aleatorio(time_selecionado)
            acao = Gol(jogador, time_selecionado)

            print('Goool!!')
            # atualizar_placar(jogo, acao)
            jogo.atualizar_placar(acao)

        elif lance == 'Falta':
            time_beneficiado = pegar_time_aleatorio([time_mandante, time_visitante])
            jogador = pegar_jogador_aleatorio(time_beneficiado)
            acao = Falta(jogador, time_beneficiado)

        elif lance == 'Escanteio':
            time_beneficiado = pegar_time_aleatorio([time_mandante, time_visitante])
            acao = Escanteio(time_beneficiado)

        else:
            time_selecionado = pegar_time_aleatorio([time_mandante, time_visitante])
            acao = SaidaBola(time_selecionado)

        jogo.exibir_placar()
        acao()

        time.sleep(0.5)
        i = i + 1

    print('\nApito final! Jogo encerrado!\n')
except Exception as e:
    print(e.args)
finally:
    jogo.exibir_placar()
    # Exibir resultado final
