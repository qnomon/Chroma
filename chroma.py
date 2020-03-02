'''--------------------------Jogo desenvolvido por Giovanna Requena para o primeiro semestre de
jogos digitais da FATEC Antonio Russo - São caetano do sul. --------------------------------------'''

#Importação das bibliotecas
import pygame
from pygame import locals
import colorsys
import random
import math
import time

#Definição das variáveis do jogo: Tamanho da tela e framerate
WIDTH = 800
HEIGHT = 600
FPS = 60
branco = (255,255,255)


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))   #Criação da janela do jogo
pygame.display.set_caption("Chroma")            #Nome do jogo na janela do pygame
clock = pygame.time.Clock()                         #Definição do clock de FPS
pecas = []                                          #Lista dos sprites de blocos

cores_purp = {'blocos':[(91,73,97), (139,88,113),(168,109,128),(185,154,157)],'fundo': (20,20,20),'barra':(139,88,113), 'bola': (242,196,6)}
cores_blue = {'blocos':[(17,34,54), (67,98,127), (165,186,219), (219,228,237)],'fundo': (20,20,20),'barra':(67,98,127), 'bola': (242,196,6)}
cores_oran = {'blocos':[(140,70,70), (220,111,104), (224,139,118), (252,211,155)],'fundo': (20,20,20),'barra':(220,111,104), 'bola': (120,196,230)}
cores_green = {'blocos':[(37,53,42), (73,101,78), (139,168,137), (192,207,178)],'fundo': (20,20,20),'barra':(73,101,78), 'bola': (242,196,6)}
cores_lib = {}
cores_lib['purple'] = cores_purp
cores_lib['blue'] = cores_blue
cores_lib['orange'] = cores_oran
cores_lib['green'] = cores_green
#cores_atual = random.choice(['purple', 'blue', 'orange', 'green'])

fases = ['green','purple','blue','orange']
fasesind = 0
cores_atual = fases[fasesind]

snd1 = pygame.mixer.Sound('Sounds/snd1.wav')        #Som de contato com parede
snd2 = pygame.mixer.Sound('Sounds/snd2.wav')        #Som de contato com blocos
music = pygame.mixer.music.load('Sounds/music.mp3')
volume = 1




#Carregando os fundos #Fase verde
bg = pygame.image.load('Sprites/plx-1.png').convert()
bgf = pygame.transform.scale(bg,(710,490))
bg2 = pygame.image.load('Sprites/plx-2.png').convert()
bg2.set_colorkey((0,0,0))
bg2f = pygame.transform.scale(bg2,(710,490))
bg3 = pygame.image.load('Sprites/plx-3.png').convert()
bg3.set_colorkey((0,0,0))
bg3f = pygame.transform.scale(bg3,(710,490))
bg4 = pygame.image.load('Sprites/plx-4.png').convert()
bg4.set_colorkey((0,0,0))
bg4f = pygame.transform.scale(bg4,(710,490))
bg5 = pygame.image.load('Sprites/plx-5.png').convert()
bg5.set_colorkey((0,0,0))
bg5f = pygame.transform.scale(bg5,(710,490))

#carregando fundos Fase azul
teste = pygame.image.load('Sprites/teste.jpg').convert()
teste.set_colorkey((255,0,255))
testef = pygame.transform.scale(teste,(710,490))

#carregando fundos fase rosa
pla01 = pygame.image.load('Sprites/fnd01.jpg').convert()
pla1 = pygame.transform.scale(pla01,(710,490))

#fundo orange
vulcan = pygame.image.load('Sprites/vulcan.png').convert()

#carregando powerups
pwrup_img = {}
pwrup_img['purple'] = pygame.image.load('Sprites/pwpurple.png').convert()
pwrup_img['blue'] = pygame.image.load('Sprites/pwblue.png').convert()
pwrup_img['green'] = pygame.image.load('Sprites/pwgreen.png').convert()
pwrup_img['orange'] = pygame.image.load('Sprites/pworange.png').convert()
vidaload = pygame.image.load('Sprites/vida.png').convert()
vidaload.set_colorkey((255,0,255))
vida = pygame.transform.scale(vidaload, (30,28))

