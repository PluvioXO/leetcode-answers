class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = [] 
        rotten, normal = set(), set()
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 2: 
                    rotten.add((y,x))
                elif grid[y][x] == 1:
                    normal.add((y,x))
        if not rotten:
            if not normal:
                return 0
            return -1 
        if not normal:
            return 0 
        # we have now indexed the entire map; 
        c = 0 
        while len(normal) > 0 and len(rotten) > 0:
            nRotten = set()
            print(rotten, normal)
            for i in list(rotten):
                y,x = i
                if (y+1, x) in normal:
                    nRotten.add((y+1, x))
                    normal.remove((y+1, x))
                if (y-1, x) in normal:
                    nRotten.add((y-1, x))
                    normal.remove((y-1,x))
                if (y, x+1) in normal:
                    nRotten.add((y, x+1))
                    normal.remove((y,x+1))
                if (y, x-1) in normal: 
                    nRotten.add((y, x-1))
                    normal.remove((y,x-1))
            if not nRotten:
                return -1; 
            rotten = nRotten; 
            c+=1
        return c
        
