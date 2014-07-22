<<<<<<< HEAD
import sys
import ctypes
from ConfigParser import ConfigParser

from pygame import init, image, quit, QUIT, KEYDOWN, K_ESCAPE, FULLSCREEN, K_p, display, time, K_F1, K_EQUALS, K_MINUS, K_LEFTBRACKET, K_RIGHTBRACKET, K_o, K_l, K_r, MOUSEBUTTONDOWN, MOUSEBUTTONUP, mouse, key, K_RIGHT, K_LEFT, K_UP, K_DOWN, K_w, K_a, K_s, K_d
import pygame.event as events

import ui
import camera



# Settings can be changed in the settings.ini file

init()

settings = ConfigParser()
=======
import pygame
import sys
import ui
import camera
import ctypes
import ConfigParser 

# Settings can be changed in the settings.ini file

pygame.init()

settings = ConfigParser.ConfigParser()
>>>>>>> 4ecb01b3859532b2862cc4f12464180bfeb4ce08
settings.read('settings.ini')

# Display Settings
windowWidth = int(settings.get('DisplaySettings', 'window_width'))
windowHeight = int(settings.get('DisplaySettings', 'window_height'))

<<<<<<< HEAD
screen = display.set_mode((windowWidth, windowHeight))

display.set_icon(image.load('pictures/flowers/flower1.png'))
display.set_caption('Arrows!')

import World.world as World

world = World.World(screen, windowWidth, windowHeight)

worldSize = world.get_size('pixels')

camera = camera.Camera(worldSize)

clock = time.Clock()
=======
screen = pygame.display.set_mode((windowWidth, windowHeight))

pygame.display.set_icon(pygame.image.load('pictures/flowers/flower1.png'))
pygame.display.set_caption('Arrows!')     

import World.world as World

# World Settings
worldWidth = int(settings.get('WorldSettings', 'world_width'))
worldHeight = int(settings.get('WorldSettings', 'world_height'))
chunkSize = int(settings.get('WorldSettings', 'chunk_size'))
tileSize = int(settings.get('WorldSettings', 'tile_size'))
worldPixelWidth = worldWidth*chunkSize*tileSize
worldPixelHeight = worldHeight*chunkSize*tileSize

camera = camera.Camera((worldPixelWidth, worldPixelHeight))

world = World.World(camera, worldWidth, worldHeight, chunkSize, tileSize, screen, windowWidth, windowHeight)

clock = pygame.time.Clock()
>>>>>>> 4ecb01b3859532b2862cc4f12464180bfeb4ce08

UI = ui.UI(world, (windowWidth, windowHeight))

debug = False  # If true, shows FPS and other data on screen

paused = False

mouseDown = False

if __name__ == '__main__':

    while True:
<<<<<<< HEAD
        if paused:
            clock.tick(60)
            for event in events.get():
                if event.type == QUIT:
                    quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            quit()
                            sys.exit()
                    if event.key == K_p:
=======
        pygame.event.pump()
        if(paused):
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                    if event.key == pygame.K_p:
>>>>>>> 4ecb01b3859532b2862cc4f12464180bfeb4ce08
                        paused = False
        else:
            clock.tick(60)
            screen.fill((0, 0, 0))
<<<<<<< HEAD
            for event in events.get():
                if event.type == QUIT:
                    quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        quit()
=======
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
>>>>>>> 4ecb01b3859532b2862cc4f12464180bfeb4ce08
                        sys.exit()

                    '''This is supposed to save the world surface as a picture so
                    you can look at it later, but it isn't working right now'''
                    # if event.key == K_i:
                    #     st = str(datetime.datetime.utcnow())
                    #     pygame.image.save(world.get_surface(),'pictures/map/'+st+'.png')
<<<<<<< HEAD
                    if event.key == K_F1:
                        if not debug:
                            debug = True
                        else:
                            debug = False
                    if event.key == K_EQUALS:
                        world.scaleUp()
                    elif event.key == K_MINUS:
                        world.scaleDown()
                    if event.key == K_LEFTBRACKET:
                        camera.changeSpeed(-10)
                    elif event.key == K_RIGHTBRACKET:
                        camera.changeSpeed(10)
                    if event.key == K_o:
                        display.set_mode((windowWidth, windowHeight))
                    if event.key == K_l:
                        user32 = ctypes.windll.user32
                        screensize = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
                        display.set_mode(screensize, FULLSCREEN)
                    if event.key == K_p:
                        paused = True
                    if event.key == K_r:
                        world = World.World(screen, windowWidth, windowHeight)
                        UI = ui.UI(world)

                if event.type == MOUSEBUTTONDOWN:
=======
                    if(event.key == pygame.K_F1):
                        if not(debug):
                            debug = True
                        else:
                            debug = False
                    if(event.key == pygame.K_EQUALS):
                        world.scaleUp()
                    elif(event.key == pygame.K_MINUS):
                        world.scaleDown()
                    if(event.key == pygame.K_LEFTBRACKET):
                        camera.changeSpeed(-10)
                    elif(event.key == pygame.K_RIGHTBRACKET):
                        camera.changeSpeed(10)
                    if(event.key == pygame.K_o):
                        pygame.display.set_mode((windowWidth, windowHeight))
                    if(event.key == pygame.K_l):
                        user32 = ctypes.windll.user32
                        screensize = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
                        pygame.display.set_mode(screensize, FULLSCREEN)
                    if event.key == pygame.K_p:
                        paused = True
                    if event.key == pygame.K_r:
                        world = World.World(camera, (worldWidth, worldHeight), chunkSize, tileSize)
                        UI = ui.UI(world)

                if event.type == pygame.MOUSEBUTTONDOWN:
>>>>>>> 4ecb01b3859532b2862cc4f12464180bfeb4ce08
                    if event.button == 4:
                        world.scaleUp()
                    elif event.button == 5:
                        world.scaleDown()
                    elif event.button == 1:
                        mouseDown = True
<<<<<<< HEAD
                if event.type == MOUSEBUTTONUP:
                    if event.button == 1:
                        mouseDown = False

                if mouseDown:
                    UI.click(mouse.get_pos(), camera)
                    
            keys = key.get_pressed()
            if keys[K_w] or keys[K_UP]:
                camera.move('up')
            if keys[K_a] or keys[K_LEFT]:
                camera.move('left')
            if keys[K_s] or keys[K_DOWN]:
                camera.move('down')
            if keys[K_d] or keys[K_RIGHT]:
                camera.move('right')            

            world.update(screen, camera)
            UI.update(screen, world, clock, debug, camera)
            display.flip()
=======
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        mouseDown = False

                if(mouseDown):
                    UI.click(pygame.mouse.get_pos())
                    
            keys = pygame.key.get_pressed()
            if(keys[pygame.K_w] or keys[pygame.K_UP]):
                camera.move('up')
            if(keys[pygame.K_a] or keys[pygame.K_LEFT]):
                camera.move('left')
            if(keys[pygame.K_s] or keys[pygame.K_DOWN]):
                camera.move('down')
            if(keys[pygame.K_d] or keys[pygame.K_RIGHT]):
                camera.move('right')            

            world.update(screen)
            UI.update(screen, world, clock, debug)
            pygame.display.flip()
>>>>>>> 4ecb01b3859532b2862cc4f12464180bfeb4ce08
