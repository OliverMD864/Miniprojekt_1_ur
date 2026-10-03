import pygame
import math
import time

pygame.init() 
screen = pygame.display.set_mode((640, 640)) # laver et vindue af 640x640 pixels

run_ur = True
while run_ur is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_ur = False

    # gmtime og så i danmark er det +2 pga sommertid
    rn = time.gmtime()
    timer = rn.tm_hour+2
    minute = rn.tm_min
    second = rn.tm_sec


    #timer = 19
    #minute = 0
    
    tid_decimal = (timer + minute / 60) % 24
    sol_degree = (tid_decimal - 12) * 15 - 90

    if tid_decimal < 6 or tid_decimal >= 18:
        baggrund = (15, 20, 50) # nat
        visere_og_urfarve = (255, 255, 255)
    else:
        baggrund = (135, 206, 235) # dag
        visere_og_urfarve = (0, 0, 0)
    
    screen.fill((baggrund)) 

    # klokke cirkel
    pygame.draw.circle(screen, (visere_og_urfarve), (320, 320), 210, 2) # tegner en cirkel med radius 200 og center i (320, 320)

    font = pygame.font.Font(None, 36) # opretter en font til tallet
    # tal til hver time
    for i in range(1, 13):
        angle_tal = math.radians(i * 30 - 90) # 360/30 = 12 grader pr. time
        x = 320 + 180 * math.cos(angle_tal) # beregner x-koordinaten for tallet
        y = 320 + 180 * math.sin(angle_tal) # beregner y-koordinaten for tallet
        text = font.render(str(i), True, (visere_og_urfarve)) # opretter en tekst med tallet
        text_rect = text.get_rect(center=(x, y)) # centrerer teksten på koordinaterne
        screen.blit(text, text_rect) # tegner teksten på skærmen

    for i in range(60):
        if i % 5 == 0: # når 5 rammer tal den går op i uden rest, rest = 0 skal den continue og lave et nyt punkt
            continue
        angle_punkt = math.radians(i * 6 + 90) # 360/60 = 6 grader pr. minut
        x = 320 + 200 * math.cos(angle_punkt) # beregner x-koordinaten for punktet
        y = 320 + 200 * math.sin(angle_punkt) # beregner y-koordinaten for punktet
        pygame.draw.line(screen, (visere_og_urfarve), (x, y), (x + 8 * math.cos(angle_punkt), y + 8 * math.sin(angle_punkt)), 2)
        

    # lav 12 punkter på cirklen for hver time
    for i in range(12):
        angle_punkt = math.radians(i * 30 + 90) # beregner vinklen for hvert punkt
        x = 320 + 195 * math.cos(angle_punkt) # beregner x-koordinaten for punktet
        y = 320 + 195 * math.sin(angle_punkt) # beregner y-koordinaten for punktet
        pygame.draw.line(screen, (visere_og_urfarve), (x, y), (x + 15 * math.cos(angle_punkt), y + 15 * math.sin(angle_punkt)), 5) # tegner en linje fra punktet til et punkt 10 pixels længere væk i samme retning


     # længder for sekundviser, minutviser og timeviser
    length_second = 200
    length_minute = 150
    length_hour = 100

    # center for uret
    x_start = 320  
    y_start = 320
    start_pos = (x_start, y_start)


    # vinkel for sekundviser, minutviser og timeviser
    degree_second = second * 6 -90
    degree_minute = (minute + second / 60) * 6 -90 # / 60 deler minuttets 6 grader op i 60 skridt 0,1 pr. sekund, så viseren glider
    degree_hour = (timer + minute / 60) * 30 -90 # / 60 deler timens 30 grader op i 60 skridt 0,5 pr. minut, så viseren glider


    
    sol_x = 320 + 80 * math.cos(math.radians(sol_degree))
    sol_y = 320 + 80 * math.sin(math.radians(sol_degree))
    
    mone_degree = sol_degree + 180
    mone_x = 320 + 80 * math.cos(math.radians(mone_degree))
    mone_y = 320 + 80 * math.sin(math.radians(mone_degree))
    
    
    sol_farve = (255, 200, 0)
    sol_position = (sol_x, sol_y)
    sol_radius = 20
    
    mone_farve = (180, 180, 200)
    mone_position = (mone_x, mone_y)
    mone_radius = 12
    
    pygame.draw.circle(screen, sol_farve, sol_position, sol_radius)
    pygame.draw.circle(screen, mone_farve, mone_position, mone_radius)
    
    pygame.draw.line(screen, (0,0,0), (160,320), (480,320), 2)

    # sekundviser
    x_end_second = x_start + length_second * math.cos(math.radians(degree_second))
    y_end_second = y_start + length_second * math.sin(math.radians(degree_second))
    pygame.draw.line(screen, (visere_og_urfarve), (start_pos), (x_end_second, y_end_second), 2)
   

    # minutviser
    x_end_minute = x_start + length_minute * math.cos(math.radians(degree_minute))
    y_end_minute = y_start + length_minute * math.sin(math.radians(degree_minute))
    pygame.draw.line(screen, (visere_og_urfarve), (start_pos), (x_end_minute, y_end_minute), 3)


    # timeviser
    x_end_hour = x_start + length_hour * math.cos(math.radians(degree_hour))
    y_end_hour = y_start + length_hour * math.sin(math.radians(degree_hour))
    pygame.draw.line(screen, (visere_og_urfarve), (start_pos), (x_end_hour, y_end_hour), 5)  



    clock = pygame.time.Clock() # giver loopet en clock så den ikke kører for hurtigt
    dt = clock.tick(60)

    pygame.display.flip() 