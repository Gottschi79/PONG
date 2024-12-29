import pygame

WIN_SIZE_X = 1280
WIN_SIZE_Y = 800

screen = pygame.display.set_mode((WIN_SIZE_X, WIN_SIZE_Y))

def playing_field():
    pygame.draw.rect(screen, "green", (0, 100, 1280, 600))

def net(): #Border between fields
    pygame.draw.line(screen, 'white', [640,100],[640,700],5)

def middle_line():
    pygame.draw.line(screen, 'white', [320, 400], [960, 400], 5)

def t_linie():
    pygame.draw.line(screen, 'white', [320, 100], [320, 700], 5)
    pygame.draw.line(screen, 'white', [960, 100], [960, 700], 5)

def draw_game_over_message(screen, message):
    """Zeichne die 'Game Over' Nachricht in der Mitte des Bildschirms."""
    font = pygame.font.Font(None, 74)  # Schriftgröße 74
    text = font.render(message, True, (255, 0, 0))  # Rote Farbe für die Nachricht
    text_rect = text.get_rect(center=(640, 350))  # Position der Nachricht in der Mitte
    screen.blit(text, text_rect)
