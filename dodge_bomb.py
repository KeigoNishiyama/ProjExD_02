import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1200, 675

delta = {
pg.K_UP: (0, -5),
pg.K_DOWN: (0, +5),
pg.K_LEFT: (-5, 0),
pg.K_RIGHT: (+5, 0),
}



def check_bound(obj_rct: pg.Rect):
    yoko, tate = True, True
    if obj_rct.left < 0 or WIDTH < obj_rct.right:
        yoko = False
    if obj_rct.top < 0 or HEIGHT < obj_rct.bottom:
        tate = False
    return yoko, tate

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    """こうかとん"""
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = (675, 300)
    """ばくだん"""
    bd_img = pg.Surface((20, 20))
    bd_img.set_colorkey((0, 0, 0))
    pg.draw.circle(bd_img, (255, 0, 0), (10, 10), 10)
    bd_rct = bd_img.get_rect()
    x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    bd_rct.center = (x, y)
    vx, vy = +5, +5

    clock = pg.time.Clock()
    tmr = 0
    kk_img_2 = pg.transform.flip(kk_img, True, False) #こうかとんの画像を左右反転したものをつくる
    dire = {                                    #direという画像の辞書を作成する  
    pg.K_UP: pg.transform.rotate(kk_img_2, 90), #上キーを押したとき、反転した画像を反時計回りに90度回転させる
    pg.K_DOWN: pg.transform.rotate(kk_img_2, -90), #下キーを押したとき、反転した画像を時計回りに90度回転させる
    pg.K_LEFT: pg.transform.rotate(kk_img, 0), #左キーを押したとき、元の画像を表示させる
    pg.K_RIGHT: pg.transform.flip(kk_img, True, False), #右キーを押したとき、元の画像を左右反転させる
    }
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        if kk_rct.colliderect(bd_rct):
            print("ゲームオーバー")
            return
        screen.blit(bg_img, [0, 0])

        """こうかとん"""
        key_lst = pg.key.get_pressed()
        sum_mv = [0,0]
        for key, pc in dire.items(): #pcという変数を作成し、上下左右キーが押されたときにdireの辞書を呼び出す
            if key_lst[key]:
                kk_img = pc
        for key, mv in delta.items():
            if key_lst[key]:
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
        kk_rct.move_ip(sum_mv[0], sum_mv[1])
        if check_bound(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
        screen.blit(kk_img, kk_rct)
        """ばくだん"""
        bd_rct.move_ip(vx, vy)
        yoko, tate = check_bound(bd_rct)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        screen.blit(bd_img, bd_rct)

        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()