class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.dade = idade


class Jogador(Pessoa):
    def __init__(self, nome: str, idade: int, numero_camisa: int, posicao: [str]):
        super().__init__(nome, idade)
        self.numero_camisa = numero_camisa
        self.posicao = posicao


class Tecnico(Pessoa):
    def __init__(self, nome: str, idade: int):
        super().__init__(nome, idade)


class Torcedor(Pessoa):
    def __init__(self, nome: str, idade: int):
        super().__init__(nome, idade)


class Juiz(Pessoa):
    def __init__(self, nome: str, idade: int):
        super().__init__(nome, idade)


class Time:
    def __init__(self, nome: str, apelido: str, tecnico: Tecnico, jogadores: [Jogador], torcedores: [Torcedor]):
        self.nome = nome
        self.apelido = apelido
        self.tecnico = tecnico
        self.jogadores = jogadores
        self.orcedores = torcedores


class Acao:
    def __init__(self, nome: str):
        self.nome = nome

    def __call__(self):
        print(f'Ação {self.nome} foi acionada')


class Gol(Acao):
    def __init__(self, jogador: Jogador, time: Time):
        super().__init__('Gol')
        self.jogador = jogador
        self.time = time

    def __call__(self):
        print(f'Ação {self.nome} foi acionada.\n O jogador {self.jogador.nome} fez um gol pelo time {self.time.nome}')


class Falta(Acao):
    def __init__(self, jogador: Jogador, time_benificiado: Time):
        super().__init__('Falta')
        self.jogador = jogador
        self.time_benificiado = time_benificiado

    def __call__(self):
        print(f'Ação {self.nome} foi acionada.\n')
        print(f'O jogador {self.jogador.nome} fez uma falta contra o time {self.time_benificiado.nome}')


class Escanteio(Acao):
    def __init__(self, time_benificiado: Time):
        super().__init__('Escanteio')
        self.time_benificiado = time_benificiado

    def __call__(self):
        print(f'Ação {self.nome} foi acionada.\n')
        print(f'O time {self.time_benificiado.nome} cobrou escanteio')


class SaidaBola(Acao):
    def __init__(self, time: Time):
        super().__init__('Saída de Bola')
        self.time = time

    def __call__(self):
        print(f'Ação {self.nome} foi acionada.\n')
        print(f'O time {self.time.nome} saiu jogando bola')


class Placar:
    def __init__(self, placar_time_mandante: int, placar_time_visitante: int):
        self.__placar_time_mandante = placar_time_mandante
        self.__placar_time_visitante = placar_time_visitante


class Jogo:
    def __init__(self, time_mandante: Time, time_visitante: Time, placar: Placar, juiz: Juiz):
        self.__time_mandante = time_mandante
        self.__time_visitante = time_visitante
        self.__placar = placar
        self.__juiz = juiz