#menu e outros
menuimg = pygame.image.load('Sprites/menu.png').convert()
som = []
som00 = pygame.image.load('Sprites/som00.png').convert()
som00.set_colorkey((181,181,181))
som.append(som00)
som01 = pygame.image.load('Sprites/som01.png').convert()
som01.set_colorkey((181,181,181))
som.append(som01)
icon = pygame.image.load('Sprites/icon.png')
pygame.display.set_icon(icon)


#Carregando portal
portal = []
for i in range(9):
    filename = 'Sprites/portal_0{}.png'.format(i)
    imgload = pygame.image.load(filename).convert()
    imgload.set_colorkey((255,0,255))
    img = pygame.transform.scale(imgload, (480,480))
    portal.append(img)




'''criação da função para escrever texto na tela'''
font_name = pygame.font.match_font('arial')           #Faz com que o sistema encontre uma fonte 'Arial' disponivel
score = 0                                             #Iniciação da variavel de Score

def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 37 * i
        img_rect.y = y
        surf.blit(img, img_rect)

def menu():
    menu = True
    cor1 = (104,104,104)
    cor2 = (86,86,86)
    cor3 = (53,53,53)
    last = pygame.time.get_ticks()
    last_ver = pygame.time.get_ticks()
    i = 0
    si = 0
    music_paused = False
    global volume
    tela = pygame.Surface((800, 700))
    tela.set_colorkey((255, 255, 255))
    all_sprites = pygame.sprite.Group()
    particles = pygame.sprite.Group()
    while menu:
        for x in range(3):
            particula = ParticleMenu()
            all_sprites.add(particula)
            particles.add(particula)

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if l1.collidepoint(event.pos) or l2.collidepoint(event.pos):
                    menu = False
                if l3.collidepoint(event.pos) or l4.collidepoint(event.pos):
                    level()
                if l5.collidepoint(event.pos) and not music_paused and pygame.time.get_ticks() - last_ver > 250 :
                    pygame.mixer.music.pause()
                    volume = 0
                    music_paused = True
                    last_ver = pygame.time.get_ticks()
                    si = 1
                if l5.collidepoint(event.pos) and music_paused and pygame.time.get_ticks() - last_ver > 250:
                    pygame.mixer.music.unpause()
                    volume = 1
                    music_paused = False
                    last_ver = pygame.time.get_ticks()
                    si = 0


        screen.blit(menuimg, (0,0))
        screen.blit(portal[i], (350, 75))
        if pygame.time.get_ticks() - last > 50:
            last = pygame.time.get_ticks()
            i += 1
            if i >= len(portal):
                i = 0

        screen.blit(tela, (0, 0))
        tela.fill((0, 0, 0))
        tela.set_colorkey((0, 0, 0))
        all_sprites.draw(tela)
        pygame.draw.polygon(tela, (0, 0, 0), [(0, 0), (640, 250), (640, 340), (0, 700), (800, 700), (800, 0)])
        all_sprites.update()

        l1 = pygame.draw.polygon(screen, (cor1), [(177,288),(177,233),(225,206),(272,233),(272,288),(225,315)])
        l2 = pygame.draw.polygon(screen, (cor1), [(277,288),(277,233),(325,206),(372,233),(372,288),(325,315)])
        l3 = pygame.draw.polygon(screen, (cor2), [(128,373),(128,318),(176,291),(223,318),(223,373),(176,400)])
        l4 = pygame.draw.polygon(screen, (cor2), [(228,373),(228,318),(276,291),(323,318),(323,373),(276,400)])
        l5 = pygame.draw.polygon(screen, (cor3),[(328,373),(328,318),(376,291), (423,318), (423,373), (376, 400)])



        screen.blit(som[si], (346, 318))

        draw_text_menu(screen, 'Croma', 92, 157, 108, (220, 138, 118))
        draw_text(screen, 'Jogar',50, 272,224, (255,255,255))
        draw_text(screen, 'Fases', 50, 222, 308, (255, 255, 255))


        if l1.collidepoint(pygame.mouse.get_pos()) or l2.collidepoint(pygame.mouse.get_pos()):
            cor1 = (163,79,111)
        else:
            cor1 = (104,104,104)
        if l3.collidepoint(pygame.mouse.get_pos()) or l4.collidepoint(pygame.mouse.get_pos()):
            cor2 = (78,94,160)
        else:
            cor2 = (86,86,86)
        if l5.collidepoint(pygame.mouse.get_pos()) :
            cor3 = (119,219,124)
        else:
            cor3 = (53,53,53)
        pygame.display.update()

