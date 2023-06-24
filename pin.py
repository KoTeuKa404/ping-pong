from pygame import*
widht=600
height=600

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