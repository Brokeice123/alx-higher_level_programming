#!/usr/bin/python3
"""
nqueens backtracking program to print the cordinates of n queens
on an n x n chessboard
"""


from sys import argv

if __name__ == "__main__":
    a = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    if not argv[1].isdigit():
        print("N must be a number")
        exit(1)

    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    for i in range(n):
        a.append([i, None])

    def already_exists(y):
        """Check that a queen does not already exist in that y value"""
        for x in range(n):
            if y == a[x][1]:
                return True
        return False

    def reject(x, y):
        """determines whether or not to reject the solution"""
        if (already_exists(y)):
            return False
        i = 0
        while(i < x):
            if abs(a[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_a(x):
        """clears the answers from the point of failure on"""
        for i in range(x, n):
            a[i][1] = None

    def nqueens(x):
        """backtracking function"""
        if x == n:
            print(a)
        else:
            for y in range(n):
                if reject(x, y):
                    a[x][1] = y
                    nqueens(x + 1)
                    clear_a(x)

    nqueens(0)
