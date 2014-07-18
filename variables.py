import pygame

'''This file is like an old habit of mine to just store random data into a file
so they're accessible from anywhere
I might modify it later to read these from a text file so people can edit it 
and shiz.'''

scale = 0.25
#Scale at which to render things. Used for zooming in/out.

windowWidth = 1000
windowHeight = 1000

tileSize = 16#tile width & height, in pixels
chunkSize = 10 #chunk size in tiles
worldWidth = 15 #world size in chunks
worldHeight = 90
realWorldWidth = worldWidth * chunkSize * tileSize #world size in pixels WE'VE GONE FULL CIRCLE
realWorldHeight = worldHeight * chunkSize * tileSize
'''how many chunks could a world chunk chunk if a world chunk could chunk chunks?
                                 ...dear god I've finally broke'''

seeRange = 2 #Number of chunks to load around player

screen = pygame.display.set_mode((windowWidth, windowHeight))

#The main surface, where everything is drawn.

def scaleUp():
    global scale
    if(scale < 1):
        scale += 0.125
    elif(scale >= 1 and scale < 2):
        scale += 0.25
def scaleDown():
    global scale
    if(scale > 1):
        scale -= 0.25
    if(scale <= 1 and scale >= 0.25):
        scale -= 0.125
