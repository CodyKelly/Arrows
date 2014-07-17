import pygame, thing

class Animal(thing.Thing):
    def __init__(self, x, y, picDestination, speed, name, world, maxHealth):
        self.maxHealth = maxHealth
        self.health = maxHealth
        thing.Thing.__init__(self,x, y, picDestination, speed, name, world)
        self.world.animalGroup.add(self)
    def heal(self, amount):
        if(self.health + amount > self.maxHealth):
            self.health = self.maxHealth
        else:
            self.health += amount
    def hurt(self, amount):
        if(self.health - amount <= 0):
            self.kill()
        else:
            self.health -= amount