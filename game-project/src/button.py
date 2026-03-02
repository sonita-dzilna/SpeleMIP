import pygame
#pogas klase
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        # scale regulē pogu lielumu ekrānā
        self.image = pygame.transform.scale(image, (int(width *scale)), (int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.visible = True #vai redzama

    def draw(self, surface):
        action = False
        #redzēt kursoru
        pos = pygame.mouse.get_pos() # saņem kursora koordinātes spēles ekrānā
        #kursora nosacījumi
        if self.rect.collidepoint(pos): #vai kursors ir uz pogas teritorijas
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False : #uztver, kad uzspiež uz pogas
                self.clicked = True #novērš, ka, uzspiežot uz pogas, darbība tiek veikta vairākas reizes
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #parādīt pogu uz ekrāna
        surface.blit(self.igame, (self.rect.x, self.rect.y))

        return action #saņem darbības sākšanas signālu
