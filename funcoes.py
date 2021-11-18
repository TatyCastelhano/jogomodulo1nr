from os import system, name
import formatacao
import mensagens

def clear():
  # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def sai_do_jogo():  # Encerra o aplicativo
    exit()


def jogar():  # Dá a opção para o usuário continuar no jogo ou sair
    letra_S = False

    while letra_S == False:
        formatacao.forma_linha()
        joga = input(
            'Deseja continuar? Digite S para Sim ou N para sair do jogo: ')
        formatacao.forma_linha()
        if joga == 'S' or joga == 's':
            letra_S = True
            pass
        elif joga == 'N' or joga == 'n':
            sai_do_jogo()
        else:
            print(mensagens.mensagem_erro())
            letra_S = False


def entrada():  # Coleta do usuário a entrada para escolha do personagem
    seletor = 0        
    atende = False
    
    while atende == False:
        escolha = input('Escolha um dos personagens acima (letra A, B ou C): ')

        if escolha == 'A' or escolha == 'a':
            personagem = 'Gabriel '
            atende = True
            seletor = 1

        elif escolha == 'B' or escolha == 'b':
            personagem = 'Gustavo'
            atende = True
            seletor = 2

        elif escolha == 'C' or escolha == 'c':
            personagem = 'Teodoro'
            atende = True
            seletor = 3

        else:
            mensagem_erro = 'Digite corretamente apenas letras A, B ou C!'
            print(formatacao.escolher_cor(mensagens.cor_alerta, mensagem_erro))

        if(atende == True):
            print(mensagens.personagem_escolhido(personagem))
            if seletor == 1:
                caminho_personagem1()  
            elif seletor == 2:
                caminho_personagem2()
            elif seletor == 3:
                caminho_personagem3()

def reinicio(): # Em caso de game over retorna ao menu principal ou sai do jogo
    texto = 'Deseja jogar novamente? Digite S para continuar ou tecle Enter para encerrar: '
    formatacao.forma_linha()
    reinicia = input(formatacao.escolher_cor('yellow', texto))
    if reinicia == 'S' or reinicia == 's':
        clear()
        mensagens.escolha_personagem()
        entrada()
    else:
        sai_do_jogo()



        
