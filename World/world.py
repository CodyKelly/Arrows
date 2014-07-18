import numpy, random, pygame, variables
from island_generator import *

'''So I might move the two tile-related classes into their own file 
but I'm feelin a little lazy right now so I'll do it later.'''

class Tile(object):
    '''A tile is basically a name and a picture. Any more convoluted than that
    and ur just plain dumb. Dummy.'''
    
    def __init__(self, name, pic, tileType):
        self.pic = pygame.image.load(pic).convert()
        self.name = name
        self.tileType = tileType
        self.scale = variables.scale
    def draw(self, surface, (x,y)):
        
        '''It also has the ability to make a picture of itself and post it on
        anything, just like a white girl.'''
        surface.blit(self.pic, (x,y))
    def get_type(self):
        return(self.tileType)
    
class Tiles(object):
    def __init__(self):
        self.tiles = []
        '''Bunch o' tiles types right here. Bunch of em. Okay, not THAT many
        but still, a good... what... fifteen or so? Maybe... seven?
        TODO: MAKE A PROGRAM TO COUNT THESE BITCHES'''
        self.tiles.append(Tile('grass1', 'pictures/grass/grass1.png','land'))
        self.tiles.append(Tile('grass2', 'pictures/grass/grass2.png','land'))
        self.tiles.append(Tile('grass3', 'pictures/grass/grass3.png','land'))
        self.tiles.append(Tile('grass4', 'pictures/grass/grass4.png','land'))
        self.tiles.append(Tile('grass5', 'pictures/grass/grass5.png','land'))
        self.tiles.append(Tile('flower1', 'pictures/flowers/flower1.png','land'))
        self.tiles.append(Tile('flower2', 'pictures/flowers/flower2.png','land'))
        self.tiles.append(Tile('flower3', 'pictures/flowers/flower3.png','land'))
        self.tiles.append(Tile('flower4', 'pictures/flowers/flower4.png','land'))
        self.tiles.append(Tile('sand1', 'pictures/sand/sand1.png','land'))
        self.tiles.append(Tile('sand2', 'pictures/sand/sand2.png','land'))
        self.tiles.append(Tile('sand3', 'pictures/sand/sand3.png','land'))
        self.tiles.append(Tile('sand4', 'pictures/sand/sand4.png','land'))
        self.tiles.append(Tile('sand5', 'pictures/sand/sand5.png','land'))
        self.tiles.append(Tile('bush', 'pictures/bush.png','land'))
        self.tiles.append(Tile('swater', 'pictures/swater.png','water'))
        self.tiles.append(Tile('water', 'pictures/water.png','water'))
        self.tiles.append(Tile('dwater', 'pictures/dwater.png','water'))
        print(str(len(self.tiles))+ ' tiles loaded') #added code to 'count these bitches'        
        #Now, these variables right heah (joisey talk right thaeh) control
        #what tiles have what range of values. So:
        self.dwaterline = 50 #if a value is above this, it's mid-level water
        self.waterline = 90 #if a value is above this, it's shallow water
        self.swaterline = 100 #if a value is above this, I DON'T KNOW WHAT HAPPENS!
        
        self.sandline = 135  #Oh it's sand, nvm
        
        
        self.grassline = 150
        
    def get_tile(self, name):
        for t in self.tiles:
            if t.name == name:
                return t
    def generate_tile(self, value):
        '''So uh, here we get a value and decide what kinda tile it is depending
        on the variables defined above (water line, sand line, etc.)
        and yeah that's all I have to say about that.'''
        if(value < self.dwaterline):
            tile = self.get_tile('dwater')
            return(tile)
        elif(value < self.waterline and value > self.dwaterline): 
            tile = self.get_tile('water')
            return(tile)
        elif(value < self.swaterline and value > self.waterline):
            tile = self.get_tile('swater')
            return(tile)
        elif(value > self.swaterline and value < self.sandline):
                rand2 = random.random()
                split = 1.0/5.0
                if(rand2 <= split):
                    tile = self.get_tile('sand1')
                    return(tile)
                elif(rand2 > split and rand2 <= split*2):
                    tile = self.get_tile('sand2')
                    return(tile)
                elif(rand2 > split*2 and rand2 <= split*3):
                    tile = self.get_tile('sand3')
                    return(tile)                   
                elif(rand2 > split*3 and rand2 <= split*4):
                    tile = self.get_tile('sand4')
                    return(tile)
                else:
                    tile = self.get_tile('sand5')
                    return(tile)
        elif(value > self.sandline and value < self.grassline):
            rand = random.random()
            if rand <= 0.6:
                rand2 = random.random()
                split = 1.0/5.0
                if(rand2 <= split):
                    tile = self.get_tile('sand1')
                    return(tile)
                elif(rand2 > split and rand2 <= split*2):
                    tile = self.get_tile('sand2')
                    return(tile)
                elif(rand2 > split*2 and rand2 <= split*3):
                    tile = self.get_tile('sand3')
                    return(tile)                   
                elif(rand2 > split*3 and rand2 <= split*4):
                    tile = self.get_tile('sand4')
                    return(tile)
                else:
                    tile = self.get_tile('sand5')
                    return(tile)            
            elif rand > 0.6 and rand <= 0.985:
                # Deciding what grass the tile is, makes the ground look more varied.
                rand2 = random.random()
                split = 1.0/5.0
                if(rand2 <= split):
                    tile = self.get_tile('grass1')
                    return(tile)
                elif(rand2 > split and rand2 <= split*2):
                    tile = self.get_tile('grass2')
                    return(tile)
                elif(rand2 > split*2 and rand2 <= split*3):
                    tile = self.get_tile('grass3')
                    return(tile)                   
                elif(rand2 > split*3 and rand2 <= split*4):
                    tile = self.get_tile('grass4')
                    return(tile)
                else:
                    tile = self.get_tile('grass5')
                    return(tile)
            elif rand > 0.985 and rand <= 0.99:
                #Bush
                tile = self.get_tile('bush')
                return(tile)
            elif rand > 0.99 and rand <= 1:
                #Flower
                rand2 = random.randint(1,4)
                if rand2 == 1:
                    tile = self.get_tile('flower1')
                    return(tile)
                if rand2 == 2: 
                    tile = self.get_tile('flower2')
                    return(tile)
                if rand2 == 3:               
                    tile = self.get_tile('flower3')
                    return(tile)
                if rand2 == 4:       
                    tile = self.get_tile('flower4')
                    return(tile)
        elif(value > self.sandline):
            rand = random.random()            
            if rand <= 0.985:
                # Deciding what grass the tile is, makes the ground look more varied.
                rand2 = random.random()
                split = 1.0/5.0
                if(rand2 <= split):
                    tile = self.get_tile('grass1')
                    return(tile)
                elif(rand2 > split and rand2 <= split*2):
                    tile = self.get_tile('grass2')
                    return(tile)
                elif(rand2 > split*2 and rand2 <= split*3):
                    tile = self.get_tile('grass3')
                    return(tile)                   
                elif(rand2 > split*3 and rand2 <= split*4):
                    tile = self.get_tile('grass4')
                    return(tile)
                else:
                    tile = self.get_tile('grass5')
                    return(tile)
            elif rand > 0.985 and rand <= 0.99:
                #Bush
                tile = self.get_tile('bush')
                return(tile)
            elif rand > 0.99 and rand <= 1:
                #Flower
                rand2 = random.randint(1,4)
                if rand2 == 1:
                    tile = self.get_tile('flower1')
                    return(tile)
                if rand2 == 2: 
                    tile = self.get_tile('flower2')
                    return(tile)
                if rand2 == 3:               
                    tile = self.get_tile('flower3')
                    return(tile)
                if rand2 == 4:       
                    tile = self.get_tile('flower4')
                    return(tile)
                
