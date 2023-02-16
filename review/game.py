import pygame,sys,time

# define variable
size = (720,600)
player_x = 120
player_y = 120
speed = 60
player_size = 60

# make display
win = pygame.display.set_mode(size)
pygame.display.set_caption("movement")
back_not = pygame.image.load("back.jpg")
player_not = pygame.image.load("cat.jpg")
back = pygame.transform.scale(back_not,(720,600))


# while
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        win.blit(back,(0,0))
        player = pygame.transform.scale(player_not,(player_size,player_size))
        win.blit(player,(player_x,player_y))
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_d or event.key == pygame.K_RIGHT ) and player_x < 640 :
                player_x += speed
            if event.key == pygame.K_a and player_x != 0 or event.key == pygame.K_LEFT :
                player_x -= speed
            if event.key == pygame.K_w and player_y != 0:
                player_y -= speed
            if event.key == pygame.K_s and player_y != 540:
                player_y += speed
            # zoom - not zoom
            if event.key == pygame.K_EQUALS:
                if player_size < 600:
                    player_size += 5
            if event.key == pygame.K_MINUS:
                player_size -= 5


    pygame.display.update()