def unfreeze():
    if hits.isfreeze:
        hits.isfreeze = False
    hits.vida -= 1

def speedup():
    if hits.isfire:
        bola.accelerate()


def level():
    level = True
    global cores_atual
    i = 0
    last = pygame.time.get_ticks()
    tela = pygame.Surface((800, 700))
    tela.set_colorkey((255, 255, 255))
    all_sprites = pygame.sprite.Group()
    particles = pygame.sprite.Group()
    while level:
        clock.tick(FPS)
        for x in range(3):
            particula = ParticleMenu()
            all_sprites.add(particula)
            particles.add(particula)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if blue.collidepoint(event.pos):
                    cores_atual = 'blue'
                if green.collidepoint(event.pos):
                    cores_atual = 'green'
                if orange.collidepoint(event.pos):
                    cores_atual = 'orange'
                if purple.collidepoint(event.pos):
                    cores_atual = 'purple'
                if back.collidepoint(event.pos):
                    level = False


        screen.blit(menuimg,(0,0))

        screen.blit(portal[i], (350, 75))
        if pygame.time.get_ticks() - last > 50:
            last = pygame.time.get_ticks()
            i += 1
            if i >= len(portal):
                i = 0

        screen.blit(tela, (0, 0))
        tela.fill((0, 0, 0))
        tela.set_colorkey((0, 0, 0))
        all_sprites.draw(tela)
        pygame.draw.polygon(tela, (0, 0, 0), [(0, 0), (640, 250), (640, 340), (0, 700), (800, 700), (800, 0)])
        all_sprites.update()

        draw_text_menu(screen, 'Croma', 92, 157, 108, (220, 138, 118))

        blue = pygame.draw.rect(screen, (50, 50, 125), ((50, 250), (100, 100)))
        green = pygame.draw.rect(screen, (50, 125, 50), ((160, 250), (100, 100)))
        orange = pygame.draw.rect(screen, (255, 125, 50), ((50, 360), (100, 100)))
        purple = pygame.draw.rect(screen, (125, 50, 125), ((160, 360), (100, 100)))
        back = pygame.draw.rect(screen, (125, 125, 125), ((50, 500), (210, 50)))
        pygame.display.update()



def pause():
    paused = True
    while paused:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
        draw_text(screen, 'Pause: Press C to continue', 40, WIDTH / 2, HEIGHT / 2, branco)
        pygame.display.update()


def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