def caminho_personagem1():
    def fase_tres():
        print('Essa é a Fase 3: ')
        print('Você precisa usar um equipamento de segurança  EPI para altura NR 35 e: ')
        formatacao.p()
        print('[A] Coloca o equipamento de segurança la em cima ')
        print('[B] Se prepara colocando os equipamentos antes de subir')
        
        resposta = False

        while resposta == False:
            final_fase3 = input('Digite A ou B para informar sua decisão: ')

            if final_fase3 == 'A' or final_fase3 == 'a':
                escolha_errada = 'Você escolheu a resposta errada e como consequência você poderá cair e sofrer uma queda brutal'
                print(formatacao.escolher_cor(mensagens.cor_erro, escolha_errada))
                resposta = True 
                reinicio()

            elif final_fase3 == 'B' or final_fase3 == 'b':
                escolha_certa = (('=')*60+
                '\n' +(' ' *25) +'PARABÉNS!!!'
                '\n' + (' ' *15) + 'VOCÊ ESCOLHEU A RESPOSTA CORRETA!!!'
                '\n' + (' ' *22) + 'VOCÊ GANHOU O JOGO!!!!'
                '\n' + ('=')*60)
                print(formatacao.escolher_cor(mensagens.cor_sucesso, escolha_certa))
                resposta = True 
                reinicio()
            else:
                mensagem_erro = 'Digite corretamente apenas letras A ou B!'
                print(formatacao.escolher_cor(mensagens.cor_alerta, mensagem_erro))
                resposta = False
    def fase_dois():
        print('Essa é a Fase 2: ')
        print('Você precisa fazer um serviço em espaço confinado fluvial, qual Epi será necessario?')
        formatacao.p()
        print('[A] Não é necessário mais nada, devo iniciar imediatamente!')
        print('[B] Devo preencher a Permissão para Trabalho Perigoso, usar botas de borracha para se proteger evitando dessa forma a proliferação de doenças,'
        '\nquedas, escorregões e, além disso, melhorando a qualidade da mobilidade ')
                
        resposta = False

        while resposta == False:
            final_fase2 = input('Digite A ou B para informar sua decisão: ')

            if final_fase2 == 'A' or final_fase2 == 'a':
                escolha_errada = 'Você escolheu a resposta errada e como consequência você poderá ser infectado com doenças ,quedas etc'
                print(formatacao.escolher_cor(mensagens.cor_erro, escolha_errada))
                resposta = True
                reinicio()
            elif final_fase2 == 'B' or final_fase2 == 'b':
                escolha_certa = (('=')*60+
                '\n' +(' ' *25) +'PARABÉNS!!!'
                '\n' + (' ' *15) + 'VOCÊ ESCOLHEU A RESPOSTA CORRETA!!!'
                '\n' + (' ' *10) + 'O PREENCHIMENTO DA PTP É OBRIGATÓRIO E ASSEGURA '
                '\n' + (' ' *10) + 'QUE TODAS AS ÁREAS SEJAM INFORMADAS DO SERVIÇO. '
                '\n' + ('=')*60)
                print(formatacao.escolher_cor(mensagens.cor_sucesso, escolha_certa))
                resposta = True
                reinicio()
                fase_tres()
            else:
                mensagem_erro = 'Digite corretamente apenas letras A ou B!'
                print(formatacao.escolher_cor(mensagens.cor_alerta, mensagem_erro))
                resposta = False
    def fase_um():
        print('=' * 60)
        print('Você foi chamado para receber e analisar Combustíveis Líquidos e Inflamáveis qual a prevenção e controle de risco deve fazer ?')
        formatacao.p()
        print('[A] As analises devem ser coordenadas  por um profissional habilitado')
        print('[B] Preencher ficha de inspeção e usar mascaras'
        '\n')
            
        resposta = False

        while resposta == False:
            final_fase1 = input('Digite A ou B para informar sua decisão: ')

            if final_fase1 == 'B' or final_fase1 == 'b':
                escolha_errada = 'Você escolheu a resposta errada pois tem q ser feito com um especialista '
                print(formatacao.escolher_cor(mensagens.cor_erro, escolha_errada))
                resposta = True
                reinicio()
            elif final_fase1 == 'A' or final_fase1 == 'a':
                escolha_certa = (('=')*60 +
                '\n' +(' ' *25) +'PARABÉNS!!!'
                '\n' + (' ' *15) + 'VOCÊ ESCOLHEU A RESPOSTA CORRETA!!!'
                '\n' + (' ' *10) + 'TODO SERVIÇO DE RISCO DEVE SER ACOMPANHADO POR  '
                '\n' + (' ' *10) + 'UM PROFISSIONAL RESPONSAVEL. '
                '\n' + (' ' *10) + 'VOCÊ AVANÇOU PARA A FASE 2, BOA SORTE!!!'
                '\n' + ('=')*60)
                print(formatacao.escolher_cor(mensagens.cor_sucesso, escolha_certa))
                resposta = True
                reinicio()
                fase_dois()
            else:
                mensagem_erro = 'Digite corretamente apenas letras A ou B!'
                print(formatacao.escolher_cor(mensagens.cor_alerta, mensagem_erro))
                resposta = False 
    fase_um()
  
