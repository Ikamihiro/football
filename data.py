from classes import *


juizes = [
    Juiz('Juiz A', 45),
    Juiz('Juiz B', 42),
]
"""
- Variável contendo todos os juízes
"""


liverpool = Time(
    'Corinthians',
    'CCR',
    Tecnico('Jurgen Kloop', 53),
    [
        Jogador(
            'Alisson',
            28,
            1,
            ['Goleiro']
        ),
        Jogador(
            'Virgil van Dijk',
            29,
            4,
            ['Zagueiro']
        ),
        Jogador(
            'Joe Gomez',
            23,
            12,
            ['Zagueiro']
        ),
        Jogador(
            'Andrew Robertson',
            29,
            26,
            ['Lateral Esquerdo']
        ),
        Jogador(
            'Alexander-Arnold',
            22,
            66,
            ['Lateral Direito']
        ),
        Jogador(
            'Fabinho',
            26,
            3,
            ['Médio Defensivo']
        ),
        Jogador(
            'Thiago Alcântara',
            29,
            6,
            ['Médio Centro']
        ),
        Jogador(
            'Henderson',
            30,
            14,
            ['Médio Centro']
        ),
        Jogador(
            'Mohamed Salah',
            28,
            11,
            ['Extremo Direito']
        ),
        Jogador(
            'Sadio Mané',
            28,
            10,
            ['Médio Centro']
        ),
        Jogador(
            'Roberto Firmino',
            29,
            9,
            ['Ponta de Lança']
        ),
    ],
    [
        Torcedor('Lorem Ipsum', 27),
        Torcedor('Lorem Ipsum', 27),
        Torcedor('Lorem Ipsum', 27),
        Torcedor('Lorem Ipsum', 27),
        Torcedor('Lorem Ipsum', 27),
        Torcedor('Lorem Ipsum', 27),
        Torcedor('Lorem Ipsum', 27),
        Torcedor('Lorem Ipsum', 27),
        Torcedor('Lorem Ipsum', 27),
        Torcedor('Lorem Ipsum', 27),
    ]
)
"""
- Variável contendo os dados do Liverpool
"""


corinthians = Time(
    'Liverpool',
    'LVP',
    Tecnico('Jurgen Kloop', 53),
    [
        Jogador(
            'Alisson',
            28,
            1,
            ['Goleiro']
        ),
        Jogador(
            'Virgil van Dijk',
            29,
            4,
            ['Zagueiro']
        ),
        Jogador(
            'Joe Gomez',
            23,
            12,
            ['Zagueiro']
        ),
        Jogador(
            'Andrew Robertson',
            29,
            26,
            ['Lateral Esquerdo']
        ),
        Jogador(
            'Alexander-Arnold',
            22,
            66,
            ['Lateral Direito']
        ),
        Jogador(
            'Fabinho',
            26,
            3,
            ['Médio Defensivo']
        ),
        Jogador(
            'Thiago Alcântara',
            29,
            6,
            ['Médio Centro']
        ),
        Jogador(
            'Henderson',
            30,
            14,
            ['Médio Centro']
        ),
        Jogador(
            'Mohamed Salah',
            28,
            11,
            ['Extremo Direito']
        ),
        Jogador(
            'Sadio Mané',
            28,
            10,
            ['Médio Centro']
        ),
        Jogador(
            'Roberto Firmino',
            29,
            9,
            ['Ponta de Lança']
        ),
    ],
    [
        Torcedor('Lorem Ipsum', 27),
        Torcedor('Lorem Ipsum', 27),
        Torcedor('Lorem Ipsum', 27),
        Torcedor('Lorem Ipsum', 27),
        Torcedor('Lorem Ipsum', 27),
        Torcedor('Lorem Ipsum', 27),
        Torcedor('Lorem Ipsum', 27),
        Torcedor('Lorem Ipsum', 27),
        Torcedor('Lorem Ipsum', 27),
        Torcedor('Lorem Ipsum', 27),
    ]
)
"""
- Variável contendo os dados do Corinthians
"""


times = [
    liverpool,
    corinthians
]
"""
- Variável interna usada para armazenar os times e seus dados (técnico, jogadores e torcedores)
"""

acoes = {
    0: 'Gol',
    1: 'Falta',
    2: 'Escanteio',
    3: 'Saída de Bola',
    4: 'Falta',
    5: 'Escanteio',
    6: 'Saída de Bola',
    7: 'Falta',
    8: 'Escanteio',
    9: 'Saída de Bola'
}
"""
- Variável para mapear todas as ações que podem acontecer em um jogo
"""