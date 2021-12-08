import pygame
import random
import sys


## 함수 선언 부분 ##
# @기능 2-5 : 매개변수로 받은 객체를 화면에 그리는 함수를 선언한다.
def paintEntity(entity, x, y) : 
   monitor.blit(entity, (int(x), int(y)))

# @기능 5-4 : 점수를 화면에 쓰는 함수를 선언한다. <== 12~15행 
def writeScore(score) :
    myfont = pygame.font.Font('D:/CODES/last_ex/NanumGothic.ttf', 20)      # 한글 폰트
    txt = myfont.render('점수 : ' + str(score), True, (255-r, 255-g, 255-b))
    monitor.blit(txt, (10, sheight - 40))

#12.05 추가
def LifeScore(score) :
    myfont = pygame.font.Font('D:/CODES/last_ex/NanumGothic.ttf', 20)      # 한글 폰트
    txt = myfont.render('생명 : ' + str(score), True, (255-r, 255-g, 255-b))
    monitor.blit(txt, (90, sheight - 40))   

''' # (12.05 추가)
def refreshDescription() :
    myfont = pygame.font.Font('D:/CODES/last_ex/NanumGothic.ttf', 20)      # 한글 폰트
    txt = myfont.render('게임 시작은 S , 재시작은 R 키를 누르시오')
    monitor.blit(txt, (150, sheight-0))
'''

def playGame() :
    global monitor, ship, monster, missile, shipSize

    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256) 
    
     # @기능 2-2 : 우주선의 초기 위치 키보드를 눌렀을 때 이동량을 저장할 변수를 선언한다.
    shipX = swidth / 2  # 우주선 위치
    shipY = sheight * 0.8
    dx, dy = 0, 0  # 키보드를 누를때 우주선의 이동량
    
    # @기능 3-2 : 우주괴물을 랜덤하게 추출하고 크기와 위치를 설정한다.
    monster = pygame.image.load(random.choice(monsterImage))
    monsterSize = monster.get_rect().size                 # 우주괴물 크기
    monsterX = random.randrange(30, 470) #양쪽 30씩 비워줬음 (12.05 추가)
    monsterY = 0 # 상위 30% 위치까지만 >> 위에서 젠되도록 설정함 (12.05 추가)
    monsterSpeed = random.randrange(1, 8)

    # @기능 4-2 : 미사일 좌표를 초기화한다.
    missileX, missileY = None, None  # None은 미사일을 쏘지 않았다는 의미이다.

    # @기능 5-1 : 맞힌 우주괴물 숫자를 저장할 변수를 선언한다. <== 40행 
    fireCount = 0
    LifePoint = 2 # (12.05 추가) 

    # 무한 반복
    while True :
        (pygame.time.Clock()).tick(50)  # 게임 진행을 늦춘다(10~100 정도가 적당).
        monitor.fill((r, g, b))              # 화면 배경을 칠한다.

        # 키보드나 마우스 이벤트가 들어오는지 체크한다.
        for e in pygame.event.get() :
            if e.type in [pygame.QUIT]  :
                pygame.quit()
                sys.exit()

            # @기능 2-3 : 방향키에 따라 우주선이 움직이게 한다.
            # 방향키를 누르면 우주선이 이동한다(누르고 있으면 계속 이동). 
            if e.type in [pygame.KEYDOWN] :
                if e.key == pygame.K_LEFT : dx = -10
                elif e.key == pygame.K_RIGHT : dx = +10
                elif e.key == pygame.K_UP : dy = -10
                elif e.key == pygame.K_DOWN : dy = +10
                
                # @기능 4-3 : 스페이스바를 누르면 미사일을 발사한다.
                elif e.key == pygame.K_SPACE : 
                    if missileX == None :                     # 미사일을 쏜 적이 없다면
                        missileX = shipX + shipSize[0]/2    # 우주선 위치에서 미사일을 발사한다.
                        missileY = shipY

            # 방향키를 떼면 우주선이 멈춘다.
            if e.type in [pygame.KEYUP] :
                 if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT \
                    or e.key == pygame.K_UP or e.key == pygame.K_DOWN : dx, dy = 0, 0

        # @기능 2-4 : 우주선이 화면 안에서만 움직이게 한다.
        if (0 < shipX+dx and shipX+dx <= swidth-shipSize[0]) \
            and (sheight/2 < shipY+dy and shipY+dy <= sheight - shipSize[1]) :  # 화면의 중앙까지만
            shipX += dx
            shipY += dy
            
        paintEntity(ship, shipX, shipY)   # 우주선을 화면에 표시한다.

        # @기능 3-3 : 우주괴물이 자동으로 나타나 왼쪽에서 오른쪽으로 움직인다. (12.05 추가)
        monsterY += monsterSpeed
        if monsterY > sheight :
            monsterY = 0
            monsterX = random.randrange(30, 470)
            
            # 우주괴물 이미지를 무작위로 선택한다.
            monster = pygame.image.load(random.choice(monsterImage))
            monsterSize = monster.get_rect().size
            monsterSpeed = random.randrange(1, 8)

            LifePoint-=1 #추가 (12.05 추가)
           
        paintEntity(monster, monsterX, monsterY)
        
        # @기능 4-4 : 미사일을 화면에 표시한다.
        if missileX != None :                          # 총알을 쏘면 좌표를 위로 변경한다.
            missileY -= 15
            if missileY < 0 :
                  missileX, missileY= None, None   # 총알이 사라진다.
                  
        if missileX != None :           # 미사일을 쏜 적이 있으면 미사일을 그려준다.
            paintEntity(missile, missileX, missileY)
            
            # @기능 5-2 : 우주괴물이 미사일에 맞았는지 체크한다. <== 101 ~ 114행 
            if (monsterX < missileX and missileX < monsterX + monsterSize[0]) and \
                   (monsterY < missileY and missileY < monsterY + monsterSize[1]) :
                fireCount += 1

                # 우주괴물을 초기화(무작위 이미지로 다시 준비) >> (12.6 추가)
                monster = pygame.image.load(random.choice(monsterImage))
                monsterSize = monster.get_rect().size
                monsterX = random.randrange(30, 470)
                monsterY = 0
                monsterSpeed = random.randrange(1, 8)

                # (12.6 추가)
                ship = pygame.image.load(random.choice(ship_Image))
                shipSize = ship.get_rect().size
                
                # 미사일을 초기화한다.
                missileX, missileY= None, None   # 총알이 사라진다.

        # @기능 5-3 : 점수를 화면에 쓰는 함수를 호출한다. <== 117행 
        writeScore(fireCount)
        LifeScore(LifePoint) # (12.05 추가)
        
        # 화면을 업데이트한다.
        pygame.display.update()

        
