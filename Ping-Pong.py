from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self,p_img,x,y,p_speed,width,height):
        super().__init__()
        self.image=transform.scale(image.load(p_img),(width,height))
        self.speed=p_speed
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def reset(self):
        win.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys=key.get_pressed()
        if keys[K_UP] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys[K_DOWN] and self.rect.y<win_height-80:
            self.rect.y+=self.speed
    def update_l(self):
        keys=key.get_pressed()
        if keys[K_w] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys[K_s] and self.rect.y<win_height-80:
            self.rect.y+=self.speed
bg=(200,255,255)
win_width=600
win_height=500
win=display.set_mode((win_width,win_height))
win.fill(bg)
game=True
end=False
clock=time.Clock()
FPS=60
r1=Player('racket.png',30,200,4,50,150)
r2=Player('racket.png',520,200,4,50,150)
ball=GameSprite('tenis_ball.png',200,200,4,50,50)
font.init()
font=font.Font(None,35)
lose1=font.render('PLAYER 1 LOSE!',True,(180,0,0))
lose2=font.render('PLAYER 2 LOSE!',True,(180,0,0))
spd_x=3
spd_y=3
while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
    if end!=True:
        win.fill(bg)
        r1.update_l()
        r2.update_r()
        ball.rect.x+=spd_x
        ball.rect.y+=spd_y
        if sprite.collide_rect(r1,ball) or sprite.collide_rect(r2,ball):
            spd_x*=-1
            spd_y*=1
        if ball.rect.y>win_height-50 or ball.rect.y<0:
            spd_y*=-1
        if ball.rect.x<0:
            end=True
            win.blit(lose1,(200,200))
            game_over=True
        if ball.rect.x>win_width:
            end=True
            win.blit(lose2,(200,200))
            game_over=True
        r1.reset()
        r2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)