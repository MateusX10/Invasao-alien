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
        text = font.render("Pontuação: " + str(pontuacao), True, (0, 255, 0), (0,0,0))
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



#define o tamanho da janela (800X600 no caso)
janela = pygame.display.set_mode((960, 540)) 






#define o título da janela
pygame.display.set_caption("Invasão Alien") 


# Carrega a música de fundo do game
musica = pygame.mixer.music.load("musica_espaço_sideral2.mp3")

# Define o volume do som
# Toca a música
mixer.music.play()
#Carrega a imagem do plano de fundo do jogo
background_image = pygame.image.load("/home/mateus/Documentos/computação/programacao/python/exs/jogo da nave/background.png")
#Carrega a imagem da nave do player
nave_player = pygame.image.load("/home/mateus/Documentos/computação/programacao/python/exs/jogo da nave/nave_pequena.png")
#Carrega a imagem da nave inimiga
nave_inimiga = pygame.image.load("/home/mateus/Documentos/computação/programacao/python/exs/jogo da nave/nave inimiga pequena.png")
#Carrega o míssil
missil = pygame.image.load("/home/mateus/Documentos/computação/programacao/python/exs/jogo da nave/missil pequeno.png")
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

    if segundos == 300:
        quit()

    if segundos == 60:
        vel_nave_inimigo = 6

    elif segundos == 120:
        vel_nave_inimigo = 10

    elif segundos == 180:
        vel_nave_inimigo = 14

    elif segundos == 240:
        vel_nave_player = 15
        vel_nave_inimigo = 20
        

    # Define a fonte do tempo
    font2 = pygame.font.Font("freesansbold.ttf", 18)
    # Concatena a string "tempo" com a string "segundos"
    tempo = font2.render("Tempo: " + str(segundos), True, (0,255,0), (0,0,0))
    # O retângulo que ficará em volta do tempo
    tempo_rect = tempo.get_rect()
    # Posiçãp do retângulo do tempo
    tempo_rect.center = (54, 40)

    # Primeiro argumento: é a fonte, segundo argumento: tamanho da fonte
    font = pygame.font.Font('freesansbold.ttf', 18)
    # 3º argumento: O "True" quer dizer "alta resolução"
    # 4º argumento: cor da fonte será verde
    # 5º argumento: cor do fundo será preto
    text = font.render("Pontuação: " + str(pontuacao), True, (0, 255, 0), (0,0,0))
    # Este será o retângulo para o nosso texto
    text_Rect = text.get_rect()
    #Arg1: pos x, arg2: pos y
    text_Rect.center = (75, 10)


    # Reage as teclas pressionadas pelo usuário
    teclas = pygame.key.get_pressed()

    # Para cada evento/ação realizada pelo usuário na janela, se o usuário cliclar no "X" ou clicar na tecla "E", o jogo irá fechar
    for events in pygame.event.get():
        if events.type == pygame.QUIT or teclas[pygame.K_q] or nave_player_morreu:
            loop = False


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
    janela.blit(text, text_Rect)
    janela.blit(tempo, tempo_rect)
    


    #atualizar a tela
    pygame.display.update()

# Se a nave do player morrer, a tela é congelada por 5 segundos.Após isso,
# O jogo fecha
if nave_player_morreu:
    sleep(1)
    quit()