def caminho_personagem2():
    def fase_tres():
        print('Essa é a Fase 3: ')
        print('Você precisa realizar serviços em ceu aberto conforme a nr21  qual Epi deve usar ?: ')
        formatacao.p()
        print('[A] Começa a trabalhar imediatamente ')
        print('[B] usa protetor solar e oculos de preteção UVA UVB escuros  ')
        
        
        resposta = False

        while resposta == False:
            final_fase3 = input('Digite A ou B para informar sua decisão: ')

            if final_fase3 == 'A' or final_fase3 == 'a':
                escolha_errada = 'Você escolheu a resposta errada e como consequência você poderá ser queimado e causando uma insolaçao '
                print(formatacao.escolher_cor(mensagens.cor_erro, escolha_errada))
                resposta = True
                reinicio()

            elif final_fase3 == 'B' or final_fase3 == 'b':
                escolha_certa = (('=')*60+
                '\n' +(' ' *25) +'PARABÉNS!!!'
                '\n' + (' ' *15) + 'VOCÊ ESCOLHEU A RESPOSTA CORRETA!!!'
                '\n' + (' ' *22) + 'VOCÊ GANHOU O JOGO!!!!'
                '\n' + ('=')*60)
                print(formatacao.escolher_cor(mensagens.cor_sucesso, escolha_certa))
                resposta = True
                reinicio()
            else:
                mensagem_erro = 'Digite corretamente apenas letras A ou B!'
                print(formatacao.escolher_cor(mensagens.cor_alerta, mensagem_erro))
                resposta = False
    def fase_dois():
        print('Essa é a Fase 2: ')
        print('Quais são os agentes de risco ambientais? ')
        formatacao.p()
        print('[A] Não tem agentes de riscos !')
        print('[B] Agentes quimicos e biologicos ')
    
        
        resposta = False

        while resposta == False:
            final_fase2 = input('Digite A ou B para informar sua decisão: ')

            if final_fase2 == 'A' or final_fase2 == 'a':
                escolha_errada = 'Você escolheu a resposta errada !'
                print(formatacao.escolher_cor(mensagens.cor_erro, escolha_errada))
                resposta = True
                reinicio()
            elif final_fase2 == 'B' or final_fase2 == 'b':
                escolha_certa = (('=')*60+
                '\n' +(' ' *25) +'PARABÉNS!!!'
                '\n' + (' ' *15) + 'VOCÊ ESCOLHEU A RESPOSTA CORRETA!!!'
                '\n' + (' ' *10) + 'OS RISCOS AMBIENTAIS EXISTENTES SÃO : '
                '\n' + (' ' *10) + 'QUIMICOS E BIOLOGICOS  '
                '\n' + ('=')*60)
                print(formatacao.escolher_cor(mensagens.cor_sucesso, escolha_certa))
                resposta = True
                reinicio()
                fase_tres()
            else:
                mensagem_erro = 'Digite corretamente apenas letras A ou B!'
                print(formatacao.escolher_cor(mensagens.cor_alerta, mensagem_erro))
                resposta = False
    def fase_um():
        print('=' * 60)
        print('Quais sao as atividades e operações insalubres ?')
        formatacao.p()
        print('[A] Não tem atividade insalubre ')
        print('[B] Agentes biologicos, trabalho sobre vibração, trabalho ar comprimido')
       
            
        resposta = False

        while resposta == False:
            final_fase1 = input('Digite A ou B para informar sua decisão: ')

            if final_fase1 == 'A' or final_fase1 == 'a':
                escolha_errada = 'Você escolheu a resposta errada !'
                print(formatacao.escolher_cor(mensagens.cor_erro, escolha_errada))
                resposta = True
                reinicio()
            elif final_fase1 == 'B' or final_fase1 == 'b':
                escolha_certa = (('=')*60 +
                '\n' +(' ' *25) +'PARABÉNS!!!'
                '\n' + (' ' *15) + 'VOCÊ ESCOLHEU A RESPOSTA CORRETA!!!'
                '\n' + (' ' *10) + 'OPERAÇOES INSALUBRES SAO TODAS AS ATIVIDADES QUE ENVOLVEM  '
                '\n' + (' ' *10) + 'RISCO DE VIDA OU DE INVALIDEZ . '
                '\n' + (' ' *10) + 'VOCÊ AVANÇOU PARA A FASE 2, BOA SORTE!!!'
                '\n' + ('=')*60)
                print(formatacao.escolher_cor(mensagens.cor_sucesso, escolha_certa))
                resposta = True
                loop_erro = False
                while loop_erro == False:
                    continua = input('Digite S para continuar para a fase 2: ')
                    if continua == 'S' or continua == 's':
                        loop_erro = True
                        fase_dois()
                    else:
                        print(formatacao.escolher_cor(mensagens.cor_alerta,'Digite somente S para continuar!'))
                        loop_erro = False

                resposta = True
                reinicio()
               
            else:
                mensagem_erro = 'Digite corretamente apenas letras A ou B!'
                print(formatacao.escolher_cor(mensagens.cor_alerta, mensagem_erro))
                resposta = False 
    fase_um()

