from pygame import *
from time import time as timerr
window = display.set_mode((700, 500))
display.set_caption('игруха')
rot = 1
room = 0
timer = 0
rom = False
rom1 = False
bul = 0
mon = 0
mon1 = 0
a = 5
mus = True
gameov = False
hpcount = 3
real_time = False
real_time1 = False
real_time2 = False
win = 0
hpup1 = 0
hpcoun = 0
end_game = 0
winka = 0
endlol = False
anim = 0
real_timea = False
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (100, 100))
        self.player_speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        global rot
        global room
        if key_pressed[K_w] and self.rect.y >= 0:
            self.rect.y -= self.player_speed
            self.image = transform.scale(image.load('player2.png'), (100, 100))
            rot = 2
        if key_pressed[K_s] and self.rect.y <= 430:
            self.rect.y += self.player_speed
            self.image = transform.scale(image.load('player.png'), (100, 100))
            rot = 1
        if key_pressed[K_d] and self.rect.x <= 600:
            self.rect.x += self.player_speed
            self.image = transform.scale(image.load('player3.png'), (100, 100))
            rot = 3
        if key_pressed[K_a] and self.rect.x >= 0:
            self.rect.x -= self.player_speed
            self.image = transform.scale(image.load('player4.png'), (100, 100))
            rot = 4
       
    def fire_up(self):
        bullet = Bullet_up('magicup.png', self.rect.centerx - 40, self.rect.centery - 90, 10)
        bullets.add(bullet)
    def fire_left(self):
        bullet = Bullet_left('magicleft.png', self.rect.centerx - 90, self.rect.centery - 50, 10)
        bullets.add(bullet)
    def fire_right(self):
        bullet = Bullet_right('magicright.png', self.rect.centerx , self.rect.centery - 50, 10)
        bullets.add(bullet)
    def fire_down(self):
        bullet = Bullet_down('magicdown.png', self.rect.centerx - 40, self.rect.centery - 20, 10)
        bullets.add(bullet)
    def attack(self):
        global swor
        swor = Sw('sword1.png', self.rect.centerx - 40, self.rect.centery - 20, 2)
        bullets.add(swor)
class Nps(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_imagea):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.image = transform.scale(image.load(player_imagea), (100, 100))
    def update(self,):
        global player_imagea
        global real_time
        global last_time
        global now_time
        global real_timea
        global last_timea
        
        if real_time == False:
            
            last_time = timerr()
            real_time = True
            self.image = transform.scale(image.load(player_imagea), (100, 100))
                
                
                
                
        if real_time == True:
            now_time = timerr()
            if now_time - last_time >= 3:
                real_time = False

        if real_timea == False:
            
            last_timea = timerr()
            real_timea = True
            self.image = transform.scale(image.load(player_image), (100, 100))
        
                
                
                
        if real_timea == True:
            now_time = timerr()
            if now_time - last_timea >= 2:
                real_timea = False



class Sw(GameSprite):
    def update(self):
        global timer
        global bul
        if rot == 1:
            self.image = transform.scale(image.load('sword1.png'), (100, 100))
            self.rect.y += self.player_speed
            if self.rect.y >= 500:
                self.kill()
                bul = 0
        if rot == 2:
            self.image = transform.scale(image.load('sword2.png'), (100, 100))
            self.rect.y -= self.player_speed
            if self.rect.y <= 0:
                self.kill()
                bul = 0
        if rot == 3:
            self.image = transform.scale(image.load('sword3.png'), (100, 100))
            self.rect.x += self.player_speed
            if self.rect.x >= 700:
                self.kill()
                bul = 0
        if rot == 4:
            self.image = transform.scale(image.load('sword4.png'), (100, 100))
            self.rect.x -= self.player_speed
            if self.rect.x <= 0:
                self.kill()
                bul = 0
class Bullet_up(GameSprite):
    def update(self):
        self.rect.y -= self.player_speed
        if self.rect.y <= 0:
            self.kill()
class Bullet_left(GameSprite):
    def update(self):
        self.rect.x -= self.player_speed
        if self.rect.y <= 0:
            self.kill()
class Bullet_right(GameSprite):
    def update(self):
        self.rect.x += self.player_speed
        if self.rect.y >= 700:
            self.kill()
class Bullet_down(GameSprite):
    def update(self):
        self.rect.y += self.player_speed
        if self.rect.y >= 500:
            self.kill()
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.y >= 500:
            self.rect.y = 0
        if self.rect.y <= 0:
            self.direction = 'left'

        if self.direction == 'right':
            self.rect.y -= self.player_speed
        if self.direction == 'left':
            self.rect.y += self.player_speed
