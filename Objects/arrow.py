import pygame, thing, math, animal

class Arrow(thing.Thing):
    def __init__(self, rotation, (x,y), world, caster):
        self.rotation = math.radians(rotation)
        speed = 20
        self.life = 50
        picDestination = 'pictures/arrow.png'
        name = 'Arrow'
        self.hurtValue = 10
        self.caster = caster
        thing.Thing.__init__(self,x, y, picDestination, speed, name, world)        
        self.image = pygame.transform.rotate(self.image, 270-math.degrees(self.rotation))
    def update(self):
        self.rect.x = int(round(self.x)) - self.world.offsetX
        self.rect.y = int(round(self.y)) - self.world.offsetY
        if(self.life > 0):
            moveX = math.cos(self.rotation)*self.speed
            moveY = math.tan(self.rotation)*moveX
            self.x += moveX
            self.y += moveY
            self.life -= 1
        elif(self.life == 0):
            self.kill()
        for animal in pygame.sprite.spritecollide(self,self.world.animalGroup,0):
            if not(animal == self.caster):
                animal.hurt(self.hurtValue)
                self.kill()
        #if(self.rect.x < 0 or self.rect.x > self.world.size *32):
            #self.world.remove_object(self)
        #if(self.rect.y < 0 or self.rect.y > self.world.size *32):
            #self.world.remove_object(self)