# ! usr/bin/python
# File Name : shortest_route.py
__author__ = 'Tips'

def shortest_distance(grid):
    m = len(grid)

    # [] boundary cases
    if m == 0:
        return 0
    n = len(grid[0])

    # [[][][]] boundary cases
    if n == 0:
        return 0

    # normal cases
    # initialize the dp matrix to accept the answer in each steps
    dp = [[0] * n for _ in range(m)] # the same size with the gird m * n
    
    # dp: find a function to inference from the previous step to the present step
    for i in range(m):
        for j in range(n):
            if i == j == 0:
                # the first number
                dp[i][j] = grid[i][j]
            elif i == 0:
                # i ==0 and j != 0
                dp[i][j] = grid[i][j] + dp[i][j-1]
            elif j == 0:
                # i != 0 and j == 0
                dp[i][j] = grid[i][j] + dp[i-1][j]
            else:
                # i !=0 and j != 0
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

    return dp


if __name__ == '__main__':
    grid = [[1, 4, 1],
            [2, 0, 1],
            [7, 9, 1]]
    # find the shortest distance from upper left to lower right
    dp = shortest_distance(grid)
    print(dp)