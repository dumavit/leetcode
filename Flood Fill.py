class Solution:
    def floodFill(self, image, sr, sc, newColor):
        n, m = len(image), len(image[0])
        visited = set()
        oldColor = image[sr][sc]
        queue = [(sr, sc)]
        while queue:
            y, x = queue.pop(0)
            visited.add((y,x))
            image[y][x] = newColor
            if y > 0 and image[y-1][x] == oldColor and (y-1, x) not in visited:
                queue.append((y-1, x))
            if x > 0 and image[y][x-1] == oldColor and (y, x-1) not in visited:
                queue.append((y, x-1))
            if y + 1 < n and image[y+1][x] == oldColor and (y+1, x) not in visited:
                queue.append((y+1, x))
            if x+1 < m and image[y][x+1] == oldColor and (y, x+1) not in visited:
                queue.append((y, x+1))
        return image


print(Solution().floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
# The length of image and image[0] will be in the range [1, 50].
# The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
# The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