def caminho_personagem3():
    def fase_tres():
        print('Essa é a Fase 3: ')
        print('Quais sao as condiçoes de trabalho conforme Nr 17?: ')
        formatacao.p()
        print('[A] Trabalho ao ar livre ')
        print('[B] Estabelecer parametros para permitir a adaptacao de trabalho ')
        
        
        resposta = False

        while resposta == False:
            final_fase3 = input('Digite A ou B para informar sua decisão: ')

            if final_fase3 == 'A' or final_fase3 == 'a':
                escolha_errada = 'Você escolheu a resposta errada '
                print(formatacao.escolher_cor(mensagens.cor_erro, escolha_errada))
                resposta = True
                reinicio()

            elif final_fase3 == 'B' or final_fase3 == 'b':
                escolha_certa = (('=')*60+
                '\n' +(' ' *25) +'PARABÉNS!!!'
                '\n' + (' ' *15) + 'VOCÊ ESCOLHEU A RESPOSTA CORRETA!!!'
                '\n' + (' ' *22) + 'VOCÊ GANHOU O JOGO!!!!'
                '\n' + ('=')*60)
                print(formatacao.escolher_cor(mensagens.cor_sucesso, escolha_certa))
                resposta = True
                reinicio()
            else:
                mensagem_erro = 'Digite corretamente apenas letras A ou B!'
                print(formatacao.escolher_cor(mensagens.cor_alerta, mensagem_erro))
                resposta = False
    def fase_dois():
        print('Essa é a Fase 2: ')
        print('Quais são as condições de trabalho a céu aberto? ')
        formatacao.p()
        print('[A] Não é necessário nada!')
        print('[B] È obrigatorio a existência de abrigos para proteger os trabalhadores ')
        
        
        resposta = False

        while resposta == False:
            final_fase2 = input('Digite A ou B para informar sua decisão: ')

            if final_fase2 == 'A' or final_fase2 == 'a':
                escolha_errada = 'Você escolheu a resposta errada '
                print(formatacao.escolher_cor(mensagens.cor_erro, escolha_errada))
                resposta = True
                reinicio()
            elif final_fase2 == 'B' or final_fase2 == 'b':
                escolha_certa = (('=')*60+
                '\n' +(' ' *25) +'PARABÉNS!!!'
                '\n' + (' ' *15) + 'VOCÊ ESCOLHEU A RESPOSTA CORRETA!!!'
                '\n' + (' ' *10) + 'A NECESSIDADE DE TER UM ABRIGO E TAMBEM  '
                '\n' + (' ' *10) + 'QUE TODAS AS ÁREAS SEJAM INFORMADAS DO SERVIÇO. '
                '\n' + ('=')*60)
                print(formatacao.escolher_cor(mensagens.cor_sucesso, escolha_certa))
                resposta = True
                reinicio()
                fase_tres()
            else:
                mensagem_erro = 'Digite corretamente apenas letras A ou B!'
                print(formatacao.escolher_cor(mensagens.cor_alerta, mensagem_erro))
                resposta = False
    def fase_um():
        print('=' * 60)
        print('Como deve ser as condições sanitarias conforme a  Nr21?')
        formatacao.p()
        print('[A] Trabalho Livre ')
        print('[B] Devem ser mantidos em condições sanitárias compativeis com o genero da atividade ')
       
            
        resposta = False

        while resposta == False:
            final_fase1 = input('Digite A ou B para informar sua decisão: ')

            if final_fase1 == 'A' or final_fase1 == 'a':
                escolha_errada = 'Você escolheu a resposta errada '
                print(formatacao.escolher_cor(mensagens.cor_erro, escolha_errada))
                resposta = True
                reinicio()
            elif final_fase1 == 'B' or final_fase1 == 'b':
                escolha_certa = (('=')*60 +
                '\n' +(' ' *25) +'PARABÉNS!!!'
                '\n' + (' ' *15) + 'VOCÊ ESCOLHEU A RESPOSTA CORRETA!!!'
                '\n' + (' ' *10) + 'DEVEM SER MANTIDOS EM PERFEITAS CONDIÇÕES SANITÁRIAS  '
                '\n' + (' ' *10) + 'VOCÊ AVANÇOU PARA A FASE 2, BOA SORTE!!!'
                '\n' + ('=')*60)
                print(formatacao.escolher_cor(mensagens.cor_sucesso, escolha_certa))
                resposta = True
                
                loop_erro = False
                while loop_erro == False:
                    continua = input('Digite S para continuar para a fase 2: ')
                    if continua == 'S' or continua == 's':
                        loop_erro = True
                        fase_dois()
                    else:
                        print(formatacao.escolher_cor(mensagens.cor_alerta,'Digite somente S para continuar!'))
                        loop_erro = False

                       
            else:
                mensagem_erro = 'Digite corretamente apenas letras A ou B!'
                print(formatacao.escolher_cor(mensagens.cor_alerta, mensagem_erro))
                resposta = False 
    fase_um()
    


   