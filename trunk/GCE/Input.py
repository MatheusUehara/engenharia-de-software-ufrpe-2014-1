from pygame.locals import *
import random
import pygame, sys, eztext

pygame.init()

pygame.display.set_caption(' G C E ')

screen = pygame.display.set_mode((800,600))


def main(comprimento):
    layer = pygame.image.load("Interface/caixa de dialogo/layer_1.png")
    background = pygame.image.load("Interface/background/background_GCE.png")
    botao = pygame.image.load("Interface/botoes/INSERIR.png")
    voltar = pygame.image.load("Interface/botoes/VOLTAR.png")
    desfazer = pygame.image.load("Interface/botoes/DESFAZER.png")
    
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
    
    while 1:
        clock.tick(30)
        
        screen.blit(background,(0,0))
        screen.blit(layer,(30,285))
        screen.blit(botao,(575,286))    
        screen.blit(desfazer,(575,350))
        screen.blit(voltar,(575,500))
        
        events = pygame.event.get()
        
        for event in events:
            if event.type == pygame.QUIT: 
                sys.exit()
            
            if event.type==pygame.MOUSEBUTTONDOWN:             
                pos = pygame.mouse.get_pos()
               
                try:
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
                        MENU.selecao_campeonato()
                        
                except:
                    pass
        

        font = pygame.font.Font(None, 40)#(255,0,0)
        font_score = font.render("Faltam: %d equipes" %(cont), True, (24,45,135))
        screen.blit(font_score, (300,360))
        
        txtbx.update(events)
        txtbx.draw(screen)
        pygame.display.flip()