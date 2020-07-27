import pygame
import random

#Background sound
pygame.init()
pygame.mixer.init()

#colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (0,128,0)
blue = (30,144,255)
purpal = (131,111,255)
sky = (135,206,235)

#game window
window_width = 900
window_height = 600
Game_Window = pygame.display.set_mode((window_width,window_height))
pygame.display.update()

#Background image
bgimg = pygame.image.load("download.jpg")
bgimg = pygame.transform.scale(bgimg, (window_width, window_height)).convert_alpha()


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    Game_Window.blit(screen_text, [x, y])

def plot_snake(Game_Window, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(Game_Window, color, [x, y, snake_size, snake_size])


def welcome():
    game_exit = False
    pygame.display.set_caption("Snake Game Made By Ashutosh Kumar Gupta")
    Game_Window.fill(sky)
    text_screen("Snakes Game Me Aapka Swagat Hai!!!", purpal, 100, 180)
    text_screen("Press Enter To Continue ", purpal, 250, 275)

    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.load('Alan.mp3')
                    pygame.mixer.music.play()
                    game_loop()


        pygame.display.update()
        clock.tick(60)




#Game Loop
def game_loop():

    #game variables
    game_exit = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 20
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20, 350)
    food_y = random.randint(20, 300)
    init_velocity = 5
    score = 0
    fps = 60
    snk_list = []
    snk_length = 1

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    while not game_exit:
        if game_over:
            with open("hiscore.txt","w") as f:
                f.write(str(hiscore))
            Game_Window.fill((164,211,238))
            text_screen("Bechara!! ", green, 350, 180)
            text_screen("Koi Nhi, Well Try!! ", green, 280, 230)
            text_screen("Agar phir se khelna h to 'Space Bar' Key dbaao", green, 30, 280)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.music.load('Alan.mp3')
                        pygame.mixer.music.play()
                        game_loop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0




            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x-food_x)<20 and abs(snake_y-food_y)<20:
                score += 10
                food_x = random.randint(20, 350)
                food_y = random.randint(20, 300)
                snk_length +=5
                if score>int(hiscore):
                    hiscore = score


            Game_Window.fill((176,226,255))
            Game_Window.blit(bgimg,(0,0))
            pygame.display.set_caption(f"Score: {str(score)}                    High Score:{str(hiscore)}")
            pygame.draw.circle(Game_Window, red, [food_x, food_y], 10)


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

                pygame.mixer.music.load('game_over.mp3')
                pygame.mixer.music.play()


            if snake_x < 0 or snake_x > window_width or snake_y < 0 or snake_y > window_height:
                game_over = True
                pygame.mixer.music.load('game_over.mp3')
                pygame.mixer.music.play()


            plot_snake(Game_Window, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()

welcome()