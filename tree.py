from functools import cache
import pygame
pygame.init()
SIZE=1
ALTURA=20
RESOLUTION = (7680, 4320)
#Create a displace surface object
DISPLAYSURF = pygame.display.set_mode(RESOLUTION)
total_its = 0
mainLoop = True
cache = []
#pygame.event.get()
def draw(start=(0,0),end=(0,0), level = 0):
    global total_its
    global cache
    total_its+=1
    x_s , y_s = start
    x_e , y_e = end
    pygame.draw.line(DISPLAYSURF,(0,255,0),start,end,width=1)
    pygame.draw.circle(DISPLAYSURF,(255,0,0),start,2)
    
    for i in cache:
        if i == end or i == start:
            return
    if total_its%1000==0:
        pygame.display.update()
        pygame.event.get()
    if level <= 0:
        #pygame.draw.line(DISPLAYSURF,(0,255,0),start,end,width=1)
        return
    else:
        draw((x_e,y_e),(x_e+5+level*SIZE,y_e+ALTURA),level= level - 1)
        draw((x_e,y_e),(x_e+5+level*SIZE,y_e-ALTURA),level= level - 1)
        cache.append((x_e,y_e))
        cache.append((x_e+5+level*SIZE,y_e+ALTURA))
        
while mainLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False
    draw(start=(0,2160),end=(0,2160),level=100)
    cache=[]
    
    print(total_its)
    pygame.display.update()
    total_its = 0
    h , w = RESOLUTION
    rect = pygame.Rect(0, 0, h,w)
    sub = DISPLAYSURF.subsurface(rect)
    pygame.image.save(sub, "screenshot.jpg")
    mainLoop = False
pygame.quit()
