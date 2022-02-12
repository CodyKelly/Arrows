'''Pretty straightforward, this class controls
what gets rendered onto the screen'''

class Camera(object):
    def __init__(self, size):
        width, height = size
        self.speed = 10
        self.width = width
        self.height = height
        self.x = float(width/2)
        self.y = float(height/2)
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
    
    def set_pos(self, position):
        (self.x,self.y) = position    
    
    def move(self, direction):
        if(direction=='left'):
            if(self.x>0+self.speed):
                self.x -= self.speed
            else:
                self.x = 0
        elif(direction=='right'):
            if(self.x<=self.width-(self.speed+self.size)):
                self.x += self.speed
            else:
                self.x = self.width - self.size
        elif(direction=='up'):
            if(self.y>=0+self.speed):
                self.y -= self.speed
            else:
                self.y = 0
        elif(direction=='down'):
            if(self.y<=self.height-(self.speed+self.size)):
                self.y += self.speed  
            else:
                self.y = self.height - self.size  