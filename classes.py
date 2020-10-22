class Pessoa:
    """
    - Classe para representar os dados de uma **Pessoa**
    """
    def __init__(self, nome: str, idade: int):
        """
        - Construtor para a classe **Pessoa**
        :param nome: str
        :param idade: int
        """
        self.nome = nome
        self.dade = idade


class Jogador(Pessoa):
    """
    - Classe para representar os dados de um **Jogador**
    """
    def __init__(self, nome: str, idade: int, numero_camisa: int, posicao: [str]):
        """
        - Construtor para a classe **Jogador**
        :param nome: str
        :param idade: int
        :param numero_camisa: int
        :param posicao: [str]
        """
        super().__init__(nome, idade)
        self.numero_camisa = numero_camisa
        self.posicao = posicao


class Tecnico(Pessoa):
    """
    - Classe para representar os dados de um **Técnico**
    """
    def __init__(self, nome: str, idade: int):
        """
        - Construtor para a classe **Tecnico**
        :param nome: str
        :param idade: int
        """
        super().__init__(nome, idade)


class Torcedor(Pessoa):
    """
    - Classe para representar os dados de um **Torcedor**
    """
    def __init__(self, nome: str, idade: int):
        """
        - Construtor para a classe **Torcedor**
        :param nome: str
        :param idade: int
        """
        super().__init__(nome, idade)


class Juiz(Pessoa):
    """
    - Classe para representar os dados de um **Juiz**
    """
    def __init__(self, nome: str, idade: int):
        """
        - Construtor da classe **Juiz**
        :param nome: str
        :param idade: int
        """
        super().__init__(nome, idade)


class Time:
    """
    - Classe para representar os dados de um **Time**
    """
    def __init__(self, nome: str, apelido: str, tecnico: Tecnico, jogadores: [Jogador], torcedores: [Torcedor]):
        """
        - Construtor da classe **Time**
        :param nome: str
        :param apelido: str
        :param tecnico: Tecnico
        :param jogadores: [Jogador]
        :param torcedores: [Torcedor]
        """
        self.nome = nome
        self.apelido = apelido
        self.tecnico = tecnico
        self.jogadores = jogadores
        self.orcedores = torcedores


class Acao:
    """
    - Classe para representar os dados de uma **Ação**
    """
    def __init__(self, nome: str):
        """
        - Construtor para a classe **Acao**
        :param nome: str
        """
        self.nome = nome

    def __call__(self):
        """
        - Método para exibir a ação
        :return: None
        """
        print(f'Ação {self.nome} foi acionada')


class Gol(Acao):
    """
    - Classe para representar os dados de um **Gol**
    """
    def __init__(self, jogador: Jogador, time: Time):
        """
        - Construtor da classe **Gol**
        :param jogador: Jogador
        :param time: Time
        """
        super().__init__('Gol')
        self.jogador = jogador
        self.time = time

    def __call__(self) -> None:
        """
        - Método para exibir a ação
        :return: None
        """
        print(f'O jogador {self.jogador.nome} fez um gol pelo time {self.time.nome}')


class Falta(Acao):
    """
    - Classe para representar os dados de uma **Falta**
    """
    def __init__(self, jogador: Jogador, time_benificiado: Time):
        """
        - Construtor para a classe **Falta**
        :param jogador: Jogador
        :param time_benificiado: Time
        """
        super().__init__('Falta')
        self.jogador = jogador
        self.time_benificiado = time_benificiado

    def __call__(self) -> None:
        """
        - Método para exibir a ação
        :return: None
        """
        # print(f'Ação {self.nome} foi acionada.\n')
        print(f'O jogador {self.jogador.nome} fez uma falta contra o time {self.time_benificiado.nome}')


class Escanteio(Acao):
    """
    - Classe para representar os dados de um **Escanteio**
    """
    def __init__(self, time_benificiado: Time):
        """
        - Construtor para a classe **Escanteio**
        :param time_benificiado: Time
        """
        super().__init__('Escanteio')
        self.time_benificiado = time_benificiado

    def __call__(self) -> None:
        """
        - Método para exibir a ação
        :return: None
        """
        # print(f'Ação {self.nome} foi acionada.\n')
        print(f'O time {self.time_benificiado.nome} cobrou escanteio')


class SaidaBola(Acao):
    """
    - Classe para representar os dados de uma **Saída de Bola**
    """
    def __init__(self, time: Time):
        """
        - Construtor da classe **SaidaBola**
        :param time: Time
        """
        super().__init__('Saída de Bola')
        self.time = time

    def __call__(self) -> None:
        """
        - Método para exibir a ação
        :return: None
        """
        # print(f'Ação {self.nome} foi acionada.\n')
        print(f'O time {self.time.nome} saiu jogando bola')


class Placar:
    """
    - Classe para representar os dados de um **Placar**
    """
    def __init__(self, placar_time_mandante: int, placar_time_visitante: int):
        """
        - Construtor da classe **Placar**
        :param placar_time_mandante: int
        :param placar_time_visitante: int
        """
        self.placar_time_mandante = placar_time_mandante
        self.placar_time_visitante = placar_time_visitante


class Jogo:
    """
    - Classe para representar os dados de um **Jogo**
    """
    def __init__(self, time_mandante: Time, time_visitante: Time, placar: Placar, juiz: Juiz):
        """
        - Construtor da classe **Jogo**
        :param time_mandante: Time
        :param time_visitante: Time
        :param placar: Placar
        :param juiz: Juiz
        """
        self.time_mandante = time_mandante
        self.time_visitante = time_visitante
        self.placar = placar
        self.juiz = juiz

    def exibir_placar(self) -> None:
        """
        - Exibi o placar do **Jogo**
        :return: None
        """
        print(f'\n{self.time_mandante.nome} | {self.placar.placar_time_mandante} ', end='X')
        print(f' {self.placar.placar_time_visitante} | {self.time_visitante.nome}\n')

    def atualizar_placar(self, gol: Gol) -> None:
        """
        - Atualizar o placar do **Jogo** quando um time faz gol
        :param gol: Gol
        :return: None
        """
        if gol.time == self.time_mandante:
            self.placar.placar_time_mandante += 1
        else:
            self.placar.placar_time_visitante += 1
