import pygame
from pygame import mixer
from random import randint
from time import sleep


pygame.init()
mixer.init()


# Configura a colisão das naves e balas
def colisao():
    global pontuacao, pos_x_inimigo, pos_y_inimigo, player_rect, inimigo_rect
    global random_y, random_x, pos_y_player,nave_player_morreu

    # Se a nave do player colidir com a nave inimiga, ele morrerá

    if player_rect.colliderect(inimigo_rect):
        pos_y_player = 100000 
        nave_player_morreu = True
        som_derrota_pum = pygame.mixer.Sound("pum.mp3")
        som_derrota_pum.play()
    if inimigo_rect.y > 500:
        pontuacao -= 5
        print(pontuacao)
        return True





    # Se o missil lançado pelo player acertar a nave inimiga, ele ganhará
    # Pontos e a nave inimiga "desaparecerá" por um breve instante
    elif missil_rect.colliderect(inimigo_rect):
        pontuacao += 5
        pos_y_inimigo -= 1200        
        som_explosao = pygame.mixer.Sound("som_explosao5.mp3")
        som_explosao.play()
        if pos_y_inimigo < -1000:
            random_y = randint(1,1)
            random_x = randint(1, 870)
            pos_y_inimigo -= 450
            pos_y_inimigo = random_y
            pos_x_inimigo = random_x
        print(pontuacao) # VERIFICAR
        return 
        
    else:
        return False


def VerificaSeArquivoExiste():
    from os import path
    
    if not path.isfile("score.txt"):
        try:
            arquivo = open("score.txt", "a+")
        except:
            print(f"\033[1;31mOcorreu um erro ao criar o arquivo\033[m")

        else:
            print("\033[1;32mArquivo criado com sucesso!\033[m")

        finally:
            arquivo.close()


def MarcaPontos(pontos): # arrumar código da função
    global segundos, situacao
    situacao = ' '
    from datetime import datetime

    horario = datetime.now()
    
    try:
        arquivo = open("score.txt", "a")

    except (FileNotFoundError):
        print("\033[1;31mOcorreu um erro ao escrever no arquivo.\033[m")
    
    else:
        if segundos >= 300: #300
            situacao = "vitória"
        else:
            situacao = "derrota"

        arquivo.write(f"{segundos} segundos {pontos:>10}{situacao:>15}\n")
    

   
         # Define a fonte do tempo


def MostraTextoNaTela(texto1='', texto2='', posx=0, posy=0, tamanho_fonte=10, vermelho=0, verde=255, azul=0, atualizar_tela=True, tempo_tela_congelada=0):
    ''' --> Mostra um texto na tela
    :param texto1: texto que você quer que apareça na tela.Ex: "pontos: ", "tempo:", "vitórias: "
    :param texto2: o texto que você quer mostrar na tela (depende do desempenho do jogador no jogo).Ex: 20, 30 (pontos)
    :param posx: a posição em que o texto ficará no eixo x
    :param posy: a posição em que o texto ficará no eixo y
    :param tamanho_fonte: tamanho da fonte do texto que aparecerá na tela
    :param vermelho: cor do texto a aparecer na tela (vermelho)
    :param verde: cor do texto a aparecer na tela (verde)
    :param azul: cor do textoa aparecer na tela (azul)
    :param atualizar_tela: atualiza ou não a tela
    :param tempo_tela_congelada: (opcional) congela ou não a tela
    :return: sem retorno
    '''
    from time import sleep
    # Define a fonte do tempo
    font2 = pygame.font.Font("freesansbold.ttf", tamanho_fonte)
    # Concatena a string "tempo" com a string "segundos"
    if str(texto2).strip() == '':
        tempo = font2.render(f"{texto1}", True, (vermelho,verde,azul), (0,0,0))
    else:
        tempo = font2.render(f"{texto1}: " + str(texto2), True, (0,255,0), (0,0,0))
    # O retângulo que ficará em volta do tempo
    tempo_rect = tempo.get_rect()
    # Posição do retângulo do tempo
    tempo_rect.center = (posx, posy)
    janela.blit(tempo, (tempo_rect))

    #atualiza a tela
    if atualizar_tela:
        pygame.display.update()

    #congela a tela
    if tempo_tela_congelada:
        pygame.display.update()
        sleep(tempo_tela_congelada)

