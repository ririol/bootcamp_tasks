def floodFill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    start = image[sr][sc]
    visited = []
    stack = [[sr,sc]]
    change = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while stack:
        y, x = stack.pop()
        visited.append([y, x])
        for dy, dx in change:
            if not y + dy >= 0 or not y + dy <= len(image)-1: continue
            if not x + dx >= 0 or not x + dx <= len(image[0])-1: continue
            if not (image[y + dy][x + dx] == start) or [y + dy,x + dx] in visited: continue           
            stack.append([y + dy,x + dx])
    
    for y,x in visited:
        image[y][x] = color
        
    return image

