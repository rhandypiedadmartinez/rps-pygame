import pygame
from pygame.display import (
    set_caption, 
    set_icon,
    set_mode
)
from pygame.surface import Surface
from pygame.sprite import Sprite
from pygame.image import load
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,

    K_w,
    K_a,
    K_s,
    K_d,

    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Player(Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = Surface((50, 50))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()
        # self.rect.move_ip(177, 400)
        

    def update_player1(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -3)

        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 3)

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-3, 0)

        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(3, 0)

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

        if self.rect.left < 0:
            self.rect.left = 0

    def update_player2(self, pressed_keys):

        if pressed_keys[K_w]:
            self.rect.move_ip(0, -3)

        if pressed_keys[K_s]:
            self.rect.move_ip(0, 3)

        if pressed_keys[K_a]:
            self.rect.move_ip(-3, 0)

        if pressed_keys[K_d]:
            self.rect.move_ip(3, 0)

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Ground(Sprite):
    def __init__(self):
        super(Ground, self).__init__()
        self.surf = Surface((600, 100))
        self.surf.fill((200, 0, 0))
        self.rect = self.surf.get_rect(center=((400),(500)))

icon = load('./assets/icon.png')

pygame.init()

# Window/Screen
screen = set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
set_caption("rock paper scissors")
set_icon(icon)

player1 = Player()
player2 = Player()
ground1 = Ground()

player1.rect.move_ip(177, 400)
player2.rect.move_ip(599, 400)

running = True

while running:
    # for loop through the event queue
    for event in pygame.event.get():

        # Check for KEYDOWN event
        if event.type == KEYDOWN:

            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False

        # Check for QUIT event. If QUIT, then set running to false.

        elif event.type == QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()

    player1.update_player1(pressed_keys)
    player2.update_player2(pressed_keys)

    screen.fill((255, 255, 255))

    # Fighting ground
    screen.blit(ground1.surf, ground1.rect)

    if pygame.sprite.collide_rect(player1, ground1):

# this code below effectively stops player colliding to the left and right of fighting ground
#        if player1.rect.right >= ground1.rect.right:
 #           player1.rect.left = ground1.rect.right
 #       if player1.rect.left <= ground1.rect.left:
  #          player1.rect.right = ground1.rect.left

 #       This code below is working to stop player from falling but has problems at left and right side
        if player1.rect.bottom >= ground1.rect.top:
            player1.rect.bottom = ground1.rect.top

    if pygame.sprite.collide_rect(player2, ground1):

# this code below effectively stops player colliding to the left and right of fighting ground
#        if player1.rect.right >= ground1.rect.right:
 #           player1.rect.left = ground1.rect.right
 #       if player1.rect.left <= ground1.rect.left:
  #          player1.rect.right = ground1.rect.left

 #       This code below is working to stop player from falling but has problems at left and right side
        if player2.rect.bottom >= ground1.rect.top:
            player2.rect.bottom = ground1.rect.top

    if pygame.sprite.collide_rect(player2, player1):
        print('players collided')
        break

# <rect(177, 400, 50, 50)>
# <rect(594, 400, 50, 50)>    

    screen.blit(player1.surf, player1.rect)
    screen.blit(player2.surf, player2.rect)

    # print(player2.rect)
    # print(player1.rect)
    pygame.display.flip()

pygame.quit()