Tiles = Tiles() #making a tiles object to do stuff with

'''I should really comment the rest of this program
TODO: GET ON MY LAZY ASS AND FUCKIN' COMMENT THIS SHIT
AND DON'T COME BACK UNTIL IT'S FINISHED OR I'LL WHIP MYSELF'''

class Chunk(object):
    '''It's a chunk of data, stupid, what else would it be?'''
    
##Chunk Initialization    
    
    def __init__(self,(x,y), size, map):
        self.x = x
        self.y = y
        self.tileList = numpy.zeros([size,size], dtype=Tile)
        self.surface = pygame.Surface((size*variables.tileSize,size*variables.tileSize))
        self.originalSurface = self.surface
        #This variable is for later
        valueAvg = 0
        for x in range(0,size):
            for y in range(0,size):
                #First the chunk gets its raw values from the world map
                try:
                    value = map[self.y + y][self.x + x]
                    #Then it passes the values to the Tiles class, gets back a tile,
                    #and stores it into its tileList
                    self.tileList[x][y] = Tiles.generate_tile(value)
                    #Then it blits the tile onto its surface
                    self.tileList[x][y].draw(self.surface, (x*variables.tileSize,y*variables.tileSize))
                    #And BAM! we got ourselves a nice new chunk with a bunch of tiles and its
                    #very own surface
                    
                    #Now we're going to determine this chunk's type, whether it be land or water.
                    #To do this, we'll get the sum of all the tile values
                    valueAvg += value
                except: IndexError
                
        #Then we'll divide it by how many tiles this chunk has, giving us an average value
        valueAvg /= size ** 2
        #then we pass it to the tile generator, and the type of the tile returned will be this chunk's type.
        self.chunkType = Tiles.generate_tile(valueAvg).get_type()
        self.avgHeight = valueAvg #We'll keep this average height stored because it may be handy later
    def get_type(self):
        return(self.chunkType) 
    def get_tile(self, (x,y)):
        
        return(self.tileList[x][y])
                
