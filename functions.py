import random
from typing import Dict
from data import times, juizes
from classes import Time, Jogo, Placar, Gol


def iniciar_times() -> Dict[str, Time]:
    """
    - Função que seleciona dois times de forma aleatória para se enfrentarem

    - Dispara uma Exception caso a lista **times** possua menos que dois times

    :return: Dict[str, Time]
    """

    if len(times) <= 1:
        raise Exception('Não dá pra inicar um jogo só com um time')

    # Embaralha a lista de times
    random.shuffle(times)

    # Selecione uma posição da lista aleatoriamente
    # para pegar o time mandante
    time_mandante_posicao = random.randrange(0, len(times))

    # Selecione uma posição da lista aleatoriamente
    # para pegar o time visitante
    time_visitante_posicao = random.randrange(0, len(times))

    # Verifica se a posição do mandante e visitante é
    # a mesma posição
    while time_visitante_posicao == time_mandante_posicao:
        time_visitante_posicao = random.randrange(0, len(times))

    # Pega o time mandante na posição selecionada
    time_mandamante = times[time_mandante_posicao]
    # Pega o time vistante na posição selecionada
    time_visitante = times[time_visitante_posicao]

    # Retorna um Dict contendo os times que irão duelar
    return dict(mandante=time_mandamante, visitante=time_visitante)


def iniciar_jogo(time_mandante: Time, time_visitante: Time) -> Jogo:
    """
    - Recebe como parâmetro o Time Mandante e o Time Visitante e instancia um Jogo

    - Caso os times não tenham 11 jogadores, lança uma Exception

    :param time_mandante: Time
    :param time_visitante: Time
    :return: Jogo
    """
    # Verificando se os times tem exatamente 11 jogadores
    if len(time_mandante.jogadores) != 11 or len(time_visitante.jogadores) != 11:
        raise Exception('Para iniciar o jogo, ambos os times tem que ter 11 jogadores')

    juiz = random.choice(juizes)

    # Cria um objeto Jogo
    jogo = Jogo(
        time_mandante,
        time_visitante,
        Placar(0, 0),
        juiz
    )

    # Retorna o objeto instanciado
    return jogo


def pegar_acao_aleatoria(__i: int) -> int:
    if (__i == 1) or (__i == 45):
        return 4
    return random.randrange(0, 9)


def pegar_time_aleatorio(__times: []) -> Time:
    return random.choice(__times)


def pegar_jogador_aleatorio(__time_selecionado: Time):
    __jogadores = __time_selecionado.jogadores
    return random.choice(__jogadores)


def verificar_possibilidade_gol() -> bool:
    possibilidade = random.randint(0, 10)
    if possibilidade > 6:
        return True
    return False


def exibir_placar(jogo: Jogo) -> None:
    print(f'\n{jogo.time_mandante.nome} | {jogo.placar.placar_time_mandante} ', end='X')
    print(f' {jogo.placar.placar_time_visitante} | {jogo.time_visitante.nome}\n')


def atualizar_placar(jogo: Jogo, gol: Gol) -> None:
    if gol.time == jogo.time_mandante:
        jogo.placar.placar_time_mandante += 1
    else:
        jogo.placar.placar_time_visitante += 1