#define o tamanho da janela (800X600 no caso)
janela = pygame.display.set_mode((960, 540)) 
VerificaSeArquivoExiste()





#define o título da janela
pygame.display.set_caption("Invasão Alien") 


# Carrega a música de fundo do game
musica = pygame.mixer.music.load("musica_espaço_sideral2.mp3")

# Define o volume do som
# Toca a música
mixer.music.play()
#Carrega a imagem do plano de fundo do jogo
background_image = pygame.image.load("/home/luffy/Documentos/programação/python/ataque_alien/background.png")
#Carrega a imagem da nave do player
nave_player = pygame.image.load("nave_pequena.png")
#Carrega a imagem da nave inimiga
nave_inimiga = pygame.image.load("nave_inimiga_pequena.png")
#Carrega o míssil
missil = pygame.image.load("missil pequeno.png")
# Altera o tamanho da imagem para 30X30
missil = pygame.transform.scale(missil, (30,30))



#posição da nave do player
pos_x_player = 400
pos_y_player = 430
#velocidade da nave do player
vel_nave_player = 12 #12

#posição da nave inimiga
pos_x_inimigo = 400
pos_y_inimigo = 50

#Velocidade da nave do inimigo
vel_nave_inimigo = 2

#Velocidade do missil
vel_missil = 30 #30
# Posição do missil
pos_x_missil = pos_x_player
pos_y_missil = pos_y_player

pontuacao = contador = tempo = segundos = 0




tiro_alvo = nave_player_morreu =  False


loop = True

