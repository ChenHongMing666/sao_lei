from random import randint, choice
import pygame
from sys import exit
from time import sleep


pygame.init()
class 扫雷:

    def __init__(self, 地雷数=5, 地图大小=5) :
        self.hand_x = 0
        self.hand_y = 0
        self.live = True
        self.tnts = 地雷数
        self.tnt_rest = 0
        self.MapSize = 地图大小
        if self.tnts > self.MapSize**2 :
            self.tnts = self.MapSize**2*2//5
        self.map_out = [ [ '■' for i in range(self.MapSize+1) ] for j in range(self.MapSize+1) ]
        self.map_book = [ [ 0 for i1 in range(self.MapSize+1) ] for j1 in range(self.MapSize+1) ]
        self.map_tab = self.map_book.copy()
        self.next = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        while self.tnt_rest <= self.tnts:
            x = randint(0,self.MapSize-1)
            y = randint(0,self.MapSize-1)
            if self.map_book[x][y] != 9 :
                self.map_book[x][y] > 9
                for k in self.next:
                    tx = x + k[0]
                    ty = y + k[1]
                    try :
                        self.map_book[tx][ty] += 1
                    except IndexError:
                        pass
                self.tnt_rest += 1
    
    def dfs(self, x, y):
        sum = 5
        for k1 in range(8):
            tx = x + self.next[k1][0]
            ty = y + self.next[k1][1]
            if tx < 0 or ty > self.MapSize or ty < 0 or ty > self.MapSize or sum == 0 :
                continue
            if self.map_book == 0 and self.map_tab == 0 :
                sum -= 1
                self.map_out[tx][ty] = 0 
                self.map_tab = 1
                self.dfs(tx,ty)
            if self.map_book > 0 and self.map_tab == 0 :
                sum -= 1
                self.map_out[tx][ty] = self.map_book[tx][ty]
                self.map_tab[tx][ty] = 1
                self.dfs(tx, ty)
        return None
    
    def win(self):
        for i4 in range(self.MapSize):
            for j4 in range(self.MapSize):
                if self.map_book == 9 and self.map_out == "■":
                    print('you win !')
    
    def move(self):
        for events in pygame.event.get():
            if  events.type == pygame.KEYDOWN:
                if events.key == pygame.K_UP:
                    if self.hand_y == 0:
                        pass
                    else:
                        self.hand_y -= 1
                elif events.key == pygame.K_DOWN:
                    if self.hand_y == self.MapSize:
                        pass
                    else:
                        self.hand_y += 1
                elif events.key == pygame.K_LEFT:
                    if self.hand_x == 0:
                        pass
                    else:
                        self.hand_x -= 1
                elif events.key == pygame.K_RIGHT:
                    if self.hand_y == self.MapSize :
                        pass
                    else:
                        self.hand_y += 1
                elif events.key == pygame.K_SPACE:
                    if self.map_book[self.hand_y][self.hand_x] == 9:
                        self.live = False
                    else:
                        self.dfs(self.hand_x,self.hand_y)
            self.map_out[self.hand_y][self.hand_x] = '□'
            for y in range(self.MapSize):
                for x in range(self.MapSize):
                    print(self.map_out[y][x],end=' ')
                print()

    def main_game(self):
        while self.live :
            self.move()
            self.win()


if __name__ == "__main__" :
    size =  input('size:')
    tnts = input('tnt:')
    if size :
        if tnts :
            try:
                ai = 扫雷(int(tnts),int(size))
            except ValueError:
                ai = 扫雷()
                ai.main_game()
            finally :
                print('game start!')
                ai.main_game()
            
