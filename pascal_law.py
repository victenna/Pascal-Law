import pygame,sys,math,time
#from pygame.locals import *
pygame.init()
size = 1300, 900
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Window Name')#window name
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)
DEEPSKYBLUE=(0,191,255)
WHITE=(255,255,255)
BLACK=(0,0,0)
YELLOW=(255,255,0)
PURPLE=(128,0,128)
LIME=(0,255,0)
GREY=(220,220,220)
TEAL=(0,128,128)
timer=pygame.time.Clock()

img1=pygame.image.load('image1P.png')
img2=pygame.image.load('image2P.png')
#img2=pygame.transform.scale(img2,(473,325))
img3=pygame.image.load('image3P.png')
img3=pygame.transform.scale(img3,(394,160))
img4=pygame.image.load('image4P.png')
cursor=pygame.image.load('cursor.png')
X1,Y1=243,250 
X2,Y2=819,-10# position of image with car
X3,Y3=-70,290# маленький поршень 
X4,Y4=909,305
X5,Y5=20,550# question position


dY2=0.3
dX3=2

font0 = pygame.font.SysFont(None, 60)
message0 = font0.render('ГИДРАВЛИЧЕСКИЙ ПРЕСС(Закон Паскаля)', True, BLUE)

font1 = pygame.font.SysFont(None, 30)
message1 = font1.render('P1=давление жидкости под поршнем маленького диаметра;  ', True, BLACK)

message2 = font1.render('S1=площадь поперечного сечения маленького поршня', True, BLACK)
message3 = font1.render('P2=давление жидкости под поршнем большого диаметра;  ', True, BLACK)
message4 = font1.render('S2=площадь поперечного сечения большого поршня', True, BLACK)


score=0
message5 = font0.render('Количество правильных ответов=', True, BLUE)
message6= font0.render(str(score), True, 'blue')



    

#-----------------------------------------------------
text = ''

A=0
answer=0
s1=0
pi=math.pi

font = pygame.font.SysFont(None, 48)
wrong = font.render('Ответ неправильный', True, RED)
right = font.render('Ответ Правильный', True, RED)
q_number=1

questions=[0,pygame.image.load('question1P.png'),pygame.image.load('question2P.png'),\
           pygame.image.load('question3P.png'),pygame.image.load('question4P.png'),\
           pygame.image.load('question5P.png')]
q_answer=[2500,150,4,5,11]
number_of_answers=0

def question_answer(m):
    global number_of_answers
    global text
    global answer
    global s1
    global q_number
    global score
    screen.blit(questions[m],(X5,Y5))
    if q_number==m:
        if answer==q_answer[m-1]:
            text=str(q_answer[m-1])
            screen.blit(right,(200,550))
            s1=s1+1
            print('s1=',s1)
            #score=score+1
            
            if s1==99:
                text=''
                score=score+1
                number_of_answers=number_of_answers+1
                
            if s1==100:
                text=''
                s1=0
                #A=0
                answer=0
                
                q_number=q_number+1
        if answer!=q_answer[m-1] and answer!=0:
            screen.blit(wrong,(200,550))
            text=''
            s1=s1+1
            if s1==100:
                s1=0
                q_number=q_number+1
                number_of_answers=number_of_answers+1
                answer=0

X3=0
s2=0

while True: # the main game loop
    #print('q_number=',q_number)
    screen.fill('gold')
    screen.blit(message0,(300,10))
    screen.blit(img1,(X1,Y1))
    screen.blit(img2,(X2,Y2)) #image with car
    screen.blit(img3,(X3,Y3))
    screen.blit(img4,(X4,Y4))
    
    screen.blit(message1,(10,100))
    screen.blit(message2,(10,130))
    screen.blit(message3,(10,160))
    screen.blit(message4,(10,190))
    
    print('X3=',X3)
    
    X3=X3+dX3

    Y2=Y2-dY2
        
        
    if X3>189:
        X2,Y2=819,-10# position of image with car
        X3,Y3=-70,290# маленький поршень 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #pygame.quit()
            exit()
            #sys.exit()

        if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
                    A=text
                if event.key == pygame.K_RETURN:
                    answer=int(A)
                    #text=''    
       
    if q_number==1:
        question_answer(1)
    if q_number==2:
        question_answer(2)
    if q_number==3:
        question_answer(3)
    if q_number==4:
        question_answer(4)
    if q_number==5:
        question_answer(5)
        
    font2 = pygame.font.SysFont(None, 48)
    text_surface = font2.render(text, True, RED)
    
    if time.time() % 1 > 0.5:
        screen.blit(cursor,(65,501))
    screen.blit(text_surface, (70,505))
    pygame.draw.rect(screen, BLACK,[50,500,130,40],4)
    print('score=',score)
    if number_of_answers==5:
        s2=s2+1
        
        screen.blit(message5,(400,825))
        
        message6= font0.render(str(score), True, 'blue')
        screen.blit(message6,(1105,826))
        if s2>100:
            
            
            break
    #score=0
    #screen.blit(message5,(400,825))
    #screen.blit(message6,(1105,826))
    pygame.display.update()
    timer.tick(40)
       
   

