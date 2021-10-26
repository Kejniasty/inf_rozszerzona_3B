import pygame as pg
pg.init()

win = pg.display.set_mode((500, 540))
pg.display.set_caption("Yeet")

x = 0
y = 40
szerokosc = 20
wysokosc = 20
krok = 20
run = True

#anty-zamykanie programu
while run:
    pg.time.delay(50)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

keys = pg.key.get_pressed()
if keys[pg.K_LEFT]:
    x -= krok
if keys[pg.K_RIGHT]:
    x += krok
if keys[pg.K_UP]:
    y -= krok
if keys[pg.K_DOWN]:
    y += krok

win.fill((0, 0, 0))
pg.draw.rect(win, (0, 255, 0), (x, y, szerokosc, wysokosc))
pg.display.update()
