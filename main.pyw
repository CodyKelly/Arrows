import sys
import ctypes
from ConfigParser import ConfigParser

from pygame import init, image, quit, QUIT, KEYDOWN, K_ESCAPE, FULLSCREEN, K_PERIOD, K_COMMA, K_QUOTE, K_SEMICOLON, K_p, display, time, K_F1, K_EQUALS, K_MINUS, K_LEFTBRACKET, K_RIGHTBRACKET, K_o, K_l, K_r, MOUSEBUTTONDOWN, MOUSEBUTTONUP, mouse, key, K_RIGHT, K_LEFT, K_UP, K_DOWN, K_w, K_a, K_s, K_d
import pygame.event as events

import data.ui






# Settings can be changed in the settings.ini file
from data import camera

init()

settings = ConfigParser()
settings.read('settings.ini')

# Display Settings
windowWidth = int(settings.get('DisplaySettings', 'window_width'))
windowHeight = int(settings.get('DisplaySettings', 'window_height'))

screen = display.set_mode((windowWidth, windowHeight))

display.set_icon(image.load('pictures/flowers/flower1.png'))
display.set_caption('Arrows!')

import data.world.world as World

world = World.World(screen, windowWidth, windowHeight)

worldSize = world.get_size('pixels')

camera = camera.Camera(worldSize)

clock = time.Clock()

UI = data.ui.UI(world, (windowWidth, windowHeight))

debug = False  # If true, shows FPS and other data on screen

paused = False

mouseDown = False

if __name__ == '__main__':

    while True:
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
                        paused = False
        else:
            clock.tick(60)
            screen.fill((0, 0, 0))
            for event in events.get():
                if event.type == QUIT:
                    quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        quit()
                        sys.exit()

                    '''This is supposed to save the world surface as a picture so
                    you can look at it later, but it isn't working right now'''
                    # if event.key == K_i:
                    #     st = str(datetime.datetime.utcnow())
                    #     pygame.image.save(world.get_surface(),'pictures/map/'+st+'.png')
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
                    if event.key == K_SEMICOLON:
                        camera.changeSpeed(-1)
                    elif event.key == K_QUOTE:
                        camera.changeSpeed(1)
                    if event.key == K_COMMA:
                        camera.changeSpeed(-0.1)
                    elif event.key == K_PERIOD:
                        camera.changeSpeed(0.1)
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
                        UI = data.ui.UI(world, (windowWidth, windowHeight))

                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 4:
                        world.scaleUp()
                    elif event.button == 5:
                        world.scaleDown()
                    elif event.button == 1:
                        mouseDown = True
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
