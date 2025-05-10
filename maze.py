from pygame import *
ww = 1000
wh = 600
x1 = 200
y1 = 200
x2, y2 = 400,400
speed = 5


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < ww - 80:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < wh - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= ww - 85:
            self.direction = "left"
        
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color, height, width, x, y):
        self.image = Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y1
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

wall_1 = Wall((50, 205, 50), 10, 200, 200, 5)
wall_2 = Wall((50, 205, 50), 25, 100, 30, 500)
wall_3 = Wall((50, 205, 50), 19, 669, 80, 100)

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
window = display.set_mode((ww, wh))
display.set_caption('Догонялки')
sprite1 = Player("hero.png", 0, 0, 5)
sprite2 = Enemy("cyborg.png", 0, 0, 5)
gold = GameSprite('treasure.png', ww - 100, wh - 100, 10)
background = transform.scale(image.load("background.jpg"), (ww, wh))
is_running = True


clock = time.Clock()
FPS = 60



while is_running:
    for e in event.get():
        if e.type == QUIT:
            is_running = False
    window.blit(background, (0, 0))
    sprite1.draw()
    sprite2.draw()
    gold.draw()
    wall_1.draw_wall()
    wall_2.draw_wall()
    wall_3.draw_wall()
    sprite2.update()
    sprite1.update()
    display.update()
    clock.tick(FPS)

