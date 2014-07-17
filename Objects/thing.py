import pygame, variables

class Thing(pygame.sprite.Sprite):
    def __init__(self, x, y, picDestination, speed, name, world):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.transform.scale2x(pygame.image.load(picDestination))
        self.size = self.image.get_height()
        self.rect = pygame.Rect((0,0),(self.size,self.size))
        self.speed = speed
        self.name = name
        self.world = world
        self.world.worldGroup.add(self)    
    def update(self):    
        pass
    def get_pos(self):
        return((self.x, self.y))
    def get_speed(self):
        return((self.speed))
    def move(self, direction):
        if(direction=='left'):
            if(self.x>0+self.speed):
                self.x -= self.speed
            else:
                self.x = 0
        elif(direction=='right'):
            if(self.x<=variables.realWorldSize-(self.speed+self.size)):
                self.x += self.speed
            else:
                self.x = variables.realWorldSize - self.size
        elif(direction=='up'):
            if(self.y>=0+self.speed):
                self.y -= self.speed
            else:
                self.y = 0
        elif(direction=='down'):
            if(self.y<=variables.realWorldSize-(self.speed+self.size)):
                self.y += self.speed  
            else:
                self.y = variables.realWorldSize - self.size    
    def get_name(self):
        return(self.name)
    def get_center(self):
        return((self.rect.center))
    def set_pos(self, (x,y)):
        (self.x,self.y) = (x,y)