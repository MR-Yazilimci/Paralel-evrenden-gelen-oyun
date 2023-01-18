import pygame

class Enemys:
    def __init__(self,screen_size, character):
        self.screen_size = screen_size
        self.character = character

        self.elvl = 1

        self.image1 = pygame.image.load("enemy1.png")
        self.image1 = pygame.transform.scale(self.image1, (64, 64))
        self.rect1 = self.image1.get_rect()
        self.rect1.x = 100
        self.rect1.y = 100
        self.hp1 = 64

        self.image2 = pygame.image.load("enemy2.png")
        self.image2 = pygame.transform.scale(self.image2, (64, 64))
        self.rect2 = self.image2.get_rect()
        self.rect2.x = 200
        self.rect2.y = 200
        self.hp2 = 64

        self.image3 = pygame.image.load("enemy3.png")
        self.image3 = pygame.transform.scale(self.image3, (64, 64))
        self.rect3 = self.image1.get_rect()
        self.rect3.x = 400
        self.rect3.y = 400
        self.hp3 = 64

        self.image4 = pygame.image.load("enemy4.png")
        self.image4 = pygame.transform.scale(self.image4, (64, 64))
        self.rect4 = self.image2.get_rect()
        self.rect4.x = 100
        self.rect4.y = 400
        self.hp4 = 64

        self.image5 = pygame.image.load("enemy5.png")
        self.image5 = pygame.transform.scale(self.image5, (64, 64))
        self.rect5 = self.image5.get_rect()
        self.rect5.x = 400
        self.rect5.y = 100
        self.hp5 = 64

        self.image6 = pygame.image.load("enemy6.png")
        self.image6 = pygame.transform.scale(self.image6, (64, 64))
        self.rect6 = self.image6.get_rect()
        self.rect6.x = 500
        self.rect6.y = 100
        self.hp6 = 64

        self.image7 = pygame.image.load("enemy7.png")
        self.image7 = pygame.transform.scale(self.image7, (64, 64))
        self.rect7 = self.image7.get_rect()
        self.rect7.x = 100
        self.rect7.y = 200
        self.hp7 = 64

        self.image8 = pygame.image.load("enemy8.png")
        self.image8 = pygame.transform.scale(self.image8, (64, 64))
        self.rect8 = self.image8.get_rect()
        self.rect8.x = 300
        self.rect8.y = 200
        self.hp8 = 64
        self.alan = pygame.image.load("alan.png")
        self.alanrct = self.alan.get_rect()

    def update(self,alanrct):
        self.mxy = pygame.mouse.get_pos()
        self.msxy = [self.mxy[0]/(self.screen_size[0]/1024),self.mxy[1]/(self.screen_size[1]/512)]
        self.alanrct.x,self.alanrct.y = self.msxy[0]-16,self.msxy[1]-16
        if self.rect1.x < self.character.offset[0]:
            self.rect1.x +=1
        elif self.rect1.x > self.character.offset[0]:
            self.rect1.x -=1
        if self.rect1.y < self.character.offset[1]:
            self.rect1.y +=1
        elif self.rect1.y > self.character.offset[1]:
            self.rect1.y -=1
        if self.rect1.colliderect(pygame.Rect(self.character.offset[0],self.character.offset[1],64,64)):
            self.character.hp -=1
        if self.rect1.colliderect(pygame.Rect(self.alanrct.x+self.character.offset[0]+480-1024+64,self.alanrct.y+self.character.offset[1]+224-512+64,32,32)):
            self.hp1 -=1


        if self.rect2.x < self.character.offset[0]:
            self.rect2.x +=1
        elif self.rect2.x > self.character.offset[0]:
            self.rect2.x -=1
        if self.rect2.y < self.character.offset[1]:
            self.rect2.y +=1
        elif self.rect2.y > self.character.offset[1]:
            self.rect2.y -=1
        if self.rect2.colliderect(pygame.Rect(self.character.offset[0],self.character.offset[1],64,64)):
            self.character.hp -=1
        if self.rect2.colliderect(pygame.Rect(self.alanrct.x+self.character.offset[0]+480-1024+64,self.alanrct.y+self.character.offset[1]+224-512+64,32,32)):
            self.hp2 -=1


        if self.rect3.x < self.character.offset[0]:
            self.rect3.x +=1
        elif self.rect3.x > self.character.offset[0]:
            self.rect3.x -=1
        if self.rect3.y < self.character.offset[1]:
            self.rect3.y +=1
        elif self.rect3.y > self.character.offset[1]:
            self.rect3.y -=1
        if self.rect3.colliderect(pygame.Rect(self.character.offset[0],self.character.offset[1],64,64)):
            self.character.hp -=1
        if self.rect3.colliderect(pygame.Rect(self.alanrct.x+self.character.offset[0]+480-1024+64,self.alanrct.y+self.character.offset[1]+224-512+64,32,32)):
            self.hp3 -=1


        if self.rect4.x < self.character.offset[0]:
            self.rect4.x +=1
        elif self.rect4.x > self.character.offset[0]:
            self.rect4.x -=1
        if self.rect4.y < self.character.offset[1]:
            self.rect4.y +=1
        elif self.rect4.y > self.character.offset[1]:
            self.rect4.y -=1
        if self.rect4.colliderect(pygame.Rect(self.character.offset[0],self.character.offset[1],64,64)):
            self.character.hp -=1
        if self.rect4.colliderect(pygame.Rect(self.alanrct.x+self.character.offset[0]+480-1024+64,self.alanrct.y+self.character.offset[1]+224-512+64,32,32)):
            self.hp4 -=1


        if self.rect5.x < self.character.offset[0]:
            self.rect5.x +=1
        elif self.rect5.x > self.character.offset[0]:
            self.rect5.x -=1
        if self.rect5.y < self.character.offset[1]:
            self.rect5.y +=1
        elif self.rect5.y > self.character.offset[1]:
            self.rect5.y -=1
        if self.rect5.colliderect(pygame.Rect(self.character.offset[0],self.character.offset[1],64,64)):
            self.character.hp -=1
        if self.rect5.colliderect(pygame.Rect(self.alanrct.x+self.character.offset[0]+480-1024+64,self.alanrct.y+self.character.offset[1]+224-512+64,32,32)):
            self.hp5 -=1


        if self.rect6.x < self.character.offset[0]:
            self.rect6.x +=1
        elif self.rect6.x > self.character.offset[0]:
            self.rect6.x -=1
        if self.rect6.y < self.character.offset[1]:
            self.rect6.y +=1
        elif self.rect6.y > self.character.offset[1]:
            self.rect6.y -=1
        if self.rect6.colliderect(pygame.Rect(self.character.offset[0],self.character.offset[1],64,64)):
            self.character.hp -=1
        if self.rect6.colliderect(pygame.Rect(self.alanrct.x+self.character.offset[0]+480-1024+64,self.alanrct.y+self.character.offset[1]+224-512+64,32,32)):
            self.hp6 -=1


        if self.rect7.x < self.character.offset[0]:
            self.rect7.x +=1
        elif self.rect7.x > self.character.offset[0]:
            self.rect7.x -=1
        if self.rect7.y < self.character.offset[1]:
            self.rect7.y +=1
        elif self.rect7.y > self.character.offset[1]:
            self.rect7.y -=1
        if self.rect7.colliderect(pygame.Rect(self.character.offset[0],self.character.offset[1],64,64)):
            self.character.hp -=1
        if self.rect7.colliderect(pygame.Rect(self.alanrct.x+self.character.offset[0]+480-1024+64,self.alanrct.y+self.character.offset[1]+224-512+64,32,32)):
            self.hp7 -=1


        if self.rect8.x < self.character.offset[0]:
            self.rect8.x +=1
        elif self.rect8.x > self.character.offset[0]:
            self.rect8.x -=1
        if self.rect8.y < self.character.offset[1]:
            self.rect8.y +=1
        elif self.rect8.y > self.character.offset[1]:
            self.rect8.y -=1
        if self.rect8.colliderect(pygame.Rect(self.character.offset[0],self.character.offset[1],64,64)):
            self.character.hp -=1
        if self.rect8.colliderect(pygame.Rect(self.alanrct.x+self.character.offset[0]+480-1024+64,self.alanrct.y+self.character.offset[1]+224-512+64,32,32)):
            self.hp8 -=1
        
    def draw(self, screen):
        screen.blit(self.image1, (self.rect1.x-self.character.offset[0]+480,self.rect1.y-self.character.offset[1]+224))
        screen.blit(self.image2, (self.rect2.x-self.character.offset[0]+480,self.rect2.y-self.character.offset[1]+224))
        screen.blit(self.image3, (self.rect3.x-self.character.offset[0]+480,self.rect3.y-self.character.offset[1]+224))
        screen.blit(self.image4, (self.rect4.x-self.character.offset[0]+480,self.rect4.y-self.character.offset[1]+224))
        screen.blit(self.image5, (self.rect5.x-self.character.offset[0]+480,self.rect5.y-self.character.offset[1]+224))
        screen.blit(self.image6, (self.rect6.x-self.character.offset[0]+480,self.rect6.y-self.character.offset[1]+224))
        screen.blit(self.image7, (self.rect7.x-self.character.offset[0]+480,self.rect7.y-self.character.offset[1]+224))
        screen.blit(self.image8, (self.rect8.x-self.character.offset[0]+480,self.rect8.y-self.character.offset[1]+224))
        pygame.draw.rect(screen,(255,0,0),(self.rect1.x-self.character.offset[0]+480,self.rect1.y-self.character.offset[1]+211,self.hp1,8))
        pygame.draw.rect(screen,(0,0,0),(self.rect1.x-self.character.offset[0]+480,self.rect1.y-self.character.offset[1]+210,64,10),1)
        pygame.draw.rect(screen,(255,0,0),(self.rect2.x-self.character.offset[0]+480,self.rect2.y-self.character.offset[1]+211,self.hp2,8))
        pygame.draw.rect(screen,(0,0,0),(self.rect2.x-self.character.offset[0]+480,self.rect2.y-self.character.offset[1]+210,64,10),1)
        pygame.draw.rect(screen,(255,0,0),(self.rect3.x-self.character.offset[0]+480,self.rect3.y-self.character.offset[1]+211,self.hp3,8))
        pygame.draw.rect(screen,(0,0,0),(self.rect3.x-self.character.offset[0]+480,self.rect3.y-self.character.offset[1]+210,64,10),1)
        pygame.draw.rect(screen,(255,0,0),(self.rect4.x-self.character.offset[0]+480,self.rect4.y-self.character.offset[1]+211,self.hp4,8))
        pygame.draw.rect(screen,(0,0,0),(self.rect4.x-self.character.offset[0]+480,self.rect4.y-self.character.offset[1]+210,64,10),1)
        pygame.draw.rect(screen,(255,0,0),(self.rect5.x-self.character.offset[0]+480,self.rect5.y-self.character.offset[1]+211,self.hp5,8))
        pygame.draw.rect(screen,(0,0,0),(self.rect5.x-self.character.offset[0]+480,self.rect5.y-self.character.offset[1]+210,64,10),1)
        pygame.draw.rect(screen,(255,0,0),(self.rect6.x-self.character.offset[0]+480,self.rect6.y-self.character.offset[1]+211,self.hp6,8))
        pygame.draw.rect(screen,(0,0,0),(self.rect6.x-self.character.offset[0]+480,self.rect6.y-self.character.offset[1]+210,64,10),1)
        pygame.draw.rect(screen,(255,0,0),(self.rect7.x-self.character.offset[0]+480,self.rect7.y-self.character.offset[1]+211,self.hp7,8))
        pygame.draw.rect(screen,(0,0,0),(self.rect7.x-self.character.offset[0]+480,self.rect7.y-self.character.offset[1]+210,64,10),1)
        pygame.draw.rect(screen,(255,0,0),(self.rect8.x-self.character.offset[0]+480,self.rect8.y-self.character.offset[1]+211,self.hp8,8))
        pygame.draw.rect(screen,(0,0,0),(self.rect8.x-self.character.offset[0]+480,self.rect8.y-self.character.offset[1]+210,64,10),1)