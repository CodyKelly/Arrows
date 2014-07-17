import pygame, variables
import Objects.mob as mob
import Objects.arrow as arrow
import Objects.totem as totem

pygame.font.init()

'''This minimap also acts as a kinda-sorta GUI so yeah.'''

class UI:
    def __init__(self, world):
        self.height = variables.windowHeight
        self.width = self.height*world.width/world.height
        self.surface = pygame.transform.scale(world.get_surface(), (self.width,self.height))
        self.active = False
        for x in range(0,world.width):
            for y in range(0,world.height):
                self.surface.blit(pygame.transform.scale(world.chunks[x][y].get_surface(), (self.width/world.width,self.height/world.height)),(x*self.width/world.width,y*self.height/world.height))
        self.world = world
        self.windowList = []
        #self.windowList.append(window((0,250), (250,variables.windowHeight-250), 2))
    def update(self, screen, world, clock, debug):
        camera = world.get_camera()
        (mouseX,mouseY) = pygame.mouse.get_pos()
        if(mouseX < self.width):
            self.active = True
            newMap = self.surface.copy()
            camera = world.get_camera()
            (cx,cy) = camera.get_pos()
            cx = cx/variables.tileSize*self.width/variables.worldWidth/variables.chunkSize
            cy = cy/variables.tileSize*self.height/variables.worldHeight/variables.chunkSize
            
            displaySurface = pygame.display.get_surface()
            cameraWidth = displaySurface.get_width()/variables.tileSize*self.width/world.getChunkWidth()/variables.chunkSize
            cameraHeight = displaySurface.get_height()/variables.tileSize*self.height/world.getChunkHeight()/variables.chunkSize
            cameraRect = pygame.Rect((0,0),(cameraWidth/variables.scale,cameraHeight/variables.scale))
            cameraRect.center = (cx,cy)
            pygame.draw.rect(newMap, (255,255,255), cameraRect, 2)
            
            rect = self.surface.get_rect()
            #if(rect.collidepoint(pygame.mouse.get_pos())):
                #newMap.set_alpha(255)
            #else:
                #newMap.set_alpha(100)
            
            screen.blit(newMap,(0,0))
            
            if(debug):
                     
                self.texts('FPS: ' + str(int(clock.get_fps())), (self.width + 5,0), screen)
                
                self.texts('Speed: '+str(camera.speed), (self.width + 5,30), screen)
                
                self.texts('Scale: '+str(variables.scale), (self.width + 5,60), screen)

            borderRect = newMap.get_rect()
            pygame.draw.rect(screen,(70,70,70),borderRect, 3)
        else:
            if(debug):
                     
                self.texts('FPS: ' + str(int(clock.get_fps())), (5,0), screen)
                
                self.texts('Speed: '+str(camera.speed), (5,30), screen)
                
                self.texts('Scale: '+str(variables.scale), (5,60), screen)            
        
    def texts(self,text, screen):
        font=pygame.font.Font('pictures/Font/Market_Deco.ttf',30)
        textpic=font.render(text, 1,(255,255,255))
        screen.blit(textpic, (x,y))
    def click(self, mousePos):
        rect = self.surface.get_rect()
        if(rect.collidepoint(mousePos)):
            (x,y) = mousePos
            x = x*variables.tileSize*variables.chunkSize*variables.worldWidth/self.width
            y = y*variables.tileSize*variables.chunkSize*variables.worldHeight/self.height
            self.world.camera.set_pos((x,y))
            return(True)
        
class texts(object):
    def __init__(self, text, screen):
        self.pos = pos
        self.thing = thing
        self.world = world
        self.icon = thing.get_picture()
    def draw(self, surface):
        surface.blit(self.icon, self.pos)
    def get_thing(self):
        return(self.thing())