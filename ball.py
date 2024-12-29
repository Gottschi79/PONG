
import pygame
from screen import screen
from racket import Racket


'''Bewegungsfeld für Ball in Pixel von x=5 - x= 1275, y = 100 - Y = 600'''
'''Kollidiert der Ball in Y, gilt "Einfallswinkel=Ausfallswinkel" '''
''' Schlägt der Schläger den Ball, gilt "Einfallswinkel=Ausfallswinkel". Wird der Schläger im Moment der Kollision bewegt, 
so wird der Ball abhängig von der Bewegungsrichtung und Geschwindigkeit des Schlägers abgelenkt.'''

RADIUS_BALL = 10
BALL_SPEED = 5
racket_length = 80


class Ball:
    def __init__(self, left_racket, right_racket):
        self.pos_x = 640
        self.pos_y = 150
        self.direction_x = 1  # Bewegungsrichtung: 1 = rechts, -1 = links
        self.direction_y = 1  # Bewegungsrichtung: 1 = runter, -1 = hoch
        self.speed = BALL_SPEED
        self.left_racket = left_racket
        self.right_racket = right_racket

    def move_ball(self):
        """Bewegt den Ball und behandelt Kollisionen."""

        # Kollisionsprüfung für die Seitenränder (Spiel verloren wenn der Ball die X-Grenzen überschreitet)
        if self.pos_x <= 0:
            # Der Ball ist am linken Rand
            return "left"  # Spiel verloren für die linke Seite

        if self.pos_x >= 1280 - RADIUS_BALL:
            # Der Ball ist am rechten Rand
            return "right"  # Spiel verloren für die rechte Seite

        # Kollisionsprüfung für den linken Schläger
        if (
            self.pos_x <= self.left_racket.x + RADIUS_BALL and
            self.pos_y <= self.left_racket.y + racket_length
        ):
            self.direction_x *= -1  # Richtung umkehren

        # Kollisionsprüfung für den rechten Schläger
        if (
            self.right_racket.x - RADIUS_BALL <= self.pos_x and
            self.pos_y <= self.right_racket.y + racket_length
        ):
            self.direction_x *= -1  # Richtung umkehren

        # Kollisionsprüfung für obere und untere Ränder
        if self.pos_y <= 100 + RADIUS_BALL or self.pos_y >= 700 - RADIUS_BALL:
            self.direction_y *= -1  # Richtung umkehren

        # Ballposition aktualisieren
        self.pos_x += self.direction_x * self.speed
        self.pos_y += self.direction_y * self.speed

        return None  # Spiel geht weiter

    def reset(self, left_racket, right_racket):
        """Setze den Ball zurück auf die Startposition."""
        self.pos_x = 640
        self.pos_y = 150
        self.direction_x = 1  # Bewegungsrichtung: 1 = rechts, -1 = links
        self.direction_y = 1  # Bewegungsrichtung: 1 = runter, -1 = hoch
        self.speed = BALL_SPEED
        self.left_racket = left_racket
        self.right_racket = right_racket

    def draw(self, screen):
        """Zeichne den Schläger auf den Bildschirm."""
        pygame.draw.circle(screen,'yellow',[self.pos_x, self.pos_y], RADIUS_BALL)




