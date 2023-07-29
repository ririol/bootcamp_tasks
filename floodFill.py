class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = image[sr][sc]
        visited = []
        stack = [[sr,sc]]
        change = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while stack:
            y, x = stack.pop()
            visited.append([y, x])
            for dy, dx in change:
                if not 0 <= y + dy <= len(image)-1: continue        # check y index
                if not 0 <= x + dx <= len(image[0])-1: continue     # check x index
                if not (image[y + dy][x + dx] == start): continue   # check color
                if [y + dy,x + dx] in visited: continue             # check if visited
                stack.append([y + dy,x + dx]) 
            
        for y,x in visited:
            image[y][x] = color
            
        return image