from pygame import*

window = display.set_mode((1000,600))
display.set_caption("Tower defens")

enemy_img = "rocket1.jpg"
class Game(sprite.Sprite):
    def __init__(self, player_img, px, py, size_x, size_y,):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_img),(size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py

class Enemy(sprite.Sprite):
    def __init(self, enemy_img, ex, ey, size_x, size_y, enemy_speed, enemy_hp):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(enemy_img),(size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = ex
        self.rect.y = ey
        self.speed = enemy_speed
        self.hit_point = enemy_hp
class Bullet(sprite.Sprite):
    def __init(self, bullet_img, bx, by, size_x, size_y, bullet_speed, damage):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(bullet_img),(size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = bx
        self.rect.y = by
        self.speed = bullet_speed
        self.damage = damage


enemy_goblin = Enemy(enemy_img, 5, 400, 80, 100, 1, 10)        
fortres_hp = 5
#while fortres_hp == 0:

finish = False
run = True
while run :
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        enemy_goblin.reset()
        enemy_goblin.update()
        display.update()

display.update()
time.delay(50)