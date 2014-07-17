import pygame, variables, animal, random, math, arrow, bork

class Mob(animal.Animal):
    def __init__(self, (x,y), world):
        speed = random.randint(2,5)
        picDestination = 'pictures/characters/townsman.png'
        name = 'Person'
        maxHealth = 10
        animal.Animal.__init__(self,x, y, picDestination, speed, name, world, maxHealth)
        self.timerValue = random.randint(25,75)
        self.timer = self.timerValue
        self.direction = "none"
        self.world.mobGroup.add(self)
    def update(self):
        self.rect.x = self.x - self.world.offsetX
        self.rect.y = self.y - self.world.offsetY
        if(self.timer > 0):
            if not(self.direction == "none"):
                self.move(self.direction)
            self.timer -= 1
        if(self.timer == 0):
            x = random.randint(0,4)
            if(x==0):
                self.direction = 'none'
            if(x==1):
                self.direction = 'left'
            if(x==2):
                self.direction = 'up'
            if(x==3):
                self.direction = 'right'                
            if(x==4):
                self.direction = 'down'            
            self.timer = self.timerValue
            
    def shoot(self, pos):
        (x,y) = pos
        deltaY = y-self.rect.y
        deltaX = x-self.rect.y
        rotation = math.atan2(deltaY,deltaX)*180/math.pi
        self.world.add_object(arrow.Arrow(rotation,self.get_pos(),self.world, self))          
    
    def hurt(self, amount):
        if(self.health - amount <= 0):
            self.world.add_object(bork.Bork(self.get_pos(), self.world))
            self.kill()
        else:
            self.health -= amount