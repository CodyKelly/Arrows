import pygame, thing

class Bork(thing.Thing):
    def __init__(self, (x,y), world):
        picDestination = 'pictures/bork.png'
        name = 'Bork'
        speed = 1
        thing.Thing.__init__(self,x, y, picDestination, speed, name, world)
        self.world.borkGroup.add(self)
    def update(self):
        self.rect.x = self.x - self.world.offsetX
        self.rect.y = self.y - self.world.offsetY