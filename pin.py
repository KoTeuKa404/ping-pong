from pygame import*

widht=600
height=600
mw=display.set_mode((widht,height))
mw.fill((255,120,0))
class GameSprite(sprite.Sprite):
    def __init__ (self,player_image,player_x,player_y,player_speed,widht,heidht):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(widht,heidht))
        self.rect=self.image.get_rect()
        self.x=player_x
        self.y=player_y
        self.speed=player_speed
    def reset(self):
        mw.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_r(self,):
        key=key.get_pressed()
        if key[K_UP] and self.rect.y<0:
            self.rect.y-=self.speed
        if key[K_DOWN] and self.rect.y>widht-80:
            self.rect.y+=self.speed
    def update_l(self,):
        key=key.get_pressed()
        if key[K_s] and self.rect.y<0:
            self.rect.y-=self.speed
        if key[K_s] and self.rect.y>widht-80:
            self.rect.y+=self.speed


display.set_caption("пінг-понг")
clock=time.Clock()
game=True
finish=False
FPS=60
racket1=Player("racket.png",50,200,4,50,150)
racket2=Player("racket.png",350,200,4,50,150)
speed_x=3
speed_y=3
font.init()
font1=font.SysFont('Calibri',35)
lose1=font1.render("1 player LOSE",True,(180,0,0))
lose2=font1.render("2 player LOSE",True,(180,0,0))
ball = GameSprite("ball.png", 200, 200, 4, 50, 50)

while game:
    for e in event.get():
        if e.type==QUIT:
            game=False

    
    if finish!=True:
        ball.rect.x+=speed_x
        ball.rect.y+=speed_y


     
    if ball.rect.y>widhth-50 or ball.rect.y<0:
        speed_y*=-1

    if sprite.collide_rect(ball,raket1) or sprite.collide_rect(ball,raket2):
        speed_y*=-1



    
   
    if ball.rect.x<0:
        finish=True
        mw.blit(lose2,(200,200))
    if ball.rect.x>widht:
        finish=True
        mw.blit(lose1,(200,200))       
    racket1.update_r()
    racket2.update_l()
    ball.update()
    display.update()
    Clock.tick(FPS) 
