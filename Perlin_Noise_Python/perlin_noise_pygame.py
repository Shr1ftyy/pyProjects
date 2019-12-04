import pygame
import math
import random
import time
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (900,100)
genFPS = 1500
wScreen = 600
hScreen = 600
chunks = 0
genwidth = 600
genheight = 600
genScale = 0.5
tileSize = 12
genX = []
genY = []
Xshift = 1.2
Yshift = 1.3

dirt = pygame.image.load('green.png')
liquid = pygame.image.load('water.png')
sand = pygame.image.load('beach.png')
tree = pygame.image.load('leaves.png')
sprPlayer = pygame.image.load('oak.png')
nothing = pygame.image.load('nothing.png')

clock = pygame.time.Clock()

win = pygame.display.set_mode((wScreen, hScreen))
pygame.display.set_caption("Perlin Noise Algorithm by Syeam")


def chk():
	global o
	global t
	if t >= 1:
		o = random.uniform(o, genX[t - 1])

	if chunkGen.y >= tileSize:
		o = random.uniform(o,genY[t - 80])


###################################################
#												  #
#                                                 #
#				chunk generator					  #
#    											  #
###################################################
class chunkGen(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def draw(self, win):
		self.genBlock = (self.x, self.y, tileSize, tileSize)
		pygame.draw.rect(win, (0, 0, 0), self.genBlock,1)
		self.x += tileSize
		if self.x == genwidth:
			self.y += tileSize
			self.x = 0

#water block
class water(object):
	def __init__ (self, x, y):
		self.x = x
		self.y = y
	def draw(self, win):
		win.blit(liquid, (chunkGen.x , chunkGen.y))


#grass block
class grass(object):
	def __init__ (self, x, y):
		self.x = x
		self.y = y
	def draw(self, win):
		win.blit(dirt, (chunkGen.x, chunkGen.y))

#sand block
class beach(object):
	def __init__ (self, x, y):
		self.x = x
		self.y = y
	def draw(self, win):
	    win.blit(sand,(chunkGen.x, chunkGen.y))

#class player(object):
	#def __init__ (self, x, y, vel):
		#self.x = x
		#self.y = y
		#self.vel = vel
	#def draw(self, win):
		#win.blit(sprPlayer, (self.x, self.y))
	#def clear(self, win):
		#win.blit(nothing, (self.x, self.y))

#man = player(32,32,5)
sea = water(0, 0)
land = grass(0, 0)
beach = beach(0, 0)
chunkGen = chunkGen(-tileSize, 0)

t = -1
yeet = (random.random())
random.seed(yeet)
run = False
generate = False
preload = True

def stats():
	global t
	global o
	global genFPS
	global chunks
	global genX
	global genY
	global chunks

	os.system('clear')

	print("CHUNKS GENERATED: " + str(chunks))
	print("""chunk generation rate: """ + str(genFPS))
	print("frame: " + str(t))
	print("current chunk: " + str(o))
	if t >= 1:
		print("last chunk: " + str (genX[t-1]))
	if t >= 120:
		print("top chunk: " + str(genY[t-120]))

	if chunks < 2500*0.1:
		print("[#         ]")
	elif chunks < 2500*0.2:
		print("[##        ]")
	elif chunks < 2500*0.3:
		print("[###       ]")
	elif chunks < 2500*0.4:
		print("[####      ]")
	elif chunks < 2500*0.5:
		print("[#####     ]")
	elif chunks < 2500*0.6:
		print("[######    ]")
	elif chunks < 2500*0.7:
		print("[#######   ]")
	elif chunks < 2500*0.8:
		print("[########  ]")
	elif chunks < 2500*0.9:
		print("[######### ]")
	elif chunks < 2500*1:
		print("[##########] CHUNK GENERATION COMPLETE")



def noise():
	global genX
	global genY
	genX.append(random.uniform(0.0, 1.0))
	genY.append(random.uniform(0.0, 1.0))


while preload:
	noise()
	t += 1
	if t >= 14000:
		t = 0
		preload = False
		print(genX)
		print(genY)
		generate = True
#mainloop
#generation sequence
print("chunks generated: ")
while generate:
	pygame.event.get()
	pygame.display.update()
	clock.tick(genFPS)
	chunkGen.draw(win)
	o = genX[t]
	j = genY[t]
	if o and j <= 0.2:
		sea.draw(win)
		o = random.uniform(o, 0.4) * Xshift
		j = random.uniform(o, 0.4) * Yshift
		chk()
	elif o and j <= 0.4:
		beach.draw(win)
		chk()
	else:
		land.draw(win)
		o = random.uniform(0.4, o) * Xshift
		j = random.uniform(0.4, o) * Yshift
		chk()
	chunks += 1
	t += 1


	if chunks >= (genwidth/tileSize)*(genheight/tileSize):
		run = True
		pygame.display.update()
		generate = False
	stats()


## 	pygame.event.get()
## 	pygame.display.update
## 	clock.tick(60)
 ##	keys = pygame.key.get_pressed()

	##for event in pygame.event.get():
	##	if event.type == pygame.QUIT:
		##	pygame.quit()

	##            	if keys[pygame.K_LEFT]:
	  ##          		man.clear(win)
	    ##        		man.x -= man.vel
	 ##           	if keys[pygame.K_RIGHT]:
	 ##           	  	man.clear(win)
			##	man.x += man.vel
	      ##      	if keys[pygame.K_DOWN]:
	      ##      		man.clear(win)
		  ##  		man.y += man.vel
	       ##     	if keys[pygame.K_UP]:
		    ##		man.clear(win)
		 ##   		man.y -= man.vel

	# man.draw(win)

pygame.quit()