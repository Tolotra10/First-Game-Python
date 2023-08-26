import pygame
import sys
import random

#Initialisation de Pygame
pygame.init()

#Dimensions
larg = 1000
height = 600
img_size = (60,60)
logo_size = (30,30)

#Couleurs
white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)

#Fonts
litle = pygame.font.Font(None,20)
medium = pygame.font.Font(None,30)
large = pygame.font.Font(None,40)

#images
joystick = pygame.image.load('./icons/joystick.png')
rock = pygame.image.load('./icons/stone.png')
paper = pygame.image.load('./icons/paper.png')
scissors = pygame.image.load('./icons/scissor.png')
joystick_size = pygame.transform.scale(joystick,logo_size)
rock_size = pygame.transform.scale(rock,img_size)
paper_size = pygame.transform.scale(paper,img_size)
scissors_size = pygame.transform.scale(scissors,img_size)

#Création fenêtre
screen = pygame.display.set_mode((larg,height))

#score
s_player = 0
s_computer = 0
result = ""

#Textes
title_game = large.render('Pierre - Feuille - Ciseaux',True,black)
notice_game = litle.render('Appuiez respectivement sur les touches p f c de votre clavier pour choisir entre Pierre, feuille ou ciseaux.',True,black)
copyright_game = litle.render('Tolotra first game.',True,black)
p_legend = medium.render('Joueur',True,black)
c_legend = medium.render('Ordinateur',True,black)
warning = litle.render("Veuillez appuyer sur un des touches recommendés!",True,black,yellow)
s_player_text = large.render(f"{s_player}",True,black)
s_computer_text = large.render(f"{s_computer}",True,black)

#Emplacements textes
title_rect = title_game.get_rect(center=(larg // 2 , 30))
notice_rect = notice_game.get_rect(center=(larg // 2,70))
copyright_rect = copyright_game.get_rect(center=(larg // 2,580))
p_legend_rect = p_legend.get_rect(center=(330,200))
c_legend_rect = c_legend.get_rect(center=(640,200))
warning_rect = warning.get_rect(center=(larg // 2, height // 2))


#Affichage des choix
def showChoice(player_c, computer_c):
    x_player = 310
    x_computer = 620
    y = 250

    screen.blit(player_c,(x_player,y))
    screen.blit(computer_c,(x_computer,y))

images_choice = {
    "pierre" : rock_size,
    "feuille" : paper_size,
    "ciseaux" : scissors_size
}

#Réinitialiser
def resetGame():
    global s_player,s_computer
    s_computer = 0
    s_player = 0





#Déterminer gagnant
def winner(player_c,computer_c):
    if(player_c == computer_c):
        return "Egalité"
    elif(player_c == "pierre" and computer_c == "ciseaux") or \
        (player_c == "feuille" and computer_c == "pierre") or \
        (player_c == "ciseaux" and computer_c == "feuille"):
            return "Joueur"
    else:
        return "Ordinateur"
  
#Script de lancement
running = True
while running :
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key in [pygame.K_f,pygame.K_p,pygame.K_c]:
                player_c =""
                computer_c = random.choice(["pierre","feuille","ciseaux"])
               
                if event.key == pygame.K_p:
                    player_c = "pierre"
                elif event.key == pygame.K_f:
                    player_c = "feuille"
                elif event.key == pygame.K_c:
                    player_c = "ciseaux"
                result = winner(player_c,computer_c)
                if result == "Joueur":
                    s_player += 1
                    s_player_text = large.render(f"{s_player}",True,black)
                if result == "Ordinateur":
                    s_computer += 1
                    s_computer_text = large.render(f"{s_computer}",True,black)

                if (s_player == 5 or s_computer == 5):
                    winner_rect = pygame.Rect(0, 0, larg, height)

                    running = False
                
                
                result_text = medium.render(result,True,black)
                result_rect = result_text.get_rect(center=(larg // 2 , 500))
                showChoice(images_choice[player_c],images_choice[computer_c])  
                screen.blit(result_text,result_rect)
            else:
                screen.blit(warning,warning_rect)
    screen.blit(s_player_text,(320,120))
    screen.blit(s_computer_text,(630,120))
    screen.blit(p_legend,p_legend_rect)
    screen.blit(c_legend,c_legend_rect)
    screen.blit(title_game,title_rect)
    screen.blit(notice_game,notice_rect)
    screen.blit(copyright_game,copyright_rect)
    screen.blit(joystick_size,(680 , 10))
    
    
    pygame.display.flip()
    pygame.time.delay(1000)

pygame.quit()
sys.exit()