def forma_linha():  # Imprime linha com o caractere =
    print('=' * 60)


def p():  # Pula uma linha
    print('\n')


def cabecalhoI():  # Imprime o cabeçalho inicial do jogo
    forma_linha()
    print((' ' * 5)+'\033[91m' +
          'BEM-VINDO AO JOGO DA SEGURANÇA DA INDÚSTRIA PRYSMIAN GROUP ' + '\033[0m')
    forma_linha()


def escolher_cor(cor, texto):
    if cor == 'red':
        return f'\033[91m {texto} \033[0m'

    if cor == 'blue':
        return f'\033[94m {texto} \033[0m'

    if cor == 'yellow':
        return f'\033[93m {texto} \033[0m'

    if cor == 'green':
        return f'\033[92m {texto} \033[0m'
