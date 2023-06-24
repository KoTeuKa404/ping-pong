from pygame import*
widht=600
height=600
class GameSprite(sprite.Sprite):
    def __init_(self,player_image,player_x,player_y,player_speed,widht,heidht):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(widht,heidht))
        self.rect=self.image.get_rect()
        self.x=player_x
        self.y=player_y
        self.speed=player_speed
    def reset(self):
        mw.blit(self.image,(self.rect.x,self.rect.y))


mw=display.set_mode((widht,height))
mw.fill((255,120,0))
display.set_caption("пінг-понг")
clock=time.Clock()
game=True
finish=False
FPS=60

while game:
    for e in event.get():
        if e.type==QUIT:
            game=False


    display.update()
    clock.tick(FPS) 