def draw_text(surf, text, size, x, y, color = cores_lib[cores_atual]['blocos'][3]):
    global cores_lib
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def draw_text_menu(surf, text, size, x, y, color = cores_lib[cores_atual]['blocos'][3]):
    global cores_lib
    font = pygame.font.Font('font_menu.otf', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surf.blit(text_surface, text_rect)


#Classe que da origem aos objetos dos blocos
class Blocos(pygame.sprite.Sprite):
    def __init__(self, x, y,indice):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((37,32))          #Define sprite da lista como sprite do objeto
        self.rect = self.image.get_rect()
        self.indice = indice
        self.color = cores_lib[cores_atual]['blocos'][self.indice]
        self.image.set_colorkey((0,0,0))
        self.hexagon = pygame.draw.polygon(self.image,self.color , [(0,16), (9,32),(28,32),(37,16),(28,0),(9,0)])
        self.rect.centerx = 90 + x          #Alinhamento do bloco em X
        self.rect.centery = 85 + y          #Alinhamento do bloco em Y
        self.speedy = 5
        self.vida = 1
        self.isapple = False
        self.isfreeze = False
        self.isinvisible = False
        self.isfire = False
        self.firecolor = [(255,115,0), (255,183,0), (255,0,0)]
        self.fireind = 0
        self.firedelay = pygame.time.get_ticks()

    def apple(self):
        self.value = random.random()
        if self.value > 0.99995:
            self.isapple = True

    def fire(self):
        self.value = random.random()
        if self.value > 0.99995:
            self.isfire = True

    def freeze(self):
        self.value = random.random()
        if self.value > 0.99995:
            self.isfreeze = True

    def invisible(self):
        self.value = random.random()
        if self.value > 0.99995:
            self.isinvisible = True

    def update(self):
        if cores_atual == 'green':
            self.apple()
        if self.isapple == True:
            self.color = (255,50,50)
            self.rect.centery += self.speedy
            self.hexagon = pygame.draw.polygon(self.image,self.color , [(0,16), (9,32),(28,32),(37,16),(28,0),(9,0)])
        if cores_atual == 'blue':
            self.freeze()
        if self.isfreeze == True:
            self.color = (42, 131, 250)
            self.hexagon = pygame.draw.polygon(self.image, self.color,[(0,16),(9,32),(28,32),(37,16),(28,0),(9,0)])
            self.vida = 2
        if cores_atual == 'purple':
            self.invisible()
        if self.isinvisible == True:
            self.image.set_alpha(25)
        if cores_atual == 'orange':
            self.fire()
        if self.isfire == True:
            self.color = self.firecolor[self.fireind]
            self.hexagon = pygame.draw.polygon(self.image, self.color,[(0, 16), (9, 32), (28, 32), (37, 16), (28, 0), (9, 0)])
            if pygame.time.get_ticks() - self.firedelay > 100:
                self.firedelay = pygame.time.get_ticks()
                self.fireind +=1
            if self.fireind > 2:
                self.fireind = 0

        if self.rect.top > 600:
            self.kill()

        if self.vida <= 0:
            self.kill()




class ParticleMenu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((4,4))
        self.x = 0
        self.color = hsv2rgb(self.x,1,1)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(-100,754)
        self.rect.centery = random.randint(602,700)
        self.speedy = random.randint(-10,-5)
        self.cres = True
        self.desc = False
        self.angle = 0
        self.inicio = self.rect.centerx
        self.orange = [0.122, 0.075, 1]

    def update(self):
        self.image.fill(self.color)
        self.rect.centery += self.speedy // 2 + (math.sin(self.angle) * 8)
        self.rect.centerx = self.inicio - (math.cos(self.angle) * 25)
        self.color = (hsv2rgb(self.x,1,1))
        self.angle += 0.2
        if self.x <= 1 and self.cres:
            self.x = self.x + 0.005
        if self.x >= 1.00:
            self.cres = False
            self.desc = True
        if self.desc:
            self.x = self.x - 0.005
        if self.x <= 0:
            self.desc = False
            self.cres = True
        if self.rect.bottom < 50 or self.rect.right > 754:
            self.kill()




class Particle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((4,4))
        self.x = 0
        self.color = hsv2rgb(0.23,self.x,1)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(-100,754)
        if cores_atual == 'green':
            self.rect.centery = random.randint(50,155)
        else:
            self.rect.centery = random.randint(602,700)
        self.speedy = random.randint(-10,-5)
        self.cres = True
        self.desc = False
        self.angle = 0
        self.inicio = self.rect.centerx
        self.orange = [0.122, 0.075, 1]
        if cores_atual == 'orange':
            self.color = hsv2rgb(random.choice(self.orange),1,1)

    def update(self):
        self.image.fill(self.color)
        if cores_atual == 'blue':
            self.rect.centery += self.speedy // 2
            self.rect.centerx = self.inicio + (math.sin(self.angle) * 15)
            self.color = (hsv2rgb(0.742, random.randint(49, 100) / 100, 1))
           # self.image.set_alpha(random.randint(0,255))
            self.angle += 0.2
        if cores_atual == 'orange':
            self.rect.centery += self.speedy//2
            self.rect.centerx = self.inicio + (math.cos(self.angle) * 8)
            self.angle += 0.2
        if cores_atual == 'green':
            self.rect.centery += -self.speedy
            self.rect.centerx = self.rect.left + math.cos(self.angle) * 6
            self.color = (hsv2rgb(0.62,random.randint(49,100)/100, 1))
        if cores_atual == 'purple':
            self.rect.centery += self.speedy//2 + (math.sin(self.angle) * 8)
            self.rect.centerx = self.inicio + (math.cos(self.angle) * 8)
            self.color = (hsv2rgb(0.766, random.randint(49, 100) / 100, 1))
            self.angle += 0.2

        if self.x <= 1 and self.cres:
            self.x = self.x + 0.005
        if self.x >= 1.00:
            self.cres = False
            self.desc = True
        if self.desc:
            self.x = self.x - 0.005
        if self.x <=0:
            self.desc = False
            self.cres = True
        if cores_atual == 'green':
            if self.rect.bottom > 600 or self.rect.right > 754:
                self.kill()
        elif cores_atual == 'orange':
            if self.rect.top < random.randint(100,400) or self.rect.right >754:
                self.kill()
        else:
            if self.rect.bottom < 50 or self.rect.right > 754:
                self.kill()


 #Classe que da origem ao bloco do jogador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = 90
        self.image = pygame.Surface((self.size,10)) #Criação da superficie
        self.image.fill(cores_lib[cores_atual]['blocos'][3])              #Preenchimento da superficie com a cor 1
        self.rect = self.image.get_rect()    #Cria um objeto com as medidas retangulares do sprite
        self.rect.centerx = WIDTH / 2        #Posição inicial em X
        self.rect.centery = HEIGHT - 56      #Posição inicial em Y
        self.speedx = 0                      #Velocidade de deslocamento
        self.modspeed = 5
        self.life = 3

    #Metodo que roda a cada ciclo de atualização
    def update(self):
        self.speedx = 0                     #Caso parado velocidade de deslocamento é zero
        keystate = pygame.key.get_pressed() #Variavel para verificar a tecla pressionada
        if keystate[pygame.K_LEFT]:         #Se a tecla pressionada for a Seta direcional Esquerda
            self.speedx = -self.modspeed                #Velocidade de deslocamento é -5
        if keystate[pygame.K_RIGHT]:        #Se a tecla pressionada for a Seta direcional Direita
            self.speedx = self.modspeed                #Velocidade de deslocamento é 5
        if keystate[pygame.K_p]:
            pause()
        if keystate[pygame.K_SPACE] and bola.ready:
            bola.newball()

        self.rect.x += self.speedx          #Soma a cada ciclo a velocidade de deslocamento a posição na tela
        if self.rect.right > 754:           #Se a posição retangular direita for maior que 754 (Limite definido)
            self.rect.right = 754           #A posição retangular direita se fora 754
        if self.rect.left < 49:             #Se a posição retangular esquerda for menor que 49
            self.rect.left = 49             #A posição retangular esquerda se torna 49

        if bola.ready:
            bola.rect.centerx = self.rect.centerx


#Criação da classe da bolinha
class Bola(pygame.sprite.Sprite):
    def __init__(self, x, y, speedy=3, speedx=random.choice((4,5,6)), ready = False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))         #Criação da superficie da bolinha
        self.sphere1 = pygame.draw.circle(self.image, (cores_lib[cores_atual]['bola']), (10,10),10)       #Desenha uma bolinha amarela na superficie
        self.image.set_colorkey((0,0,0))            #Define a cor transparente como preto
        self.rect = self.image.get_rect()           #Cria objeto com as dimensões retangulares
        self.rect.centery = y                       #Posição inicial Y
        self.rect.centerx = x                       #Posição inicial X
        self.initspeedx = speedx
        self.initspeedy = -speedy
        self.ready = ready
        if self.ready:
            self.speedy = 0                           #Velocidade de deslocamento em Y
            self.speedx = 0                            #Velocidade de deslocamento em X
        else:
            self.speedy = self.initspeedy
            self.speedx = self.initspeedx
        self.isaccelerate = False
        self.bufftime  = pygame.time.get_ticks()


    #Metodo que atualiza a cada ciclo
    def update(self):
        self.rect.y += self.speedy    #Soma a velocidade de deslocamento Y na posição Y
        self.rect.x += self.speedx    #Soma a velocidade de deslocamento X na posição X
        if self.rect.right >= 754:    #Limite das bordas da tela
            self.speedx = -self.speedx
            snd1.play()               #Se bater nas bordas toca um som
        if self.rect.left <= 49:
            self.speedx = -self.speedx
            snd1.play()
        if self.rect.top <=50:
            self.speedy = -self.speedy
            snd1.play()
        if self.rect.top > HEIGHT:
            self.kill()
        if self.isaccelerate:
            if pygame.time.get_ticks() - self.bufftime > 2000:
                self.isaccelerate = False
                if self.speedy > 0:
                    self.speedy -= 1
                else:
                    self.speedy += 1
                if self.speedx > 0:
                    self.speedx -= 1
                else:
                    self.speedx += 1


    def newball(self):
        self.speedx = self.initspeedx
        self.speedy = self.initspeedy
        self.ready = False



    def accelerate(self):
        self.isaccelerate = True
        if self.speedy > 0:
            self.speedy += 1
        else:
            self.speedy -= 1
        if self.speedx > 0:
            self.speedx += 1
        else:
            self.speedx -= 1
        self.bufftime = pygame.time.get_ticks()



