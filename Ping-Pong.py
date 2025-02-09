from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self,p_img,x,y,width,height,p_speed):
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
        if keys[k_w] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys[k_s] and self.rect.y<win_height-80:
            self.rect.y+=self.speed