##Chunk draw function

    def draw(self, surface, (x,y), scale):
        #the chunk detects a scale change by determining if its original surface width multiplied by the scale is equal to its current surface width.
        if not(int(self.originalSurface.get_width()*scale) == int(self.surface.get_width())):
            self.surface = None
            #if it isn't, it changes its current surface to a new one that fits the scale
            self.surface = pygame.Surface((self.originalSurface.get_width()*scale,self.originalSurface.get_height()*scale))
            #and scales its original surface to the new one.
            pygame.transform.scale(self.originalSurface,self.surface.get_size(),self.surface)
            #badda bing badda boom.
        surface.blit(self.surface,(self.x*scale*variables.tileSize-x,self.y*scale*variables.tileSize-y))
    def get_surface(self):
        return(self.surface)

class World(object):
    '''THIS CLASS, THIS CLASS RIGHT HERE. YA GOTTA HAND IT TO THIS CLASS
    The World simply holds all the chunks and manages any objects in the game.'''
    
##World initialization
    
    def __init__(self, camera, width, height):
        self.camera = camera
        self.height = height #world height, in chunks.
        self.width = width
        self.chunkSize = variables.chunkSize #chunk size, in worlds. I mean tiles.
        self.tileSize = variables.tileSize 
        self.objectSurface = pygame.Surface((variables.windowWidth, variables.windowHeight)) # Surface for objects to draw themselves on
        self.chunks = numpy.zeros([self.width, self.height],dtype=Chunk) #REMEMBER THOSE CHUNKS FRUM B4? YEAH THEY LIVE IN HERE.
        self.offsetX = 0
        self.offsetY = 0
        
        '''This so-called 'map' is a matrix thingy that holds all the raw world data values. 
        This is what gets passed to the chunks when they're created'''
        map = IslandGenerator().generate_island(self.width*self.chunkSize,self.height*self.chunkSize,.125,6) 
        print(len(map))
        print(len(map[0]))
        
        '''And here we see the birth of several young chunks. Watch as they try to stand up
        and get accustomed to using their newfound legs. Aren't they adorable?'''
        c = 0
        print('generating chunks...')
        for x in range(0, self.width):
            for y in range(0, self.height):
                c+=1
                self.chunks[x][y] = Chunk((x*self.chunkSize,y*self.chunkSize), self.chunkSize, map)
        print('chunks generated.')
        
        self.worldGroup = pygame.sprite.Group()
        
        '''These here groups hold different kind of objects so it's easy for other objects to find each other.
        The world group contains all objects, and then the groups below that hold specific ones.
        Such organization'''
        