class Enemy1(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.y >= 450:
            self.direction = 'right'
        if self.rect.y <= 0:
            self.direction = 'left'

        if self.direction == 'right':
            self.rect.y -= self.player_speed
        if self.direction == 'left':
            self.rect.y += self.player_speed
    def nps_fire(self):
        mon_bullet = Bullet_left('npc_magic.png', self.rect.centerx - 90, self.rect.centery - 50, 10)
        mon_bullets.add(mon_bullet)
            
background = transform.scale(image.load('room.webp'), (700, 500))
display.set_icon(transform.scale(image.load('player.png'), (30,30)))
sprite1 = Player('player.png', 300, 300, 4)
bullets = sprite.Group()
mon_bullets = sprite.Group()
sword1 = GameSprite('itemsw.png', 200, 200, 0)
clock = time.Clock()
nps_bleb = Nps('nps.png', 500, 300, 0, 'nps1.png')
monsters = sprite.Group()
door1 = GameSprite('door.png', 0, 200, 0)
door2 = GameSprite('door.png', 0, 200, 0)
hp1 = GameSprite('hp.png', 10, 10, 0)
hp2 = GameSprite('hp.png', 60, 10, 0)
hp3 = GameSprite('hp.png', 110, 10, 0)
hp4 = GameSprite('hp.png', 160, 10, 0)
hpup = GameSprite('hpup.png', 200, 200, 0)
end = GameSprite('flag.png', 450, 250, 0)
FPS = 60

if gameov == False:
    mixer.init()
    mixer.music.load('music.ogg')
    mixer.music.play()
    mixer.music.set_volume(0.10)

game = True
item = True
sword = False

while game:
    key_pressed = key.get_pressed()
    window.blit(background,(0, 0))
    if gameov == False and endlol == False:
        sprite1.reset()
        sprite1.update()
        if hpcount >= 1:
            hp1.reset()
            hp1.update()
            if hpcount >= 2:
                hp2.reset()
                hp2.update()
                if hpcount >= 3:
                    hp3.reset()
                    hp3.update()
                    if hpcount >= 4:
                        hp4.reset()
                        hp4.update()
                        
        if room == 0:
        
            bullets.update()
            bullets.draw(window)
            nps_bleb.update()
            nps_bleb.reset()
        
            if item == True:
                sword1.update()
                sword1.reset()
        
        
        if room == 1:
            if mon == 0:
                rom = True
            
            if rom == True:
                for i in range(a):
                    monster = Enemy('enemy.png',300,200,4)
                    monsters.add(monster)
                    mon = 1
                rom = False  

            
               
                    
            
                
            
            nps_bleb.kill()
            monsters.update()
            monsters.draw(window)
            bullets.update()
            bullets.draw(window)
            
            if win >= 5:
                if hpcoun == 0:
                    hpup.update()
                    hpup.reset()
                    if sprite.collide_rect(sprite1, hpup) and key_pressed[K_z]:
                        hpcount += 1
                        hpcoun = 1
                    

        if room == 2:
            if mon1 == 0:
                win = 0
            if mon1 == 0:
                rom1 = True
            
            if rom1 == True:
                a = 3
                for i in range(a):
                    evil_nps = Enemy1('evil_nps.png',500,100,4)
                    monsters.add(evil_nps)
                    mon1 = 1
                rom1 = False 
                winka = 1
            monsters.update()
            monsters.draw(window)
            bullets.update()
            bullets.draw(window)
            mon_bullets.update()
            mon_bullets.draw(window)
            if end_game == 1:
                end.update()
                end.reset()
            if real_time == False:
                if win < 3:
                    evil_nps.nps_fire()
                last_time = timerr()
                real_time = True
                
                
                
            if real_time == True:
                now_time = timerr()
                if now_time - last_time >= 1:
                    real_time = False
            if winka == 1:
                if win >= 3:
                    end_game = 1
    if hpcount <= 0:
        gameov = True     
    collides = sprite.groupcollide(monsters, bullets, True, True)
    
    for c in collides:
        win += 1
        if sword == True:
            bul -= 1
       
    if room == 0:
        if sprite.collide_rect(sprite1, sword1) and key_pressed[K_z]:
        
    
            item = False
            sword = True
    if real_time == False:
        if sprite.spritecollide(sprite1, monsters, False):
            last_time = timerr()
            real_time = True
            hpcount -= 1
                
                
    if real_time == True:
        now_time = timerr()
        if now_time - last_time >= 2:
            real_time = False
    if real_time1 == False:
        if sprite.spritecollide(sprite1, mon_bullets, True):
            last_time1 = timerr()
            real_time1 = True
            hpcount -= 1
                
                
    if real_time1 == True:
        now_time1 = timerr()
        if now_time1 - last_time >= 1:
            real_time1 = False
            
        
    if room == 2:
        if end_game == 1:
            if sprite.collide_rect(sprite1, end) and key_pressed[K_z]:
                background = transform.scale(image.load('1.webp'), (700, 500))
                endlol = True
    if room == 0:
        if sprite.collide_rect(sprite1, nps_bleb):
            mixer.music.load('meow.ogg')
            mixer.music.play()
            mixer.music.load('music.ogg')
            mixer.music.play()
        if sprite.collide_rect(sprite1, door1):
            room = 1
            
    if room == 1:
        if win >= 5:
            if sprite.collide_rect(sprite1, door2):
                room = 2
        
    if gameov == True:
        
        background = transform.scale(image.load('game_over.gif'), (700, 500))
        
        if mus == True:
            mixer.music.load('gameov.ogg')
            mixer.music.play()
            
            mus = False
    for ev in event.get():
        
        if ev.type == QUIT:
            game = False
        if ev.type == MOUSEBUTTONDOWN:
            if ev.button == 1:
                if sword == True:
                    if bul != 1:
                        sprite1.attack()
                        bul = 1
                        
                if sword == False:   
                    if rot == 4:
                       sprite1.fire_left()
                    if rot == 2:
                        sprite1.fire_up()
                    if rot == 3:
                        sprite1.fire_right()
                    if rot == 1:
                        sprite1.fire_down()
    display.update()
    clock.tick(FPS)