## 전역 변수 선언 부분 ##
r, g, b = [0] * 3                # 게임 배경색
swidth, sheight = 500, 700  # 화면 크기
monitor = None               # 게임 화면
ship, shipSize = None, 0     # 우주선의 객체와 크기 변수

# @기능 3-1 : 랜덤하게 사용할 우주괴물의 이미지 10개를 준비한다.
monsterImage = ['D:/CODES/last_ex/monster01.png', 'D:/CODES/last_ex/monster02.png', 'D:/CODES/last_ex/monster03.png', \
                'D:/CODES/last_ex/monster04.png', 'D:/CODES/last_ex/monster05.png', 'D:/CODES/last_ex/monster06.png', \
                'D:/CODES/last_ex/monster07.png', 'D:/CODES/last_ex/monster08.png', 'D:/CODES/last_ex/monster09.png', \
                'D:/CODES/last_ex/monster10.png']
monster = None   # 우주괴물
ship_Image = ['D:/CODES/last_ex/ship01.png', 'D:/CODES/last_ex/ship02.png', 'D:/CODES/last_ex/ship03.png', \
                'D:/CODES/last_ex/ship04.png']

missile = None     # 미사일
# @기능 4-1 : 미사일 이미지를 추가한다.
missile = pygame.image.load('D:/CODES/last_ex/missile.png')

# @기능 2-1 : 우주선 이미지를 준비하고 크기를 구한다.
ship = pygame.image.load(random.choice(ship_Image))
shipSize = ship.get_rect().size
## 메인 코드 부분 ##
pygame.init()
monitor = pygame.display.set_mode((swidth, sheight))
pygame.display.set_caption('우주괴물 무찌르기') 
  
playGame()