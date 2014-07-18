import pygame, numpy, random, sys, variables, datetime, ui
import World.world
import camera
import KeyManager.InputManager as InputManager
from pygame.locals import *
import ctypes

pygame.init()
pygame.display.set_icon(pygame.image.load('pictures/flowers/flower1.png'))
pygame.display.set_caption('Arrows!')

#world size, tile size, and screen size are stored in
#the variables.py file

camera = camera.Camera((variables.worldWidth/2,variables.worldHeight/2))
#variables.worldWidth = input("World width (in chunks): ")
#variables.worldHeight = input("World height (in chunks): ")
world = World.world.World(camera, variables.worldWidth, variables.worldHeight)
clock = pygame.time.Clock()
UI = ui.UI(world)

debug = False

Input = InputManager.Input()

pygame.display.set_mode((variables.windowWidth, variables.windowHeight))

paused = False

mouseDown = False

while True:
    if(paused):
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()            
            if event.type == KEYDOWN:      
                if event.type == KEYDOWN:      
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()            
                if event.key == K_p:
                    paused = False
    else:
        clock.tick(60)
        variables.screen.fill((0,0,0))
        for event in pygame.event.get():
            Input.update(event)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:      
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()                
                #if event.key == K_i:
                    #st = str(datetime.datetime.utcnow())
                    #pygame.image.save(world.get_surface(),'pictures/map/'+st+'.jpeg')
                if(event.key == K_F1):
                    if(debug==False):
                        debug = True
                    else:
                        debug = False
                if(event.key == K_EQUALS):
                    variables.scaleUp()
                elif(event.key == K_MINUS):
                    variables.scaleDown()
                if(event.key == K_LEFTBRACKET):
                    camera.changeSpeed(-10)
                elif(event.key == K_RIGHTBRACKET):
                    camera.changeSpeed(10)
                if(event.key == K_o):
                    pygame.display.set_mode((variables.windowWidth, variables.windowHeight))
                if(event.key == K_l):
                    user32 = ctypes.windll.user32
                    screensize = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
                    pygame.display.set_mode(screensize,FULLSCREEN)
                if event.key == K_p:
                    paused = True  
                if event.key == K_r:
                    world = World.world.World(camera, variables.worldWidth, variables.worldHeight)
                    UI = ui.UI(world)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 4:
                    variables.scaleUp()
                elif event.button == 5:
                    variables.scaleDown()                    
                elif event.button == 1:
                    mouseDown = True
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    mouseDown = False
                    
            if(mouseDown):
                UI.click(pygame.mouse.get_pos())
                        
    
        for k in Input.get_pressed():
            if(k.name=='right'):
                camera.move('right')
            if(k.name=='left'):
                camera.move('left')
            if(k.name=='up'):
                camera.move('up') 
            if(k.name=='down'):
                camera.move('down')        
    
        world.update(variables.screen)
        UI.update(variables.screen, world, clock, debug)
        pygame.display.flip()
    
    
    ##TODO##
    #Make collisions with stone/water... maybe calculate a bunch of hitboxes?
    #