import pygame
import random

class Fighter():
  def __init__(self, player, x, y, flip, data, sprite_sheet, animation_steps, sound):
    self.player = player
    self.size = data[0]
    self.image_scale = data[1]
    self.offset = data[2]
    self.flip = flip
    self.animation_list = self.load_images(sprite_sheet, animation_steps)
    self.action = 0
    self.frame_index = 0
    self.image = self.animation_list[self.action][self.frame_index]
    self.update_time = pygame.time.get_ticks()
    self.rect = pygame.Rect((x, y, 80, 180))
    self.vel_y = 0
    self.running = False
    self.jump = False
    self.attacking = False
    self.attack_type = 0
    self.attack_cooldown = 0
    self.attack_sound = sound
    self.hit = False
    self.health = 100
    self.alive = True


  def load_images(self, sprite_sheet, animation_steps):
    animation_list = []
    y=0
    for animation in animation_steps:
      temp_img_list = []
      for x in range(animation):
        temp_img = sprite_sheet.subsurface(x * self.size, y * self.size, self.size, self.size)
        temp_img_list.append(pygame.transform.scale(temp_img, (self.size * self.image_scale, self.size * self.image_scale)))
      animation_list.append(temp_img_list)
      y+=1
    return animation_list


  def move(self, screen_width, screen_height, surface, target, round_over):
    SPEED = 15
    GRAVITY = 2
    dx = 0
    dy = 0
    self.running = False
    self.attack_type = 0

    key = pygame.key.get_pressed()

    #ne peux effectuer autres action que si il n'attaque pas
    if self.attacking == False and self.alive == True and round_over == False:
      if self.player == 2:
        #mouvements
        if key[pygame.K_a]:
          dx = -SPEED
          self.running = True
        if key[pygame.K_d]:
          dx = SPEED
          self.running = True
        #saut
        if key[pygame.K_w] and self.jump == False:
          self.vel_y = -30
          self.jump = True
        #attaque
        if key[pygame.K_r] or key[pygame.K_t]:
          self.attack(target)
          #choix attaque
          if key[pygame.K_r]:
            self.attack_type = 1
          if key[pygame.K_t]:
            self.attack_type = 2


      if self.player == 1:
        #mouvements
        if key[pygame.K_LEFT]:
          dx = -SPEED
          self.running = True
        if key[pygame.K_RIGHT]:
          dx = SPEED
          self.running = True
        #saut
        if key[pygame.K_UP] and self.jump == False:
          self.vel_y = -30
          self.jump = True
        #attaque
        if key[pygame.K_p] or key[pygame.K_m]:
          self.attack(target)
          #choix attaque
          if key[pygame.K_p]:
            self.attack_type = 1
          if key[pygame.K_m]:
            self.attack_type = 2


    #applique gravité
    self.vel_y += GRAVITY
    dy += self.vel_y

    #joueur reste sur l'ecran
    if self.rect.left + dx < 0:
      dx = -self.rect.left
    if self.rect.right + dx > screen_width:
      dx = screen_width - self.rect.right
    if self.rect.bottom + dy > screen_height - 110:
      self.vel_y = 0
      self.jump = False
      dy = screen_height - 110 - self.rect.bottom

    #assure que joueurs soient face à face
    if target.rect.centerx > self.rect.centerx:
      self.flip = False
    else:
      self.flip = True

    #applique cooldown
    if self.attack_cooldown > 0:
      self.attack_cooldown -= 1

    #update position joueur
    self.rect.x += dx
    self.rect.y += dy


  #gere updates animation
  def update(self):
    #verifie quelle action fait joueur 
    if self.health <= 0:
      self.health = 0
      self.alive = False
      self.update_action(6)#6:mort
    elif self.hit == True:
      self.update_action(5)#5:recois un coup
    elif self.attacking == True:
      if self.attack_type == 1:
        self.update_action(3)#3:attaque1
      elif self.attack_type == 2:
        self.update_action(4)#4:attaque2
    elif self.jump == True:
      self.update_action(2)#2:saut
    elif self.running == True:
      self.update_action(1)#1:cours
    else:
      self.update_action(0)#0:idle

    animation_cooldown = 50
    #update image
    self.image = self.animation_list[self.action][self.frame_index]
    #check if enough time has passed since the last update
    if pygame.time.get_ticks() - self.update_time > animation_cooldown:
      self.frame_index += 1
      self.update_time = pygame.time.get_ticks()
    #verifie si animation fini
    if self.frame_index >= len(self.animation_list[self.action]):
      #if the player is dead then end the animation
      if self.alive == False:
        self.frame_index = len(self.animation_list[self.action]) - 1
      else:
        self.frame_index = 0
        #verifie execution attaque
        if self.action == 3 or self.action == 4:
          self.attacking = False
          self.attack_cooldown = 20
        #verifie dommages
        if self.action == 5:
          self.hit = False
          #si joueur attaque, celle ci est stoppé
          self.attacking = False
          self.attack_cooldown = 20


  def attack(self, target):
    if self.attack_cooldown == 0:
      #execute attaque
      self.attacking = True
      self.attack_sound.play()
      attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
      if attacking_rect.colliderect(target.rect):
        target.health -= 10
        target.hit = True


  def update_action(self, new_action):
    #verifie si l'action est différente de la précédente
    if new_action != self.action:
      self.action = new_action
      #update les reglages de l'animation
      self.frame_index = 0
      self.update_time = pygame.time.get_ticks()

  def draw(self, surface):
    img = pygame.transform.flip(self.image, self.flip, False)
    surface.blit(img, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))
    
class Enemy(Fighter):
  def move(self, screen_width, screen_height, surface, target, round_over):
    SPEED = 5
    GRAVITY = 2
    dx = 0
    dy = 0
    self.running = False
    self.attack_type = 1
    #ne peux effectuer autres action que si il n'attaque pas
    if self.attacking == False and self.alive == True and round_over == False:
        if target.rect.x > self.rect.x:
          dx = SPEED
          self.running = True
        if target.rect.x < self.rect.x:
          dx = -SPEED
          self.running = True

        #attaque
        if pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height).colliderect(target.rect):
          target.health -= 5
          target.hit = True
          self.attacking = True
          self.attack_cooldown -= 2


    #applique gravité
    self.vel_y += GRAVITY
    dy += self.vel_y

    #joueur reste sur l'ecran
    if self.rect.left + dx < 0:
      dx = -self.rect.left
    if self.rect.right + dx > screen_width:
      dx = screen_width - self.rect.right
    if self.rect.bottom + dy > screen_height - 110:
      self.vel_y = 0
      self.jump = False
      dy = screen_height - 110 - self.rect.bottom

    #assure que joueurs soient face à face
    if target.rect.centerx > self.rect.centerx:
      self.flip = False
    else:
      self.flip = True

    #applique cooldown

    #update position joueur
    self.rect.x += dx
    self.rect.y += dy
