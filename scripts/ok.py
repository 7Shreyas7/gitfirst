import pygame
#A program which uses pygame
pygame.init()
display_width=800
display_height=600
carImg= pygame.image.load('../resources/racecar.png')
white=(255,255,255)
black = (0,0,0)
x=display_width*0.45
y=display_height*0.75
x_change = 0
y_change = 0

def car(x,y):
    gameDisplay.blit(carImg,(x,y))


gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('A bit Racey')

clock = pygame.time.Clock()

crashed = False

while not crashed:
    for event in pygame.event.get():
        print (event)
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            elif event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                y_change = 0
    x+=x_change
    y+=y_change
    gameDisplay.fill(white)
    car(x,y)
    pygame.display.update()
    clock.tick(30)

pygame.quit()
