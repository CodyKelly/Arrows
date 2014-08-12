from pyganim import PygConductor
from pygame import sprite

class Person(sprite.Sprite):
    def __init__(self, (x,y), animConductor):
        self.x = x
        self.y = y
        self.animConductor = animConductor
        self.animation = self.animConductor.animations[0]
        self.image = self.animation.getCurrentFrame()
        self.animation.play()
    def update(self):
        self.image = self.animation.getCurrentFrame()