import pygame, sys
import time
pygame.font.init()
pygame.mixer.init()
clock = pygame.time.Clock()

WIDTH = 900
HEIGHT = 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("iCoach")
PITCH = pygame.transform.scale(pygame.image.load('C://Users/alexl/Documents/Coding/Python/COME ON ENGERLAND!/Assets/pitch.jpg'),(WIDTH,HEIGHT))
ENGERLAND_SOUND = pygame.mixer.Sound('C://Users/alexl/Documents/Coding/Python/COME ON ENGERLAND!/Assets/CAM ON INGERLAND.mp3')

WHITE = (255,255,255)
RED = (255,0,0)
FPS = 60

SCORE_FONT = pygame.font.SysFont('comicsans', 150)
NAME_FONT = pygame.font.SysFont('comicsans', 70)
COUNTDOWN_FONT = pygame.font.SysFont('comicsans', 200)



def sound_check(leftScore,rightScore):
    if leftScore%50 == 0 and leftScore!=0 and leftScore%100 !=0:
        output = True
    elif rightScore%100 == 0 and rightScore!= 0:
        output = True
    else:
        output = False
    
    return output


def start_count():
    current_time = 0
    startTime = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        

        current_time = pygame.time.get_ticks()

        if current_time - startTime < 1000:
            WIN.blit(PITCH, (0,0))
            timerText = COUNTDOWN_FONT.render(str(3), False, WHITE)
            tLength = timerText.get_width()
            tHeight = timerText.get_height()
            WIN.blit(timerText, (WIDTH/2 - tLength/2, HEIGHT/2 - tHeight/2))

        elif current_time - startTime < 2000:
            WIN.blit(PITCH, (0,0))
            timerText = COUNTDOWN_FONT.render(str(2), False, WHITE)
            tLength = timerText.get_width()
            tHeight = timerText.get_height()
            WIN.blit(timerText, (WIDTH/2 - tLength/2, HEIGHT/2- tHeight/2))
            
        elif current_time - startTime < 3000:
            WIN.blit(PITCH, (0,0))
            timerText = COUNTDOWN_FONT.render(str(1), False, WHITE)
            tLength = timerText.get_width()
            tHeight = timerText.get_height()
            
            WIN.blit(timerText, (WIDTH/2 - tLength/2, HEIGHT/2- tHeight/2))
            
        elif current_time - startTime < 4000:
            break

        pygame.display.flip()
        clock.tick(60)

        


def draw_window_play(leftScore, rightScore, leftPlayer, rightPlayer):
    WIN.blit(PITCH, (0,0))
    
    if sound_check(leftScore, rightScore) == True:
        ENGERLAND_SOUND.play()

    leftPlayerText = NAME_FONT.render(str(leftPlayer),False,WHITE)
    lNameLength = leftPlayerText.get_width()
    rightPlayerText = NAME_FONT.render(str(rightPlayer),False,WHITE)
    rNameLength = rightPlayerText.get_width()
    leftText = SCORE_FONT.render(str(leftScore),False,WHITE)
    rightText = SCORE_FONT.render(str(rightScore),False,WHITE)
    lLength = leftText.get_width()
    rLength = rightText.get_width()
    WIN.blit(leftText, (300 - lLength/2,210))
    WIN.blit(rightText, (600 - rLength/2,210))
    WIN.blit(leftPlayerText,(300 - lNameLength/2, 50) )
    WIN.blit(rightPlayerText, (600 - rNameLength/2, 50))
    pygame.display.update()


def play(leftPlayer,rightPlayer):
    start_count()
    leftScore = 0
    rightScore = 0
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RCTRL:
                    rightScore += 1
                
                if event.key == pygame.K_LCTRL:
                    leftScore += 1
            
            
        draw_window_play(leftScore, rightScore,leftPlayer, rightPlayer)

def main():
    leftPlayer = 'a'
    rightPlayer = 'b'
    play(leftPlayer, rightPlayer)
    
  

if __name__ == "__main__":
  main()