import sys
"""
    1st approach: BFS
    - we need a 2D array to cache the min distance on each cell !!!!
    - if the ball hits the wall, try to roll in 4 directions until the explorations hit the wall
    - only cache the pivot points where we turned(in front of the wall)

    Time    O(RCmax(R,C)) for every point, we can traverse up to R or C depth
    Space    O(RC)
    424 ms, faster than 20.13%
"""


class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        # left, right, up, down
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        # destination
        destI, destJ = destination[0], destination[1]
        # save shortest distance
        visited = []
        for _ in range(len(maze)):
            visited.append(len(maze[0]) * [sys.maxsize])

        q = []
        q.append((start[0], start[1], 0))

        while len(q) > 0:
            i, j, steps = q.pop(0)
            # stop the traversal if the steps >= visited[i][j]
            if steps >= visited[i][j]:
                continue
            # update visited[i][j]
            visited[i][j] = min(visited[i][j], steps)
            # stop if arrived
            if i == destI and j == destJ:
                continue
            # since we are at the walls, we can traverse every direction
            for di, dj in dirs:
                # roll the ball until it hits a wall
                row = i
                col = j
                newSteps = steps
                while 0 <= row + di < len(maze) and 0 <= col + dj < len(maze[0]) and maze[row+di][col+dj] == 0:
                    row += di
                    col += dj
                    newSteps += 1
                # enqueue
                q.append((row, col, newSteps))
        if visited[destI][destJ] == sys.maxsize:
            return -1
        return visited[destI][destJ]


a = [
    [1, 0, 1],
    [1, 0, 1],
    [0, 0, 0],
]
b = [0, 1]
c = [2, 2]
print(Solution().shortestDistance(a, b, c))

a = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
]
b = [0, 4]
c = [4, 4]
print(Solution().shortestDistance(a, b, c))

a = [
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
]
b = [0, 4]
c = [4, 4]
print(Solution().shortestDistance(a, b, c))

a = [
    [0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
]
b = [0, 4]
c = [4, 4]
print(Solution().shortestDistance(a, b, c))

print("-----")

"""
    2nd approach: DFS
    - we need a 2D array to cache the min distance on each cell !!!!
    - if the ball hits the wall, try to roll in 4 directions until the explorations hit the wall
    - only cache the pivot points where we turned(in front of the wall)

    Time     O(RCmax(R,C)) for every point, we can traverse up to R or C depth
    Space    O(RC)
    LTE
"""


class Solution(object):

    def __init__(self):
        self.visited = []

    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        # destination
        destI, destJ = destination[0], destination[1]
        # save shortest distance
        for _ in range(len(maze)):
            self.visited.append(len(maze[0]) * [sys.maxsize])

        self.dfs(maze, start[0], start[1], 0, destI, destJ)
        if self.visited[destI][destJ] == sys.maxsize:
            return -1
        return self.visited[destI][destJ]

    def dfs(self, maze, i, j, steps, destI, destJ):
        # stop the traversal if the steps >= visited[i][j]
        if steps >= self.visited[i][j]:
            return
        # update visited[i][j]
        self.visited[i][j] = min(self.visited[i][j], steps)
        # stop if arrived
        if i == destI and j == destJ:
            return
        # left, right, up, down
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for di, dj in dirs:
            # roll the ball until it hits a wall
            row = i
            col = j
            newSteps = steps
            while 0 <= row+di < len(maze) and 0 <= col+dj < len(maze[0]) and maze[row+di][col+dj] == 0:
                row += di
                col += dj
                newSteps += 1
            self.dfs(maze, row, col, newSteps, destI, destJ)


a = [
    [1, 0, 1],
    [1, 0, 1],
    [0, 0, 0],
]
b = [0, 1]
c = [2, 2]
print(Solution().shortestDistance(a, b, c))

a = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
]
b = [0, 4]
c = [4, 4]
print(Solution().shortestDistance(a, b, c))

a = [
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
]
b = [0, 4]
c = [4, 4]
print(Solution().shortestDistance(a, b, c))

a = [
    [0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
]
b = [0, 4]
c = [4, 4]
print(Solution().shortestDistance(a, b, c))
