import pygame
import time
import math
pygame.init()
running_clock = True
# Set up the display
screen = pygame.display.set_mode((600, 700))

#  Set up the colors
GRAY = (160, 160, 160)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Set up the clock
mins = 0
secs = 0
start_time = False
stop_time = False


# Set up the math
radius_secs = 280
radius_mins = 240
pi = math.pi

# Set up the font
font = pygame.font.SysFont('Times New Roman', 30)

# Set up the text
plus_mins_text = font.render('Plus Mins', True, BLACK)
plus_secs_text = font.render('Plus Secs', True, BLACK)
start_text = font.render('START', True, BLACK)
stop_text = font.render('STOP', True, BLACK)
reset_text = font.render('RESET', True, BLACK)

total = 0
clock = pygame.time.Clock()
audio = pygame.mixer.Sound('bell.wav')
while running_clock:
    clock.tick(60)
    screen.fill(GRAY)
    pygame.draw.rect(screen, BLACK, (49, 49, 152, 52))
    pygame.draw.rect(screen, WHITE, (50, 50, 150, 50))

    pygame.draw.rect(screen, BLACK, (49, 149, 152, 52))
    pygame.draw.rect(screen, WHITE, (50, 150, 150, 50))

    pygame.draw.rect(screen, BLACK, (49, 249, 152, 52))
    pygame.draw.rect(screen, WHITE, (50, 250, 150, 50))

    pygame.draw.rect(screen, BLACK, (49, 349, 152, 52))
    pygame.draw.rect(screen, WHITE, (50, 350, 150, 50))
    
    pygame.draw.circle(screen, BLACK, (400, 225), 152)
    pygame.draw.circle(screen, WHITE, (400, 225), 150)
    pygame.draw.circle(screen, BLACK, (400, 225), 5)

    pygame.draw.rect(screen, BLACK, (49, 449, 202, 52))
    pygame.draw.rect(screen, WHITE, (50, 450, 200, 50))

    pygame.draw.rect(screen, BLACK, (49, 549, 502, 52))
    pygame.draw.rect(screen, WHITE, (50, 550, 500, 50))
    
    
    # x += 12, y += 7
    screen.blit(plus_mins_text, (62, 57))
    screen.blit(plus_secs_text, (62, 157))
    screen.blit(start_text, (62, 257))
    screen.blit(stop_text, (62, 357))
    for event in pygame.event.get():
        x, y = pygame.mouse.get_pos()
        '''
        x = event.pos[0]
        y = event.pos[1]
        '''

        if event.type == pygame.QUIT: running_clock = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (event.button == 1): # left_click
                if (50 < x < 200) and (50 < y < 100):
                    print("Plus Mins")
                    mins += 1
                    total = mins * 60 + secs
                if (50 < x < 200) and (150 < y < 200):
                    print("Plus Secs")
                    secs += 1
                    total = mins * 60 + secs
                if (50 < x < 200) and (250 < y < 300):
                    print("Start")
                    start_time = True
                    stop_time = False
                if (50 < x < 200) and (350 < y < 400):
                    print("Stop")
                    start_time = False
                    stop_time = True


    if start_time:
        if secs == 0 and mins == 0:
            start_time = False
            audio.play()
        else :
            secs -= 1
            if secs < 0:
                if mins > 0:
                    mins -= 1
                    secs = 59
        time.sleep(0.03)

    mins += secs // 60
    secs %= 60
    time_text = 'Time: ' + '%02d' % mins + ':' + '%02d' % secs
    time_display = font.render(time_text, True, BLACK)
    screen.blit(time_display, (62, 457))

    pygame.draw.line(screen, BLACK, (400, 225), (400 + math.sin(pi/2 - secs*pi/60)*280*math.sin(secs*pi/60), 85 + math.sin(secs*pi/60)*math.sin(secs*pi/60)*280), 2)
    pygame.draw.line(screen, RED, (400, 225), (400 + math.sin(pi/2 - mins*pi/60)*220*math.sin(mins*pi/60), 115 + math.sin(mins*pi/60)*math.sin(mins*pi/60)*220), 5)
    
    if total != 0:
        pygame.draw.rect(screen, '#FF6666', (50, 550, int(500 * (secs + mins * 60) / total), 50))
        
                
                
                
            
    
    pygame.display.flip() # update the display
            


pygame.quit() # quit pygame