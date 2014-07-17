import variables, pygame

up_button = pygame.image.load('pictures/buttons/up_button.png')

class Menu():
    def __init__(self):
        self.width = variables.windowWidth
        self.height = variables.windowHeight
        self.surface = pygame.Surface((self.width, self.height)).convert()
        self.surface.fill((255,0,255))
        self.surface.set_colorkey((255,0,255))
    def update(self, screen):
        self.surface.blit(up_button,(0,0))
        screen.blit(self.surface,(0,0))