from pygame.locals import *
import random
import pygame, sys, eztext

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
            if event.type == QUIT:
                sys.exit()
                
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if (botao_MATA_Rect.collidepoint(pos[0],pos[1])):
                    tamanho("mata_mata")
                elif (botao_PONTOS_Rect.collidepoint(pos[0],pos[1])):
                    tamanho("pontos_corridos")
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
                if event.type == QUIT:
                    sys.exit()
                
                if event.type == MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if (botaoRect.collidepoint(pos[0],pos[1])):
                        main(2,tipo_campeonato)
                    if (botao4Rect.collidepoint(pos[0],pos[1])):
                        main(4,tipo_campeonato)
                    if (botao8Rect.collidepoint(pos[0],pos[1])):
                        main(8,tipo_campeonato)
                    if (botao16Rect.collidepoint(pos[0],pos[1])):
                        main(16,tipo_campeonato)
                    if (botao32Rect.collidepoint(pos[0],pos[1])):
                        main(32,tipo_campeonato)
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
                        main(2,tipo_campeonato)
                    if (botao4Rect.collidepoint(pos[0],pos[1])):
                        main(4,tipo_campeonato)
                    if (botao8Rect.collidepoint(pos[0],pos[1])):
                        main(8,tipo_campeonato)
                    if (botao16Rect.collidepoint(pos[0],pos[1])):
                        main(16,tipo_campeonato)
                    if (botao32Rect.collidepoint(pos[0],pos[1])):
                        main(32,tipo_campeonato)
                    if (botao_VOLTAR_Rect.collidepoint(pos[0],pos[1])):
                        selecao_campeonato()
        elif tipo_campeonato == "3":
            main(4,tipo_campeonato)
            
            
        pygame.display.flip()






def main(comprimento,tipo_campeonato):
    layer = pygame.image.load("Interface/caixa de dialogo/layer_1.png")
    background = pygame.image.load("Interface/background/background_GCE.png")
    botao = pygame.image.load("Interface/botoes/INSERIR.png")
    voltar = pygame.image.load("Interface/botoes/VOLTAR.png")
    desfazer = pygame.image.load("Interface/botoes/DESFAZER.png")
    passar = pygame.image.load("Interface/botoes/PASSAR.png")
    
    tamanho = comprimento
    cont = tamanho
    
    
    txtbx = eztext.Input(maxlength=20, color=(255,255,255), prompt='Entre com a Equipe : ')
    clock = pygame.time.Clock()
    lista= []
    
    eztext.Input().set_pos(320,120)
    
    botao_INSERIR_Rect = botao.get_rect()
    botao_INSERIR_Rect.x = 575
    botao_INSERIR_Rect.y = 286
    
    botao_DESFAZER_Rect = desfazer.get_rect()
    botao_DESFAZER_Rect.x = 575
    botao_DESFAZER_Rect.y = 350
    
    
    botao_VOLTAR_Rect = voltar.get_rect()
    botao_VOLTAR_Rect.x = 600
    botao_VOLTAR_Rect.y = 500
    
    botao_PASSAR_Rect = passar.get_rect()
    botao_PASSAR_Rect.x = 300 
    botao_PASSAR_Rect.y = 500
           
    
    while 1:
        clock.tick(30)
        
        screen.blit(background,(0,0))
        screen.blit(layer,(30,285))
        screen.blit(botao,(575,286))    
        screen.blit(desfazer,(575,350))
        screen.blit(voltar,(575,500))
        screen.blit(passar,(300,500))
        
        events = pygame.event.get() 
        
        for event in events:
            if event.type == QUIT: 
                sys.exit()
            
            if event.type == MOUSEBUTTONDOWN:             
                pos = pygame.mouse.get_pos()
               
                if (botao_INSERIR_Rect.collidepoint(pos[0],pos[1]))and (len(txtbx.value)> 5) and (len(lista)< tamanho):
                    cont -= 1
                    lista.append(txtbx.value)
                    txtbx.value = ""
                    random.shuffle(lista)
                    print 
                    for i in range(len(lista)):
                        print lista[i]
                elif (botao_DESFAZER_Rect.collidepoint(pos[0],pos[1])) and (len(lista) >= 1):
                    cont +=1
                    index = tamanho-cont
                    lista.pop(index)
                elif botao_VOLTAR_Rect.collidepoint(pos[0],pos[1]):
                    import MENU
                    MENU.tamanho(tipo_campeonato)
                    
                elif (botao_PASSAR_Rect.collidepoint(pos[0],pos[1])) and (len(lista) == comprimento) :
                    if tipo_campeonato == "mata_mata":
                        mata_mata(comprimento)
                    elif tipo_campeonato == "pontos_corridos":
                        pontos_corridos(comprimento)    
                        
        font = pygame.font.Font(None, 40)#(255,0,0)
        font_score = font.render("Faltam: %d equipes" %(cont), True, (24,45,135))
        screen.blit(font_score, (300,360))
        
        txtbx.update(events)
        txtbx.draw(screen)
        pygame.display.flip()
        
        
        
        
def mata_mata(tamanho):
    pass

def pontos_corridos(tamanho):
    pass