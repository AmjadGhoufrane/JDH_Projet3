import pygame
from pygame import mixer
from fighter import *
from parametres import *
from secret import *

class Fight:
    def __init__(self):
        mixer.init()
        pygame.init()

        #creation fenetre
        SCREEN_WIDTH = xd
        SCREEN_HEIGHT = yd

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        clock = pygame.time.Clock()
        FPS = 60

        #couleurs
        RED = (255, 0, 0)
        BLUE = (0, 0, 255)
        WHITE = (255, 255, 255)

        #variables du jeux
        intro_count = 3
        last_count_update = pygame.time.get_ticks()
        round_over = False
        ROUND_OVER_COOLDOWN = 2000

        #variables joueurs
        WARRIOR_SIZE = 162
        WARRIOR_SCALE = 4
        WARRIOR_OFFSET = [72, 56]
        WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
        WIZARD_SIZE = 250
        WIZARD_SCALE = 3
        WIZARD_OFFSET = [112, 107]
        WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]

        #musique et sons
        sword_fx = pygame.mixer.Sound("assets/audio/sword.wav")
        sword_fx.set_volume(0.1)
        magic_fx = pygame.mixer.Sound("assets/audio/magic.wav")
        magic_fx.set_volume(0.2)

        #load images
        bg_image = pygame.image.load("assets/images/background/background.jpg")

        warrior_sheet = pygame.image.load("assets/images/warrior/Sprites/warrior.png")
        wizard_sheet = pygame.image.load("assets/images/wizard/Sprites/wizard.png")

        victory_img = pygame.image.load("assets/images/icons/victory.png")

        #etapes pour chaque animation
        WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
        WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]

        #police
        count_font = pygame.font.Font("assets/police/turok.ttf", 80)

        #dessine le texte
        def draw_text(text, font, text_col, x, y):
          img = font.render(text, True, text_col)
          screen.blit(img, (x, y))

        #dessine le fond
        def draw_bg():
          scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
          screen.blit(scaled_bg, (0, 0))

        # dessine barre de vie
        def draw_health_bar(vie, x, y):
          ratio = vie / 100
          pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
          pygame.draw.rect(screen, RED, (x, y, 400, 30))
          pygame.draw.rect(screen, BLUE, (x, y, 400 * ratio, 30))


        #crée deux instances of joueurs
        fighter_1 = Fighter(1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
        fighter_2 = Enemy(2, 1400, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)

        #loop
        run = True
        while run:

          clock.tick(FPS)

          draw_bg()

          #stat du joueur
          draw_health_bar(fighter_1.health, 20, 20)
          draw_health_bar(fighter_2.health, 1275, 20)

          #update countdown
          if intro_count <= 0:
            #mouvements joueurs
            fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, round_over)
            fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, round_over)
          else:
            #affiche timer
            draw_text(str(intro_count), count_font, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
            #update timer
            if (pygame.time.get_ticks() - last_count_update) >= 1000:
              intro_count -= 1
              last_count_update = pygame.time.get_ticks()

          fighter_1.update()
          fighter_2.update()

          fighter_1.draw(screen)
          fighter_2.draw(screen)

          #verifie si le joueur est vaincu
          if round_over == False:
            if fighter_1.alive == False:
              round_over = True
              round_over_time = pygame.time.get_ticks()
            elif fighter_2.alive == False:
              round_over = True
              round_over_time = pygame.time.get_ticks()
          else:
            #affiche victoire
            screen.blit(victory_img, (360, 150))
            if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
              round_over = False
              intro_count = 3
              fighter_1 = Fighter(1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
              fighter_2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)
          if round_over == True :
              shh = Secret()
              while shh.continuer:
                  shh.Main()
          #gere evenement 
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              run = False


          pygame.display.update()

        #exit pygame
        pygame.quit()