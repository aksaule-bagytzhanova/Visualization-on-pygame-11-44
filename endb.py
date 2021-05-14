import pygame, sys
from colour import Color


x=150
y=410

x1 = 250
y1 = 340


pygame.init()
clock = pygame.time.Clock()
screen_width,screen_height = 500, 500
screen = pygame.display.set_mode((screen_width,screen_height))


img = pygame.image.load("o2.png")
img1 = pygame.image.load("b1.png")
img2 = pygame.image.load("yu.jpg")
finished = False

while not finished:
    screen.fill((16711935))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y-=1
        y1-=1
    if keys[pygame.K_s]:
        y+=1
        y1+=1
    if y<= 250:
        screen.blit(img2,(0,0))

        
    pygame.draw.aalines(screen, (255,255,255), False,
                    [[200, 150], [200, 500]])
    pygame.draw.aalines(screen, (255,255,255), False,
                    [[300, 150], [300, 500]])
    

    #pygame.draw.rect(screen, (16711935), (0,0,400,150))
    pygame.draw.rect(screen, (255,255,255), (190,80,120,10))
    pygame.draw.aalines(screen, (255,255,255), False,
                    [[250, 80], [250, 170]])

    pygame.draw.circle(screen, (255,255,255), 
                   (250,150), 50)
    screen.blit(img,(x,y))
    screen.blit(img1,(x1,y1))
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished= True
pygame.quit()

