import pygame, variables, math

class Camera(object):
    def __init__(self, (x,y)):
        self.speed = 10
        self.name = 'Camera'
        self.x = x
        self.y = y
        self.size = 0
        
    def update(self, worldX, worldY):
        pass
        
    def changeSpeed(self, value):
        if(self.speed + value >0):
            self.speed += value
                
    def get_pos(self):
        return((self.x, self.y))
    
    def get_speed(self):
        return((self.speed))
    
    def set_pos(self, (x,y)):
        (self.x,self.y) = (x,y)    
    
    def move(self, direction):
        if(direction=='left'):
            if(self.x>0+self.speed):
                self.x -= self.speed
            else:
                self.x = 0
        elif(direction=='right'):
            if(self.x<=variables.realWorldWidth-(self.speed+self.size)):
                self.x += self.speed
            else:
                self.x = variables.realWorldWidth - self.size
        elif(direction=='up'):
            if(self.y>=0+self.speed):
                self.y -= self.speed
            else:
                self.y = 0
        elif(direction=='down'):
            if(self.y<=variables.realWorldHeight-(self.speed+self.size)):
                self.y += self.speed  
            else:
                self.y = variables.realWorldHeight - self.size  