##World Updating

    def update(self, screen):
        '''So here we're gonna update only the chunks immediately surrounding
        the camera. In my old system the whole map was updated all at once so believe me
        when I say that this is a huge improvement.'''
        
##Chunk Updating                
        (pX,pY) = self.camera.get_pos() #these coordinates are in pixels, so...
        display = pygame.display.get_surface()
        (self.offsetX,self.offsetY) = (pX*variables.scale-display.get_width()/2,pY*variables.scale-display.get_height()/2)
        pX = int(pX/self.tileSize/self.chunkSize)#we convert them to tile and then chunk coords
        pY = int(pY/self.tileSize/self.chunkSize)
        
        windowWidth = screen.get_width()
        windowHeight = screen.get_height()
        
        renderRangeX = variables.realWorldWidth-windowWidth/variables.tileSize/variables.chunkSize+1
        renderRangeY = variables.realWorldHeight-windowHeight/variables.tileSize/variables.chunkSize+1
        
        #int((float(display.get_width())/(float(variables.realWorldSize)*variables.scale))*float(variables.worldWidth))+1
        

        for x in range(self.width):
            for y in range(self.height):
                if(x > pX - renderRangeX and x < pX + renderRangeX and y > pY - renderRangeY and y < pY + renderRangeY):
                    self.chunks[x][y].draw(screen, (self.offsetX, self.offsetY),variables.scale)
        '''Going through the object list, updating stuff'''
        
##Object Updating        
        self.worldGroup.update()
        self.worldGroup.draw(screen)
        
    def move(self,direction):
        
        '''Not really sure why this function exists in this class, but uh, fuck you, I'm leaving it here.'''
        
        moveSpeed = 5
        if(direction=='left'):
            if(self.offsetX<0):
                self.offsetX += moveSpeed
        elif(direction=='right'):
            if(self.offsetX>=(variables.windowWidth-self.mapSurface.get_width())+moveSpeed):
                self.offsetX -= moveSpeed
        elif(direction=='up'):
            if(self.offsetY<0):
                self.offsetY += moveSpeed
        elif(direction=='down'):
            if(self.offsetY>=(variables.windowHeight-self.mapSurface.get_height())+moveSpeed):
                self.offsetY -= moveSpeed
##Getters/Setters
##Or, looking at it again, maybe just getters.
    
    def get_surface(self):
        return(self.objectSurface)
    
    def add_object(self, o):
        self.worldGroup.add(o)
    
    def remove_object(self, o):
        self.worldGroup.remove(o)
        
    def get_group(self):
        return(self.worldGroup)   
    def get_chunk(self, (x,y)):
        x = int(x/variables.tileSize/variables.chunkSize)-1
        y = int(y/variables.tileSize/variables.chunkSize)-1
        return(self.chunks[x][y])
    def get_chunks(self):
        return self.chunks
    #def get_tile(self, (x,y)):
        #chunkX = int(x/variables.tileSize/variables.chunkSize)
        #chunkY = int(x/variables.tileSize/variables.chunkSize)
        #tileX = int(x/variables.tilesSize) - int(x/variables.
        #self.chunks[chunkX][chunkY].get_tile(
    
    def get_camera(self):
        return(self.camera)
    def getChunkWidth(self):
        return(self.width/self.chunkSize)
    def getChunkHeight(self):
        return(self.height/self.chunkSize)