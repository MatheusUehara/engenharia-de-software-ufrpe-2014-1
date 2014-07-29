import pygame,sys

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
    
    PONTOS_CORRIDOS= pygame.image.load("Interface/botoes/PONTOS_CORRIDOS.png")
    
    botao_PONTOS_Rect = PONTOS_CORRIDOS.get_rect()
    botao_PONTOS_Rect.x = 310 
    botao_PONTOS_Rect.y = 250
        
    botao_MATA_Rect = MATA_MATA.get_rect()
    botao_MATA_Rect.x = 310
    botao_MATA_Rect.y = 350
    
    
    
    while 1:
        screen.blit(background,(0,0))
        screen.blit(MATA_MATA,(310,350))
        screen.blit(PONTOS_CORRIDOS,(310,250))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if (botao_MATA_Rect.collidepoint(pos[0],pos[1])):
                    tamanho("1")
                elif (botao_PONTOS_Rect.collidepoint(pos[0],pos[1])):
                    tamanho("2")
        pygame.display.flip()
        
        
def tamanho(tipo):
    background = pygame.image.load("Interface/background/selecao.png")
    
    botao2 = pygame.image.load("Interface/botoes/2eq.png")
    botaoRect = botao2.get_rect()
    botaoRect.x = 310
    botaoRect.y = 140
        
    botao4 = pygame.image.load("Interface/botoes/4eq.png")
    
    botao8 = pygame.image.load("Interface/botoes/8eq.png")
    
    botao16 = pygame.image.load("Interface/botoes/16eq.png")
    
    botao32 = pygame.image.load("Interface/botoes/32eq.png")    

    while 1:
        screen.blit(background,(0,0))
        if tipo == "1":
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
                        import Input
                        Input.main(2)
        elif tipo == "2":
            import Input
            Input.main(4,"1")
        elif tipo == "3":
            import Input
            Input.main(4,"1")
            
            
        pygame.display.flip()
    