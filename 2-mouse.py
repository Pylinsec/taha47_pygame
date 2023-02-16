            
import pygame,sys

pygame.init()

display_x = 500
display_y = 500
size = [display_x,display_y]
display = pygame.display.set_mode(size)

# while
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEMOTION:
            mouse_re = pygame.mouse.get_rel() # mizan jabejaye mouse 
            mouse_pos = pygame.mouse.get_pos() # mokhtasat feli mouse 
            print(mouse_pos)
            # mouse = pygame.mouse.get_pressed()
            # tuple( True, False, True)
            # if mouse[0]:
            #     print('left mouse key is being pressed')
            # if mouse[1]:
            #     print('wheeel mouse key is being pressed')
            # if mouse[2]:
            #     print('right mouse key is being pressed')

        # if event.type == pygame.MOUSEBUTTONUP: # shabih bala 
        # if event.type == pygame.MOUSEWHEEL: # y=1 --> charkhesh be samt bala  , agar y = -1 --. charkhesh be samt paein
        

    pygame.display.update()