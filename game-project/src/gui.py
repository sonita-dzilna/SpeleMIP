import pygame
import button
import random
import __init__

#izveido displeja logu
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

#pogas attēls (vajag pievienot attēlus)
start_img = pygame.image.load('sākuma_poga.png').convert_alpha()
exit_img = pygame.image.load('izejas_poga.png').convert_alpha()
restart_img = pygame.image.load('restart_poga.png').convert_alpha()
cilveks_img = pygame.image.load('cilveks_poga.png').convert_alpha()
dators_img = pygame.image.load('dators_poga.png').convert_alpha()
minimaksa_img = pygame.image.load('minimaksa_poga.png').convert_alpha()
alfabeta_img = pygame.image.load('alfabeta_poga.png').convert_alpha()
skaitlis1_img = pygame.image.load('skaitlis1_poga.png').convert_alpha()
skaitlis2_img = pygame.image.load('skaitlis2_poga.png').convert_alpha()
skaitlis3_img = pygame.image.load('skaitlis3_poga.png').convert_alpha()
skaitlis4_img = pygame.image.load('skaitlis4_poga.png').convert_alpha()

#izveidot pogas, izmantojot button.py klases metodes
start_button = button.Button(100, 200, start_img, 0.8) 
exit_button = button.Button(450, 200, exit_img, 0.8)
restart_button = button.Button(500, 100, restart_img, 0.8)
# programmā obligāti jānodrošina šādas iespējas:
#kurš uzsāk spēli- cilvēks vai dators
cilveks_button = button.Button(100, 200, cilveks_img, 0.8)
dators_button = button.Button(450, 200, dators_img, 0.8)
#kuru algoritmu izmantos dators konkrētajā spēles reizē
minimaksa_button = button.Button(100, 200, minimaksa_img, 0.8)
alfabeta_button = button.Button(450, 200, alfabeta_img, 0.8)
#izpildīt gājienus-spiest uz skaitļu ģenerētajām pogām, lai tās izņemtu no virknes.
#cikls kas ģenerētu skaitļu pogas
def skaitla_button(skaitlis):
    if skaitlis == 1:
        skaitlis1_button = button.Button(random.randint(500), random.randint(750), skaitlis1_img, 0.5)
    if skaitlis == 2:
        skaitlis2_button = button.Button(random.randint(500), random.randint(750), skaitlis2_img, 0.5)
    if skaitlis == 3:
        skaitlis3_button = button.Button(random.randint(500), random.randint(750), skaitlis3_img, 0.5)
    if skaitlis == 4:
        skaitlis4_button = button.Button(random.randint(500), random.randint(750), skaitlis4_img, 0.5)

def next_move(self):
    start_button.visible = False
    restart_button.draw
    exit_button.topleft = (400, 100)
    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()
    punktisp1 = text.get_rect() # punktu rādītājs spēlētājam 1
    punktisp2 = text.get_rect() # punktu rādītājs spēlētājam 2

    # set the center of the rectangular object.
    textRect.center = (200, 300)
    punktisp1.center = (100, 300) # kur stāvētu punkti
    punktisp2.center = (300, 300)
    if cilveks_button.draw(screen) and dators_button.draw(screen):
        text = font.render ('Izvēlēties, kurš uzsāk spēli : cilvēks vai dators', True, green, blue)
        screen.blit(text, textRect)
        #te kaut kam jānotiek
        cilveks_button.visible = False
        dators_button.visible = False

    if minimaksa_button.draw(screen) and alfabeta_button.draw(screen):
        text = font.render ('Izvēlēties, kuru algoritmu izmantos dators konkrētajā spēles reizē: Minimaksa algoritmu vai Alfa-beta algoritmu', True, green, blue)
        screen.blit(text, textRect)
        #te arī kaut kam jānotiek
        minimaksa_button.visible = False
        alfabeta_button.visible = False 

     init() #spēle...

    if restart_button.draw(screen):
        next_move()


#spēles cikls
run = True
while run:
    
    screen.fill((202, 228, 241)) #fona krāsa

    if start_button.draw(screen): #izsauc metodi, kas parāda pogu
        next_move()
    if exit_button.draw(screen):
        run = False #beidzas spēle


    for event in pygame.even.get():
        #gaida, kad pārtrauks spēli
        if event.type == pygame.QUIT:   
            run = False
    
    pygame.display.update()

pygame.quit()

#https://www.youtube.com/watch?v=G8MYGDf_9ho&list=LL&index=4&t=5s
#https://www.geeksforgeeks.org/python/python-display-text-to-pygame-window/