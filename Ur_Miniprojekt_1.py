import pygame
import math
import time

pygame.init() # Initialize Pygame
screen = pygame.display.set_mode((640, 640)) # Create a window of 640x640 pixels

run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False

    screen.fill((255, 255, 255)) # Fill the screen with white

    # klokke cirkel
    pygame.draw.circle(screen, (0, 0, 0), (320, 320), 210, 2) # tegner en cirkel med radius 200 og center i (320, 320)

    font = pygame.font.Font(None, 36) # opretter en font til tallet
    # tal til hver time
    for i in range(1, 13):
        angle_tal = math.radians(i * 30 - 90) # beregner vinklen for hvert tal
        x = 320 + 180 * math.cos(angle_tal) # beregner x-koordinaten for tallet
        y = 320 + 180 * math.sin(angle_tal) # beregner y-koordinaten for tallet
        text = font.render(str(i), True, (0, 0, 0)) # opretter en tekst med tallet
        text_rect = text.get_rect(center=(x, y)) # centrerer teksten på koordinaterne
        screen.blit(text, text_rect) # tegner teksten på skærmen

    # lav 12 punkter på cirklen for hver time
    for i in range(12):
        angle_punkt = math.radians(i * 30 + 90) # beregner vinklen for hvert punkt
        x = 320 + 200 * math.cos(angle_punkt) # beregner x-koordinaten for punktet
        y = 320 + 200 * math.sin(angle_punkt) # beregner y-koordinaten for punktet
        pygame.draw.line(screen, (0, 0, 0), (x, y), (x + 10 * math.cos(angle_punkt), y + 10 * math.sin(angle_punkt)), 2) # tegner en linje fra punktet til et punkt 10 pixels længere væk i samme retning



    # længder for sekundviser, minutviser og timeviser
    length_second = 200
    length_minute = 150
    length_hour = 100

    # center of the clock
    x_start = 320  
    y_start = 320
    start_pos = (x_start, y_start)

    # Time
    rn = time.gmtime()
    timer = rn.tm_hour+2
    minute = rn.tm_min
    second = rn.tm_sec


    # vinkel for sekundviser, minutviser og timeviser
    degree_second = second * 6 -90
    degree_minute = minute * 6 -90
    degree_hour = timer * 30 -90

    # sekundviser
    x_end_second = x_start + length_second * math.cos(math.radians(degree_second))
    y_end_second = y_start + length_second * math.sin(math.radians(degree_second))
    pygame.draw.line(screen, (0, 0, 0), (start_pos), (x_end_second, y_end_second), 2)
   

    # minutviser
    x_end_minute = x_start + length_minute * math.cos(math.radians(degree_minute))
    y_end_minute = y_start + length_minute * math.sin(math.radians(degree_minute))
    pygame.draw.line(screen, (0, 0, 0), (start_pos), (x_end_minute, y_end_minute), 3)



    # timeviser
    x_end_hour = x_start + length_hour * math.cos(math.radians(degree_hour))
    y_end_hour = y_start + length_hour * math.sin(math.radians(degree_hour))
    pygame.draw.line(screen, (0, 0, 0), (start_pos), (x_end_hour, y_end_hour), 5)  

    clock = pygame.time.Clock() # giver loopet en clock så den ikke kører for hurtigt
    dt = clock.tick(60)

    pygame.display.flip() # Update the display