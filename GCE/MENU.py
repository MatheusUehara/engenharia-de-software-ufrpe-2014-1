import pygame,sys,Input

pygame.init()

pygame.display.set_caption(' G C E ')

screen = pygame.display.set_mode((800,600))

def start():
    background = pygame.image.load("Interface/background/home.png")
    
    botao = pygame.image.load("Interface/botoes/COMECAR.png")    
    botaoRect = botao.get_rect()
    botaoRect.x = 310
    botaoRect.y = 470
    
    while 1:
        screen.blit(background,(0,0))
        screen.blit(botao,(310,470))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if (botaoRect.collidepoint(pos[0],pos[1])):
                    selecao_campeonato() 
        pygame.display.flip()
        
def selecao_campeonato():
    background = pygame.image.load("Interface/background/selecao.png")
    
    MATA_MATA = pygame.image.load("Interface/botoes/MATAMATA.png")
    
    voltar = pygame.image.load("Interface/botoes/VOLTAR.png")
    
    PONTOS_CORRIDOS= pygame.image.load("Interface/botoes/PONTOS_CORRIDOS.png")
    
    botao_PONTOS_Rect = PONTOS_CORRIDOS.get_rect()
    botao_PONTOS_Rect.x = 310 
    botao_PONTOS_Rect.y = 250
        
    botao_MATA_Rect = MATA_MATA.get_rect()
    botao_MATA_Rect.x = 310
    botao_MATA_Rect.y = 350
    
    botao_VOLTAR_Rect = voltar.get_rect()
    botao_VOLTAR_Rect.x = 575
    botao_VOLTAR_Rect.y = 500
    
    
    
    while 1:
        screen.blit(background,(0,0))
        screen.blit(MATA_MATA,(310,350))
        screen.blit(PONTOS_CORRIDOS,(310,250))
        screen.blit(voltar,(575,500))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if (botao_MATA_Rect.collidepoint(pos[0],pos[1])):
                    tamanho("mata_mata")
                    break
                elif (botao_PONTOS_Rect.collidepoint(pos[0],pos[1])):
                    tamanho("pontos_corridos")
                    break
                elif (botao_VOLTAR_Rect.collidepoint(pos[0],pos[1])):
                    start()
        pygame.display.flip()
        
        
def tamanho(tipo_campeonato):
    background = pygame.image.load("Interface/background/number.png")
    
    botao2 = pygame.image.load("Interface/botoes/2eq.png")
    botaoRect = botao2.get_rect()
    botaoRect.x = 310
    botaoRect.y = 140
        
    botao4 = pygame.image.load("Interface/botoes/4eq.png")
    botao4Rect = botao4.get_rect()
    botao4Rect.x = 310
    botao4Rect.y = 240
    
    botao8 = pygame.image.load("Interface/botoes/8eq.png")
    botao8Rect = botao8.get_rect()
    botao8Rect.x = 310
    botao8Rect.y = 340
    
    botao16 = pygame.image.load("Interface/botoes/16eq.png")
    botao16Rect = botao16.get_rect()
    botao16Rect.x = 310
    botao16Rect.y = 440
    
    botao32 = pygame.image.load("Interface/botoes/32eq.png")    
    botao32Rect = botao32.get_rect()
    botao32Rect.x = 310
    botao32Rect.y = 540
    
    
    voltar = pygame.image.load("Interface/botoes/VOLTAR.png")
    botao_VOLTAR_Rect = voltar.get_rect()
    botao_VOLTAR_Rect.x = 575
    botao_VOLTAR_Rect.y = 500
    
    while 1:
        screen.blit(background,(0,0))
        if tipo_campeonato == "mata_mata":
            screen.blit(voltar,(575,500))
            screen.blit(botao2,(310,140))
            screen.blit(botao4,(310,240))
            screen.blit(botao8,(310,340))
            screen.blit(botao16,(310,440))
            screen.blit(botao32,(310,540))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if (botaoRect.collidepoint(pos[0],pos[1])):
                        Input.main(2,tipo_campeonato)
                    if (botao4Rect.collidepoint(pos[0],pos[1])):
                        Input.main(4,tipo_campeonato)
                    if (botao8Rect.collidepoint(pos[0],pos[1])):
                        Input.main(8,tipo_campeonato)
                    if (botao16Rect.collidepoint(pos[0],pos[1])):
                        Input.main(16,tipo_campeonato)
                    if (botao32Rect.collidepoint(pos[0],pos[1])):
                        Input.main(32,tipo_campeonato)
                    if (botao_VOLTAR_Rect.collidepoint(pos[0],pos[1])):
                        selecao_campeonato()
        elif tipo_campeonato == "pontos_corridos":
            screen.blit(voltar,(575,500))
            screen.blit(botao2,(310,140))
            screen.blit(botao4,(310,240))
            screen.blit(botao8,(310,340))
            screen.blit(botao16,(310,440))
            screen.blit(botao32,(310,540))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if (botaoRect.collidepoint(pos[0],pos[1])):
                        Input.main(2,tipo_campeonato)
                    if (botao4Rect.collidepoint(pos[0],pos[1])):
                        Input.main(4,tipo_campeonato)
                    if (botao8Rect.collidepoint(pos[0],pos[1])):
                        Input.main(8,tipo_campeonato)
                    if (botao16Rect.collidepoint(pos[0],pos[1])):
                        Input.main(16,tipo_campeonato)
                    if (botao32Rect.collidepoint(pos[0],pos[1])):
                        Input.main(32,tipo_campeonato)
                    if (botao_VOLTAR_Rect.collidepoint(pos[0],pos[1])):
                        selecao_campeonato()
        elif tipo_campeonato == "3":
            Input.main(4,tipo_campeonato)
            
            
        pygame.display.flip()
    