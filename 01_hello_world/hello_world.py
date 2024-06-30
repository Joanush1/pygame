import pygame

pygame.init()
BLACK = (0, 0, 0)
PURPLE = (150, 10, 100)

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ahoj svete!")
screen.fill(PURPLE)

running = True

i = 1
# cyklus udrzujici okno v chodu
while running:
    # Event
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

    i += 1
    # Update
    myfont = pygame.font.SysFont("None", 50)
    textik = myfont.render(f"Ahoj Svete!{i}", True, (250, 80, 100))

    # Render
    screen.fill((0, 0, 0))
    screen.blit(textik, (0 + i, 0 + i))

    pygame.display.update()

pygame.quit()
 