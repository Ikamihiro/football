import random
import time

# Ações:
# 1 - Gol
# 2 - Falta
# 3 - Escanteio
# 4 - Saída de Bola
# 5 - Pênalti

acoes = {
    1: 'Gol',
    2: 'Falta',
    3: 'Escanteio',
    4: 'Saída de Bola',
    5: 'Pênalti',
}

i = 1
while i <= 90:
    acao = None

    if i == 1:
        print('\nApito inicial! O jogo começou!\n')
    elif i == 45:
        print(f'\n {i} minutos. Hora do Intervalo!\n')
        time.sleep(3.5)

    if(i == 1) or (i == 45):
        acao = 4
    else:
        acao = random.randrange(1, 5)

    lance = acoes.get(acao)
    print(lance)

    time.sleep(1.0)
    i = i + 1

print('\nApito final! Jogo encerrado!\n')
