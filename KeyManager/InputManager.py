import pygame
from pygame.locals import *

class Event():
    def __init__(self, name, keyList):
        self.keyList = keyList
        self.name = name
        self.pressed = False
    def has_event(self,key):
        if(key in self.keyList):
            return(True)
        else:
            return(False)

class Input():
    def __init__(self):
        self.eventList = []
        self.eventList.append(Event('right', [K_d, K_RIGHT]))
        self.eventList.append(Event('left', [K_a, K_LEFT]))
        self.eventList.append(Event('up', [K_w, K_UP]))
        self.eventList.append(Event('down', [K_s, K_DOWN]))      
        self.mouseDown = False
        
    def update(self, event):
        if(event.type == KEYDOWN):
            for thing in self.eventList:
                if(thing.has_event(event.key)):
                    thing.pressed = True
        if(event.type == KEYUP):
            for thing in self.eventList:
                if(thing.has_event(event.key)):
                    thing.pressed = False
        if(event.type == MOUSEBUTTONDOWN):
            self.mouseDown = True
        if(event.type == MOUSEBUTTONUP):
            self.mouseDown = False
    
    def get_pressed(self):
        pressedKeys = []
        for x in self.eventList:
            if(x.pressed):
                pressedKeys.append(x)
        return(pressedKeys)