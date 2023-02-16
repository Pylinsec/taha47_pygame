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
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            left , wheel , right = pygame.mouse.get_pressed()
            print(left,wheel,right)
            
        #     if event.button == 1:
        #         print('left click pressed') 
        #     if event.button == 2:
        #         print('wheel click pressed') 
        #     if event.button == 3:
        #         print('right click pressed') 
        #     if event.button == 4:
        #         print('wheel up') 
        #     if event.button == 5:
        #         print('wheel down ') 

        # if event.type == pygame.MOUSEBUTTONUP: # shabih bala 
        # if event.type == pygame.MOUSEWHEEL: # y=1 --> charkhesh be samt bala  , agar y = -1 --. charkhesh be samt paein
        

    pygame.display.update()