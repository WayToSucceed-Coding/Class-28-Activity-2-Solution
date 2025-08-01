import pygame

pygame.init()

WIDTH, HEIGHT = 600,600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("My Pygame Window")

class Circle():

    def __init__(self, x, y, color, radius):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius

    def __repr__(self):
        return f"Circle(x={self.x}, y={self.y}, color={self.color}, radius={self.radius})"
    
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += 0.2

circles = [
    Circle(100, 200, (255, 0, 0), 20),
    Circle(200, 300, (0, 255, 0), 30),
    Circle(300, 150, (0, 0, 255), 10)
]

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 204, 153))

    for circle in circles:
        circle.move()
        circle.draw()
    
    pygame.draw.rect(screen, (255, 0, 0), (260, 330, 80, 40))

    pygame.display.update()

pygame.quit()



