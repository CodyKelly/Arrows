import pygame

pygame.font.init()

'''This minimap also acts as a kinda-sorta GUI so yeah.'''

class UI(object):
    def __init__(self, world, (windowWidth, windowHeight)):
        self.height = windowHeight
        self.width = self.height*world.width/world.height
        self.surface = pygame.transform.scale(world.get_surface(), (self.width,self.height))
        for x in range(0,world.width):
            for y in range(0,world.height):
                self.surface.blit(pygame.transform.scale(world.chunks[x][y].get_surface(), (self.width/world.width,self.height/world.height)),(x*self.width/world.width,y*self.height/world.height))
        self.world = world
        
    def update(self, screen, world, clock, debug, camera):
        (mouseX,mouseY) = pygame.mouse.get_pos()
        if(mouseX < self.width):
            newMap = self.surface.copy()
            # calculating center of camera rect in minimap
            (cx,cy) = camera.get_pos()
            cx = cx/world.tileSize*self.width/world.width/world.chunkSize
            cy = cy/world.tileSize*self.height/world.height/world.chunkSize
            
            #calculating and drawing camera square on minimap
            displaySurface = pygame.display.get_surface()
            displayWidth = displaySurface.get_width()
            displayHeight = displaySurface.get_height()
            cameraWidth = displayWidth/world.tileSize*self.width/world.width/world.chunkSize
            cameraHeight = displayHeight/world.tileSize*self.height/world.height/world.chunkSize
            cameraRect = pygame.Rect((0,0),(cameraWidth/world.scale,cameraHeight/world.scale))
            cameraRect.center = (cx,cy)
            pygame.draw.rect(newMap, (255,255,255), cameraRect, 2)
            screen.blit(newMap,(0,0))
            
            if(debug):
                     
                self.texts('FPS: ' + str(int(clock.get_fps())), (self.width + 5,0), screen)
                
                self.texts('Speed: '+str(camera.speed), (self.width + 5,30), screen)
                
                self.texts('Scale: '+str(world.scale), (self.width + 5,60), screen)

            borderRect = newMap.get_rect()
            pygame.draw.rect(screen,(70,70,70),borderRect, 3)
        else:
            if(debug):
                     
                self.texts('FPS: ' + str(int(clock.get_fps())), (5,0), screen)
                
                self.texts('Speed: '+str(camera.speed), (5,30), screen)
                
                self.texts('Scale: '+str(world.scale), (5,60), screen)            
    def click(self, mousePos, camera):
        rect = self.surface.get_rect()
        if(rect.collidepoint(mousePos)):
            (x,y) = mousePos
            x = x*self.world.tileSize*self.world.chunkSize*self.world.width/self.width
            y = y*self.world.tileSize*self.world.chunkSize*self.world.height/self.height
            camera.set_pos((x,y))
            return(True)    
        
    def texts(self,text, (x,y), screen):
        font=pygame.font.Font('pictures/Font/Market_Deco.ttf',30)
        textpic=font.render(text, 1,(255,255,255))
        screen.blit(textpic, (x,y))