class Fundo(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((800, 600))
      #  self.image.fill(cores_lib[cores_atual]['fundo'])
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH /2
        self.rect.centery = HEIGHT /2
        self.x = 0.0
        self.color = (hsv2rgb(self.x, 1, 1))
        self.cres = True
        self.desc = False
        self.lbar = pygame.draw.rect(self.image, (20,20,20), ((0,0), (46,600)))
        self.barra = pygame.draw.rect(self.image, cores_lib[cores_atual]['barra'], ((0, 539), (800, 61)))
        self.limitl = pygame.draw.line(self.image, branco, (46,50), (46,600))
        self.limitr = pygame.draw.line(self.image, branco, (754,50), (754,600))
        self.limitt = pygame.draw.line(self.image, branco, (46,50), (754,50))
        self.angle = 0

                                     

    def update(self):
        self.color = (hsv2rgb(self.x, 1, 1))
        if self.x <= 1 and self.cres:
            self.x = self.x + 0.005
        if self.x >= 1.00:
            self.cres = False
            self.desc = True
        if self.desc:
            self.x = self.x - 0.005
        if self.x <=0:
            self.desc = False
            self.cres = True
        self.line1t = pygame.draw.line(self.image, self.color, (324, 11), (754, 11))
        self.line2t = pygame.draw.line(self.image, self.color, (252, 24), (754, 24))
        self.line3t = pygame.draw.line(self.image, self.color, (156, 37), (754, 37))
        self.line1l = pygame.draw.line(self.image, self.color, (9, 316), (9, 600))
        self.line2l = pygame.draw.line(self.image, self.color, (22, 245), (22, 600))
        self.line3l = pygame.draw.line(self.image, self.color, (34, 150), (34, 600))
        self.line1r = pygame.draw.line(self.image, self.color, (766, 150), (766, 600))
        self.line2r = pygame.draw.line(self.image, self.color, (778, 245), (778, 600))
        self.line3r = pygame.draw.line(self.image, self.color, (790, 316), (790, 600))
        self.angle += 0.2

class Pow(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(('bola', 'bspeed', 'platspeed'))
        self.image = pwrup_img[cores_atual]
        self.image.set_colorkey((255, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        # kill if its move to top of screen
        if self.rect.top > HEIGHT:
            self.kill()




all_sprites = pygame.sprite.Group()
particles = pygame.sprite.Group()

#Laço infinito do jogo
running = True   #Jogo rodando
ismenu = True
gameover = True
pygame.mixer.music.play(loops=-1)
while running:
    if ismenu:
        menu()
        ismenu = False
        score = 0

    if gameover:
        indice = 0  # Índice dos sprites dos blocos
        bolas = pygame.sprite.Group()  # Grupo de sprites da bola    (Grupos de sprites funcionam como listas)
        blocos = pygame.sprite.Group()  # Grupo de sprites dos blocos
        all_sprites = pygame.sprite.Group()  # Grupo de todos os sprites
        fundo = Fundo()
        particles = pygame.sprite.Group()
        powerups = pygame.sprite.Group()
        all_sprites.add(fundo)

        # Laço de criação dos blocos
        for x in range(11):
            for y in range(4):
                bloco = Blocos(x * (31 * 2), y * 34, indice)  # Posição dos blocos
                blocos.add(bloco)  # Adiciona o objeto criado no grupo dos blocos
                all_sprites.add(bloco)  # Adiciona o objeto criado no grupo de todos os sprites
                indice += 1  # Soma 1 no índice dos sprites, cada interação troca a cor dos sprites
                if indice > 3:  # Se o valor dos sprites passar de 3 ele retorna ao valor inicial  0
                    indice = 0

        # Mesmo laço acima com mudança no posicionamento
        for x in range(10):
            for y in range(4):
                bloco = Blocos(31 + x * (31 * 2), 17 + y * 34, indice)
                blocos.add(bloco)
                all_sprites.add(bloco)
                indice += 1
                if indice > 3:
                    indice = 0

        player = Player()  # Cria o objeto jogador
        all_sprites.add(player)  # Adiciona o objeto jogador ao grupo de todos os sprites
        bola = Bola(WIDTH / 2, HEIGHT - 72, ready=True)  # Cria o objeto da bola na posição inicial
        all_sprites.add(bola)  # Adiciona o objeto da bola no grupo de todos os sprites
        bolas.add(bola)  # Adiciona a bola no grupo da bola
        snd1.set_volume(volume)
        snd2.set_volume(volume)
        gameover = False
    clock.tick(FPS)
    screen.fill((20,20,20))

    if cores_atual == 'orange':
        for x in range(0,5):
            particle = Particle()
            particles.add(particle)
    else:
        particle = Particle()
        particles.add(particle)
    # Processo de entrada de eventos
    for event in pygame.event.get():
        # Checa se a janela for fechada
        if event.type == pygame.QUIT:
            running = False    #Se for fechada o jogo para de rodar


    if cores_atual == 'green':
        screen.blit(bgf,(46,50))
        screen.blit(bg2f, (46, 50))
        screen.blit(bg3f, (46, 50))
        screen.blit(bg4f, (46, 50))
        screen.blit(bg5f, (46, 50))

    if cores_atual == 'blue':
        screen.blit(testef, (46,50))

    if cores_atual == 'purple':
        screen.blit(pla1, (46,50))

    if cores_atual == 'orange':
        screen.blit(vulcan, (46,50))


    particles.update()
    particles.draw(screen)
    all_sprites.update()     #Faz rodar o método update de todos os prites do grupo
    all_sprites.draw(screen) #Desenha na tela todos os sprites

    #Colisão do jogador com a bola
    hit = pygame.sprite.spritecollide(player,bolas, False)  #Verifica se dois objetos colidiram, False = não exclui os objetos
    for hits in hit:         #Para cada interação nos grupos verifica
        hits.speedy = -hits.speedy   #Se houve colisão inverte o deslocamento da bola em Y
        snd1.play()

    if len(bolas) == 0:
        bola = Bola(WIDTH / 2, HEIGHT - 72, ready=True)  # Cria o objeto da bola na posição inicial
        all_sprites.add(bola)  # Adiciona o objeto da bola no grupo de todos os sprites
        bolas.add(bola)
        player.life -= 1

    if player.life == 0:
        ismenu = True
        gameover = True

    if len(blocos) == 0 and gameover == False:
        fasesind += 1
        if fasesind >= len(fases):
            fasesind = 0
        cores_atual = fases[fasesind]
        gameover = True



    hit = pygame.sprite.spritecollide(player, powerups, True)
    for hits in hit:
        if hits.type == 'bspeed':
            if bola.speedy > 0:
                bola.speedy += 1
            else:
                bola.speedy -= 1
            if bola.speedx > 0:
                bola.speedx += 1
            else:
                bola.speedx -= 1
        if hits.type == 'platspeed':
            player.modspeed += 2
        if hits.type == 'bola':
            bola = Bola(bola.rect.centerx-10, bola.rect.centery)
            bolas.add(bola)
            all_sprites.add(bola)
            bola = Bola(bola.rect.centerx+10, bola.rect.centery)
            bolas.add(bola)
            all_sprites.add(bola)
        print(hits.type)


    hit = pygame.sprite.groupcollide(blocos,bolas, False, False)  #Exclui os blocos mas não a bola
    for bola in bolas:
        for hits in hit:        #Para cada interação nos grupos se houve colisão
            score += 50         #Aumenta o valor do score
            if random.random() > 0.92:
                pow = Pow(hits.rect.center)
                all_sprites.add(pow)
                powerups.add(pow)
            if hits.rect.bottom in range(bola.rect.top, bola.rect.top+5):   #Se o topo da bola colidir com a base do bloco
                bola.speedy = -bola.speedy        #Inverte o deslocamento da bola em Y
                snd2.play()                       #Toca som de colisão da bola com o bloco
                unfreeze()
                speedup()
            if hits.rect.top in range(bola.rect.bottom-5, bola.rect.bottom): #Se a base da bola colidir com o topo do bloco
                bola.speedy = -bola.speedy
                snd2.play()                      #Toca som de colisão da bola com o bloco
                unfreeze()
                speedup()
            if hits.rect.right in range(bola.rect.left, bola.rect.left+7):  #Se a lateral esquerda da bola colidir com a lateral direita do bloco
                bola.speedx = -bola.speedx
                snd2.play()                     #Toca som de colisão da bola com o bloco
                unfreeze()
                speedup()
            if hits.rect.left in range(bola.rect.right-7, bola.rect.right):  #Se a lateral direita da bola colidir com a lateral esquerda do bloco
                bola.speedx = -bola.speedx
                snd2.play()                       #Toca som de colisão da bola com o bloco
                unfreeze()
                speedup()

    print(len(blocos))
    draw_text(screen, "SCORE: " + str(score), 32, 150, HEIGHT - 50, (255,255,255))   #Escreve o score na tela
    draw_lives(screen, 620, 550, player.life, vida)
    pygame.display.flip()                       #Flipa a tela para começar a desenhar de novo

pygame.quit()
