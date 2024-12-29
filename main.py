# Hauptfunktion für das Spiel PONG
import sys
from screen import *
from ball import *
from racket import *

# pygame setup
pygame.init()

# Spielobjekte initialisieren
racket_left = Racket(20, 300)
racket_right = Racket(1260, 300)
ball = Ball(racket_left, racket_right)

# Einstellungen
clock = pygame.time.Clock()
running = True
game_over_message = None  # Spielstatus

while running:
    # Ereignisse und Tasten abfragen
    events = pygame.event.get()
    keys = pygame.key.get_pressed()

    # Ereignisbehandlung
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and game_over_message:
                # Spiel zurücksetzen
                ball.reset(racket_left, racket_right)  # Ball zurücksetzen
                racket_left.y = 300  # Linker Schläger zurücksetzen
                racket_right.y = 300  # Rechter Schläger zurücksetzen
                game_over_message = None  # Spielstatus zurücksetzen

    # Wenn das Spiel läuft und kein Game Over ist
    if not game_over_message:
        # Ball bewegen und auf Spielverlust prüfen
        result = ball.move_ball()
        if result == "left":
            game_over_message = "Rechte Seite gewinnt!"
        elif result == "right":
            game_over_message = "Linke Seite gewinnt!"

        # Schläger bewegen
        racket_left.move(keys, events, 'left')
        racket_right.move(keys, events, 'right')

    # Bildschirm aktualisieren
    screen.fill("black")  # Bildschirm leeren
    playing_field()       # Spielfeld zeichnen
    net()                 # Netz zeichnen
    middle_line()         # Mittellinie zeichnen
    t_linie()             # Top-Linie zeichnen

    # Schläger und Ball zeichnen
    racket_left.draw(screen)
    racket_right.draw(screen)
    ball.draw(screen)

    # Game Over Nachricht anzeigen, falls vorhanden
    if game_over_message:
        draw_game_over_message(screen, game_over_message)

    # Bildschirm aktualisieren
    pygame.display.flip()
    clock.tick(60)  # FPS limitieren