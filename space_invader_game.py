import math
import random
import pygame

SCREEN_WIDTH=800
SCREEN_HEIGHT=500
PLAYER_START_X=370
PLAYER_START_Y=380
ENEMY_START_Y_MIN=50
ENEMY_START_Y_MAX=150
ENEMY_SPEED_X=4
ENEMY_SPEED_Y=40
BULLET_SPEED_Y=10
COLLISION_DISTANCE=27
PLAYER_COLLISION_DISTANCE=45
START_LIVES=3

pygame.init()

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

background=pygame.image.load('space_bg.jpg')
background=pygame.transform.scale(background,(SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption("Space Invader")
icon=pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

playerImg=pygame.image.load('player.png')
playerImg=pygame.transform.scale(playerImg,(64,64))
playerX=PLAYER_START_X
playerY=PLAYER_START_Y
playerX_change=0

enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=7

for i in range(num_of_enemies):
    if i==0:
        img=pygame.image.load('asteroid.jpg')
    else:
        img=pygame.image.load('enemy.png')
    img=pygame.transform.scale(img,(40,40))
    enemyImg.append(img)
    enemyX.append(random.randint(0,SCREEN_WIDTH-64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

bulletimg=pygame.image.load('bullet.png')
bulletimg=pygame.transform.scale(bulletimg,(64,64))
bulletX=0
bulletY=PLAYER_START_Y
bulletY_change=BULLET_SPEED_Y
bullet_state="ready"

score_value=0
lives=START_LIVES
level=1
high_score=0
game_over=False
paused=False

font=pygame.font.Font('freesansbold.ttf',28)
over_font=pygame.font.Font('freesansbold.ttf',64)

def show_text(text,x,y,big=False):
    if big:
        words=over_font.render(text,True,(255,255,255))
    else:
        words=font.render(text,True,(255,255,255))
    screen.blit(words,(x,y))

def show_info():
    show_text("Score: "+str(score_value),10,10)
    show_text("Level: "+str(level),10,45)
    show_text("Lives: "+str(lives),SCREEN_WIDTH-140,10)
    show_text("Best: "+str(high_score),SCREEN_WIDTH-140,45)

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletimg,(x+16,y+16))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt((enemyX-bulletX) ** 2 + (enemyY-bulletY) ** 2)
    return distance < COLLISION_DISTANCE

def isPlayerCollision(enemyX,enemyY,playerX,playerY):
    distance=math.sqrt((enemyX-playerX) ** 2 + (enemyY-playerY) ** 2)
    return distance < PLAYER_COLLISION_DISTANCE

def respawn_enemy(i):
    enemyX[i]=random.randint(0,SCREEN_WIDTH-64)
    enemyY[i]=random.randint(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX)

def restart_game():
    global score_value,lives,level,game_over,bullet_state,bulletY,playerX
    score_value=0
    lives=START_LIVES
    level=1
    game_over=False
    bullet_state="ready"
    bulletY=PLAYER_START_Y
    playerX=PLAYER_START_X
    for i in range(num_of_enemies):
        respawn_enemy(i)

clock=pygame.time.Clock()

running=True
while running:
    clock.tick(60)
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-6
            if event.key==pygame.K_RIGHT:
                playerX_change=6
            if event.key==pygame.K_SPACE and bullet_state=="ready" and not game_over and not paused:
                bulletX=playerX
                bulletY=PLAYER_START_Y
                fire_bullet(bulletX,bulletY)
            if event.key==pygame.K_p and not game_over:
                paused=not paused
            if event.key==pygame.K_r and game_over:
                restart_game()
        if event.type==pygame.KEYUP and event.key in [pygame.K_LEFT,pygame.K_RIGHT]:
            playerX_change=0

    if not game_over and not paused:
        playerX+=playerX_change
        playerX=max(0,min(playerX,SCREEN_WIDTH-64))

        level=score_value//10+1
        speed_boost=1+(level-1)*0.2

        for i in range(num_of_enemies):
            enemyX[i]+=enemyX_change[i]*speed_boost
            if enemyX[i]<=0:
                enemyX_change[i]=abs(enemyX_change[i])
                enemyY[i]+=enemyY_change[i]
            elif enemyX[i]>=SCREEN_WIDTH-64:
                enemyX_change[i]=-abs(enemyX_change[i])
                enemyY[i]+=enemyY_change[i]

            if isCollision(enemyX[i],enemyY[i],bulletX,bulletY) and bullet_state=="fire":
                bulletY=PLAYER_START_Y
                bullet_state="ready"
                score_value+=1
                respawn_enemy(i)

            if isPlayerCollision(enemyX[i],enemyY[i],playerX,playerY):
                lives-=1
                respawn_enemy(i)

            if enemyY[i]>340:
                lives-=1
                respawn_enemy(i)

        if bulletY<=0:
            bulletY=PLAYER_START_Y
            bullet_state="ready"
        elif bullet_state=="fire":
            bulletY-=bulletY_change

        if lives<=0:
            lives=0
            game_over=True
            high_score=max(high_score,score_value)

    for i in range(num_of_enemies):
        enemy(enemyX[i],enemyY[i],i)

    if bullet_state=="fire":
        fire_bullet(bulletX,bulletY)

    if not game_over:
        player(playerX,playerY)

    show_info()

    if paused:
        show_text("PAUSED",270,220,True)

    if game_over:
        show_text("GAME OVER",200,200,True)
        show_text("Press R to restart",270,280)

    pygame.display.update()

pygame.quit()