import pygame,sys
from pygame.locals import *

def function_back_sceen(screen):
    pygame.draw.line(screen, (250, 155, 100), [0,0], [600,0], 50)
    pygame.draw.line(screen, (250, 155, 100), [0, 200], [600, 200], 50)
    pygame.draw.line(screen, (250, 155, 100), [0, 0], [0, 200], 50)
    pygame.draw.line(screen, (90, 255, 10), [600, 0], [600, 200], 50)
def function_object_update(screen,x,y):
    screen.fill((0, 0, 0));
    function_back_sceen(screen);
    image = pygame.image.load(r'image-tree.jpg')
    screen.blit(image, (400,135))
    screen.blit(image, (350, 135))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 5);
    pygame.draw.rect(screen, (10, 155, 100), (x - 15, y + 8, 30, 2));
    pygame.draw.rect(screen, (10, 155, 100), (x - 4, y + 12, 8, 20));
    pygame.draw.line(screen, (10, 155, 100), [x - 6, y + 40], [x, y + 32], 5)
    pygame.draw.line(screen, (10, 155, 100), [x, y + 32], [x + 4, y + 40], 5)
    pygame.display.update();

def function_display():

    pygame.init();
    screen = pygame.display.set_mode((600, 200));
    font = pygame.font.SysFont('tahoma', 40)
    label = font.render("Congratulations",1, (0, 255, 255))
    x=45;y=30;
    function_object_update(screen,x,y);
    while True:
        for event in pygame.event.get():
            if event.type== QUIT:
                sys.exit();
            if event.type == KEYDOWN:
                if event.key==K_LEFT:
                    if (x>45 and x<340) or (x>465)  or (x>45 and y<100):
                        x = x - 5;

                if event.key==K_RIGHT:
                    if (x > 460 and x<560) or (x < 335) or (x < 560 and y < 100):
                        x = x +5;
                if event.key==K_UP:
                    if y > 30:
                        y = y - 5;
                if event.key==K_DOWN:
                    if (y < 135 and ((x > 40 and x < 340) or (x > 460 and x < 565))) or (y < 95):
                        y = y + 5;
                function_object_update(screen,x,y);
                if (x==560):
                    screen.fill((0, 0, 0));
                    screen.blit(label,(200,50))
                    pygame.display.update();

if __name__=='__main__':
    function_display()