#Mantém a janela do jogo aberta enquanto o usuário não clicar em "fechar" ("x")
while loop:
    contador += 1

    if (contador == 24):  #24
        segundos += 1
        contador = 0


    # Define a fonte do tempo
    

    #MostraTextoNaTela("Tempo: ", segundos, 54, 40, 18)

    # Primeiro argumento: é a fonte, segundo argumento: tamanho da fonte
   
    #MostraTextoNaTela("Pontuação", pontuacao, 75, 100, 18)


    
   

    
    # Reage as teclas pressionadas pelo usuário
    teclas = pygame.key.get_pressed()

    # Para cada evento/ação realizada pelo usuário na janela, se o usuário cliclar no "X" ou clicar na tecla "E", o jogo irá fechar
    for events in pygame.event.get():
        if events.type == pygame.QUIT or teclas[pygame.K_q] or nave_player_morreu or segundos >= 300:
            MarcaPontos(pontuacao)
            sleep(1)
            if situacao == "derrota":
                MostraTextoNaTela(f'{situacao}'.upper(), "", 473, 175, 40,vermelho=255, verde=0, atualizar_tela=False)#150
            else:
                MostraTextoNaTela(f'{situacao}'.upper(), "", 473, 175, 40,verde=255, atualizar_tela=False)#150
            MostraTextoNaTela("Pontuação", pontuacao, 483, 245, 35, atualizar_tela=False) #220
            MostraTextoNaTela("Tempo", segundos, 450, 300, 35, tempo_tela_congelada=10) #275
            loop = False



   
    
    # Se o tempo de jogo bater 60 segundos (1 minuto), a velocidade da nave inimiga aumenta
    if segundos == 60:
        vel_nave_inimigo = 6

    # Se o tempo de jogo bater 120 segundos (2 minuto), a velocidade da nave inimiga aumenta
    elif segundos == 120:
        vel_nave_inimigo = 10

    # Se o tempo de jogo bater 180 segundos (3 minuto), a velocidade da nave inimiga aumenta
    elif segundos == 180:
        vel_nave_inimigo = 14

    # Se o tempo de jogo bater 240 segundos (4 minuto), a velocidade da nave inimiga aumenta
    elif segundos == 240:
        vel_nave_player = 15
        vel_nave_inimigo = 20
    



    # Faz a nave inimiga se movimentar
    pos_y_inimigo += vel_nave_inimigo

    # Se a nave inimiga tiver ultrapassado o limite da região da jenela do
    #jogo, então a nave inimiga irá respawnar (aparecer) em uma posição 
    #aleatória na tela
    if pos_y_inimigo > 530:
        # Sorteia a posição "y" da nave inimiga
        random_y = 1
        # Sorteia a posição "x" da nave inimiga 
        random_x = randint(1,870)
        pos_y_inimigo -= 450
        pos_y_inimigo = random_y
        pos_x_inimigo = random_x

    

    # Nave vai para cima se a tecla pressionada for a seta para cima
    if teclas[pygame.K_UP] or teclas[pygame.K_w]:
        pos_y_player -= vel_nave_player

    # Nave vai para baixo se a tecla pressionada for a seta para baixo
    if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
        pos_y_player += vel_nave_player

    # Nave vai para a esqueda se a tecla pressionada for a seta para a esquerda
    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        pos_x_player -= vel_nave_player

    # Nave vai para a direita se a tecla pressionada for a tecla para a direita
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        pos_x_player += vel_nave_player 

    # Nave do player vai tirar caso a tecla pressionado seja o "ESPAÇO" ou "z"
    if teclas[pygame.K_SPACE] or teclas[pygame.K_z]:
        tiro_alvo = True
        som_tiro_nave = pygame.mixer.Sound("som de tiro da nave.mp3")
        if (pos_y_missil  - pos_y_player  < 60):
            som_tiro_nave.play()
        
            
        # Se o missil atirado pelo player ultrapassar a margem da tela,
        # Ele vai voltar para a posição do jogador para que possamos atirar
        # Novamente
        if pos_y_missil < 1:
            #mixer.music.play()
            pos_y_missil = pos_y_player
            pos_x_missil = pos_x_player #REVISAR ESSA PARTE


    # Cria uma barreira para evitar que a nave do player ultrapasse o limite do tamanho da região da janela no eixo y para cima
    if pos_y_player <= -10:
        pos_y_player += vel_nave_player

    # Cria uma barreira para evitar que a nave do player ultrapasse o limite do tamanho da região da janela no eixo y  para baixo
    if pos_y_player >= 440:
        pos_y_player -= vel_nave_player

    # Cria uma barreira para evitar que a nave do player ultrapasse o limite do tamanho da região da janela no eixo x para a direita
    if pos_x_player <= 0:
        pos_x_player += vel_nave_player

    # Cria uma barreira para evitar que a nave do player ultrapasse o limite do tamanho da região da janela no eixo x para a esquerda
    if pos_x_player >= 870:
        pos_x_player -= vel_nave_player

    # Comentar mais tarde
    player_rect = nave_player.get_rect()
    inimigo_rect = nave_inimiga.get_rect()
    missil_rect = missil.get_rect()

    player_rect.y = pos_y_player
    player_rect.x = pos_x_player

    inimigo_rect.y = pos_y_inimigo
    inimigo_rect.x = pos_x_inimigo

    missil_rect.y = pos_y_missil
    missil_rect.x = pos_x_missil

    # Se o player tiver clicado em "SPACE", o missil será atirado/irá se 
    #MOvimentar
    if tiro_alvo:
        pos_y_missil -= vel_missil

    colisao()



    #Desenha/insere o plano de fundo na janela do game
    janela.blit(background_image, (0,0))
    #Desenha/insere a nave do player na janela do game
    janela.blit(nave_player, (pos_x_player,pos_y_player))
    #Desenha/insere a nave inimiga na janela do game
    janela.blit(nave_inimiga, (pos_x_inimigo, pos_y_inimigo))
    # Desenha/insere o missil do player na janela do game
    janela.blit(missil, (pos_x_missil, pos_y_missil))
    #janela.blit(text, text_Rect)
    MostraTextoNaTela("Pontuação", pontuacao, 75, 10, 18, atualizar_tela=False)
    MostraTextoNaTela("Tempo", segundos, 54, 40, 18)
   

# Se a nave do player morrer, a tela é congelada por 5 segundos.Após isso,
# O jogo fecha
'''if nave_player_morreu:
    sleep(1)'''


