import pygame

class Character:
    def __init__(self,screen_size,enemys,lvl):
        self.screen_size = screen_size
        self.lvl = lvl
        self.enemys = enemys
        self.hp = 100
        self.image = pygame.image.load("character.png")
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = 1024 / 2 - self.rect.width / 2
        self.rect.y = 512 / 2 - self.rect.height / 2
        self.speed = 4
        self.offset = [0, 0]
        self.mxy = pygame.mouse.get_pos()
        self.mos = pygame.mouse.get_pressed()
        self.keys = pygame.key.get_pressed()
        self.sira = 0
        self.bombs = pygame.image.load("bombs.png")
        self.bomb = pygame.image.load("bomb.png")
        self.ahp = pygame.image.load("hp.png")
        self.kalkan = pygame.image.load("kalkan.png")
        self.kalkans = pygame.image.load("kalkans.png")
        self.isirs = pygame.image.load("isirik.png")
        self.alan = pygame.image.load("alan.png")
        self.alanrct = self.alan.get_rect()
        self.m = 0

    def update(self):
        self.mxy = pygame.mouse.get_pos()
        self.msxy = [self.mxy[0]/(self.screen_size[0]/1024),self.mxy[1]/(self.screen_size[1]/512)]
        self.mos = pygame.mouse.get_pressed()
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_w]:
            self.offset[1] -= self.speed
        if self.keys[pygame.K_s]:
            self.offset[1] += self.speed
        if self.keys[pygame.K_a]:
            self.offset[0] -= self.speed
        if self.keys[pygame.K_d]:
            self.offset[0] += self.speed

        self.alanrct.x,self.alanrct.y = self.msxy[0]-16,self.msxy[1]-16

        if self.mos[0]:
            self.m = 1
        else:
            self.m = 0

    def draw(self, screen):
        if self.m == 1:
            screen.blit(self.alan,self.alanrct)
        screen.blit(self.image, self.rect)
        screen.blit(self.bombs, (512-16,512-34))
        screen.blit(self.kalkans, (512+20,512-34))
        screen.blit(self.isirs, (512-52,512-34))
        pygame.draw.rect(screen,(0,0,0),(1024-104,1,102,12),1)
        pygame.draw.rect(screen,(255,0,0),(1024-103,2,self.hp,10))