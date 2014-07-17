import pygame, thing, math, animal

class Fireball(thing.Thing):
    def __init__(self, rotation, (x,y), world, caster):
        self.rotation = math.radians(rotation)
        speed = 15
        self.life = 150
        picDestination = 'pictures/fireball.png'
        name = 'Fireball'
        self.hurtValue = 50
        self.caster = caster
        thing.Thing.__init__(self,x, y, picDestination, speed, name, world)        
    def update(self):
        if(self.life > 0):
            moveX = math.cos(self.rotation)*self.speed
            moveY = math.tan(self.rotation)*moveX
            self.x += moveX
            self.y += moveY
            self.rect.x = int(round(self.x))
            self.rect.y = int(round(self.y))              
            self.life -= 1
        elif(self.life == 0):
            self.world.remove_object(self)
        for o in self.world.get_objectList():
            if isinstance(o, animal.Animal):
                if(self.rect.colliderect(o.rect)):
                    if not(o == self.caster):
                        o.hurt(self.hurtValue)
                        self.world.remove_object(self)