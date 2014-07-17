import pygame, thing, mob

class Totem(thing.Thing):
    def __init__(self, (x,y), world):
        picDestination = 'pictures/totem.png'
        speed = 1
        name = 'Totem'
        thing.Thing.__init__(self, x, y, picDestination, speed, name, world)
        self.spawnTime = 1000
        self.spawnTimer = self.spawnTime
        self.group = pygame.sprite.Group()
        self.world.totemGroup.add(self)
        self.influence = 1
        #self.totemType
    def update(self):
        self.rect.x = self.x - self.world.offsetX
        self.rect.y = self.y - self.world.offsetY
        if(self.spawnTimer > 0):
            self.spawnTimer -= 1
        else:
            newMob = mob.Mob(self.get_pos(), self.world)
            self.world.add_object(newMob)
            self.world.add_object(newMob)
            self.spawnTimer = self.spawnTime