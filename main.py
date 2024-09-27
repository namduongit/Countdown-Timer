import pygame
import time
import math
pygame.init()


screen = pygame.display.set_mode((400, 600)) # 800x600 window
WHITE = (255, 255, 255) # RGB color for white
GREY = (150, 150, 150) # RGB color for grey
BLACK = (0, 0, 0) # RGB color for black
RED = (255, 0, 0) # RGB color for red

font = pygame.font.SysFont('sans', 50) # font object
text_1 = font.render('+', True, BLACK) # render the text
text_2 = font.render('+', True, BLACK) # render the text
text_3 = font.render('-', True, BLACK)
text_4 = font.render('-', True, BLACK)

text_start = font.render('Start', True, BLACK)
text_stop = font.render('Stop', True, BLACK)

total_sec, total_min = 0, 0
total = 0
start_button = False
stop_button = False

count_start = False
running = True

radius = 65
pi = math.pi

sound = pygame.mixer.Sound('bell.wav')
while running:
    screen.fill(GREY)
    # pygame.draw.rect(screen, WHITE, (100, 50, 150, 50)) # draw a white rectangle
    # pygame.draw.circle(screen, WHITE, (400, 300), 100) # draw a white circle

    mouse_x, mouse_y = pygame.mouse.get_pos()
    # print(mouse_x, mouse_y, sep=':')
    
    pygame.draw.rect(screen, WHITE, (50, 50, 50, 50))
    pygame.draw.rect(screen, WHITE, (50, 150, 50, 50))

    pygame.draw.rect(screen, WHITE, (150, 50, 50, 50))
    pygame.draw.rect(screen, WHITE, (250, 50, 100, 50))

    pygame.draw.rect(screen, WHITE, (150, 150, 50, 50))
    pygame.draw.rect(screen, WHITE, (250, 150, 100, 50))

    pygame.draw.rect(screen, BLACK, (40, 490, 320, 70))
    pygame.draw.rect(screen, WHITE, (50, 500, 300, 50))

    pygame.draw.circle(screen, BLACK, (200, 300), 75)
    pygame.draw.circle(screen, WHITE, (200, 300), 70)
    pygame.draw.circle(screen, BLACK, (200, 300), 5)

    screen.blit(text_1, (50, 50))
    screen.blit(text_2, (150, 50))

    screen.blit(text_3, (50, 150))
    screen.blit(text_4, (150, 150))
    

    # Reset button
    screen.blit(text_start, (250, 50))
    screen.blit(text_stop, (250, 150))


    


    for event in pygame.event.get(): # event loop: actions of the user will be added here
        if event.type == pygame.QUIT: # if the user clicks the close button
            running = False # stop the loop
        if event.type == pygame.MOUSEBUTTONDOWN: # if the user clicks the mouse
            if event.button == 1: 
                # print("Left click") # left click
                if (50 < mouse_x < 100) and (50 < mouse_y < 100):
                    # Plus Seconds
                    total_min += 1
                    total = total_sec + total_min * 60
            
                if (150 < mouse_x < 200) and (50 < mouse_y < 100):
                    # Plus Minutes
                    total_sec += 1
                    total = total_sec + total_min * 60
                if (50 < mouse_x < 100) and (150 < mouse_y < 200):
                    total_sec -= 1
                    total = total_sec + total_min * 60
                if (150 < mouse_x < 200) and (150 < mouse_y < 200):
                    total_min -= 1
                    total = total_sec + total_min * 60
                if (250 < mouse_x < 350) and (50 < mouse_y < 100):
                    start_button = True
                    count_start = True
                    stop_button = False
                        
                    stop_button = False
                if (250 < mouse_x < 350) and (150 < mouse_y < 200):
                    stop_button = True
                    start_button = False
                    

    

    if start_button:
        if total_sec > 0 or total_min > 0:
            total_sec -= 1
            if total_sec < 0: 
                total_min -= 1
                total_sec = 59
            time.sleep(0.03)
    if total_sec < 0:
        total_sec = 0
    if total_min < 0:
        total_min = 0
    if total_sec == 0 and total_min == 0: 
        start_button = False
        
    
    
    if total_sec + total_min * 60 == 0 and start_button == False and count_start == True:
        pygame.mixer.Sound.play(sound)
        count_start = False
    total_min += total_sec // 60
    total_sec = total_sec % 60

    time_now = str(total_min) + ':' + str(total_sec)
    text_time = font.render(time_now, True, BLACK)
    screen.blit(text_time, (20, 250))   


    pygame.draw.line(screen, BLACK, (200, 300), (200 + (math.sin((pi / 2) - (total_sec * pi / 60)) * 130 * math.sin(total_sec * pi / 60)), 235 + math.pow(math.sin(total_sec * pi / 60), 2) * 130))    
    pygame.draw.line(screen, BLACK, (200, 300), (200 + (math.sin((pi / 2) - (total_min * pi / 60)) * 100 * math.sin(total_min * pi / 60)), 235 + math.pow(math.sin(total_min * pi / 60), 2) * 100))

    
    if total != 0: pygame.draw.rect(screen, RED, (50, 500, int(300 * ((total_sec + total_min * 60) / total)), 50))

    pygame.display.flip() # update the display


pygame.quit()