import pygame
import sys
import ui
import camera
import ctypes
import ConfigParser 

# Settings can be changed in the settings.ini file

pygame.init()

settings = ConfigParser.ConfigParser()
settings.read('settings.ini')

# Display Settings
windowWidth = int(settings.get('DisplaySettings', 'window_width'))
windowHeight = int(settings.get('DisplaySettings', 'window_height'))

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

UI = ui.UI(world, (windowWidth, windowHeight))

debug = False  # If true, shows FPS and other data on screen

paused = False

mouseDown = False

if __name__ == '__main__':

    while True:
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
                        paused = False
        else:
            clock.tick(60)
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                    '''This is supposed to save the world surface as a picture so
                    you can look at it later, but it isn't working right now'''
                    # if event.key == K_i:
                    #     st = str(datetime.datetime.utcnow())
                    #     pygame.image.save(world.get_surface(),'pictures/map/'+st+'.png')
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
                    if event.button == 4:
                        world.scaleUp()
                    elif event.button == 5:
                        world.scaleDown()
                    elif event.button == 1:
                        mouseDown = True
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
