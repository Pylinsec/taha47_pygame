import pygame,sys


pygame.init()

display_x = 500
display_y = 500
size = [display_x,display_y]
display = pygame.display.set_mode(size ,pygame.RESIZABLE) # flags --> pygame.HIDDEN , pygame.SHOWN

# while
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
        #     pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        #     pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_WAIT)
        #     mouse_cursor = pygame.mouse.get_cursor()
        #     if event.button == 1:
        #         pygame.mouse.set_visible(False)
        #     if event.button == 3:
        #         pygame.mouse.set_visible(True)
        #     print(mouse_cursor)
        #     print(pygame.mouse.get_visible())
           
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     mouse_pos = pygame.mouse.get_pos()
        #     print(mouse_pos)
        #     pygame.mouse.set_pos((0,0))
        #     mouse_pos = pygame.mouse.get_pos()
        #     print(mouse_pos)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_focused()
            
            print(mouse_pos)
         

    pygame.display.update()