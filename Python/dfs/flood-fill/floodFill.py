
def floodFill(image, sr: int, sc: int, color: int):
    if image[sr][sc] == color:
        return image
    dfs(image, sr, sc, image[sr][sc], color)
    return image
def dfs(image, sr, sc, match, color):
    image[sr][sc] = color
    #left
    if sc-1 >= 0 and image[sr][sc-1] == match:
        dfs(image, sr, sc-1, match, color)
    #right
    if sc+1 < len(image[0]) and image[sr][sc+1] == match:
        dfs(image, sr, sc+1, match, color)
    #up
    if sr-1 >= 0 and image[sr-1][sc] == match:
        dfs(image, sr-1, sc, match, color)
    #down
    if sr+1 < len(image) and image[sr+1][sc] == match:
        dfs(image, sr+1, sc, match, color)

img = [[1,1,1],[1,1,0],[1,0,1]]

print(floodFill(img, 1, 1, 2))