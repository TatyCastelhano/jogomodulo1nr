import formatacao, funcoes

cor_erro = "red"
cor_principal = "blue"
cor_alerta = 'yellow'
cor_sucesso = 'green'


def boas_vindas():  # Exibe a mensagem inicial do jogo
    print('A Indústria Prysmian  produz uma grande variedade de cabos para telecomunicação de'
          '\nbugigangas elétricas e, como tal, possui vários riscos associados em seu'
          '\nprocesso produtivo.')
    print(' ')
    print('Ela possui 3 funcionários polivalentes, responsáveis pela operação,'
          '\nmanutenção e qualidade de seus equipamentos e instalações'
          '\nmas, eles são muito resistentes as boas práticas de segurança no trabalho,'
          '\ne tal resistência acaba gerando consequências indesejáveis.')
    formatacao.p()
    print('Pois bem, cabe a você prezado usuário decidir sobre as escolhas desses'
          '\nfuncionários e sofrer com eles as consequências dessas escolhas!')


def escolha_personagem():  # Exibe mensagem na segunda tela do jogo
    right_arrow = formatacao.escolher_cor(cor_principal, '--->')

    print('***** Escolha um dos três funcionários abaixo: *****')
    formatacao.forma_linha()
    print('\n'
          + right_arrow + ' Gabriel - o mecânico - letra "A"'
          '\n'
          + right_arrow + ' Gustavo  - o eletricista - letra "B"'
          '\n'
          + right_arrow + ' Teodoro - o ajudante geral - letra "C"')
    formatacao.forma_linha()


def mensagem_erro():
    texto = 'Digite corretamente apenas letras S ou N!'
    return formatacao.escolher_cor(cor_alerta, texto)


def personagem_escolhido(personagem):
    return f"O funcionário escolhido foi o sr. {formatacao.escolher_cor(cor_sucesso, personagem)}"

def inicia_jogo():
      print('Ok vamos começar!')
   