from random import randint, choice


class 扫雷:
    def __init__(self, 地雷数=10, 地图大小=5) :
        self.tnts = 地雷数
        self.tnt_rest = 0
        self.MapSize = 地图大小
        if self.tnts > self.MapSize**2 :
            self.tnts = self.MapSize**2*2//5
        self.map_out = [ [ '■' for i in range(self.MapSize) ] for j in range(self.MapSize) ]
        self.map_book = [ [ 0 for i1 in range(self.MapSize) ] for j1 in range(self.MapSize) ]
        self.map_tab = self.map_book.copy()
        self.next = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        while self.tnt_rest <= self.tnts:
            x = randint(0,5)
            y = randint(0,5)
            if self.map_book[x][y] != 9 :
                self.map_book[x][y] = 9
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
