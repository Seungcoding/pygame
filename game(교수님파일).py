import pygame

pygame.init()
display = pygame.display.set_mode((800, 600))
myfont = pygame.font.SysFont('Comic Sans MS', 30)
score = 0

player=pygame.image.load("spaceship.png")
playerX, playerY, playerDx , playerDy = 400, 550, 0, 0

alien=pygame.image.load("alien.png")
#alienX, alienY, alienDx , alienDy   = 0, 10, 0.1, 0.1
alienX = [ ]
alienY = [ ]
alienDx = [ ]
alienDy = [ ]
alienNumber = 6

for i in range(alienNumber):
    alienX.append(20+i*60)
    alienY.append(10)
    alienDx.append(0.1)
    alienDy.append(0.0)

missile = pygame.image.load('missile.png')
missileX, missileY, missileDx , missileDy = 0, 1000, 0, 0.1

missileState = "hidden"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
'''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: playerDx = -0.1
            if event.key == pygame.K_RIGHT: playerDx = 0.1
            if event.key == pygame.K_SPACE:
                if missileState == "hidden":
                    missileState = "fire"
                    missileX, missileY = playerX, playerY
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerDx = 0
    playerX += playerDx
    '''
# Serial input check(키입력 대체) 7주차 실습활동으로 진행함.
    if ser.isOpen():
        bytesToRead = ser.inWaiting()
        for i in range(bytesToRead):
            b = ser.read(1)
            print(b)
            if b == b'L':
                playerX -= 1
                playerDx = -0.1
            elif b == b'R':
                playerX += 1
                playerDx = 0.1
            elif b == b'C':
                if missileState == "hidden":
                    missileState == "fire"
                    missileX, missileY = playerX, playerY
            elif b == b'N':
                playerDx = 0
    playerX += playerDx
#7주차 추가한 코드 여기까지임
    """    
    alienX += alienDx
    if alienX <= 0 or alienX > 750:
        alienDx *= -1
        alienY += 30
    """
    if missileY <= 0:
        missileY = 1000
        missileState = "hidden"
    if missileState == "fire":
        missileY -= missileDy
        """
        rect1 = pygame.Rect(alien.get_rect(topleft=(alienX, alienY)))
        rect2 = pygame.Rect(missile.get_rect(topleft=(missileX, missileY)))
        if rect1.colliderect(rect2) and missileState != "hidden":
            score += 1
            alienX, alienY, alienDx, alienDy = 0, 10, 0.1, 0.1
        """
    display.fill((0, 0, 0))
    for i in range(alienNumber):
        alienX[i] += alienDx[i]
        alienY[i] += alienDy[i]
        if alienX[i] <= 0 or alienX[i] > 750:
            alienDx[i] *= -1
            alienY[i] += 30
        rect1 = pygame.Rect(alien.get_rect(topleft=(alienX[i], alienY[i])))
        rect2 = pygame.Rect(missile.get_rect(topleft=(missileX, missileY)))
        if rect1.colliderect(rect2) and missileState != "hidden":
            score += 1
            alienX[i], alienY[i], alienDx[i] , alienDy[i] = 0, 1000, 0.1, 0.0
        display.blit(alien, (alienX[i], alienY[i]))
        
    display.blit(player, (playerX, playerY))
    #display.blit(alien, (alienX, alienY))
    display.blit(missile, (missileX, missileY))
    text = myfont.render(f'score={score}', False, (255, 255, 255))
    display.blit(text,(10,550))
    pygame.display.update()

pygame.quit()
