# Code Signal Solutions
# Arrays - rotateImage
# Jaedin Davasligil (2024)

# PROBLEM
# You are given an n x n 2D matrix that represents an image. Rotate the image
# by 90 degrees (clockwise).

# SOLUTION
# We notice that the image can be rotated by transposing the matrix and then
# reversing each row.
def solution(a):
    n = len(a)
    tmp = 0

    # Iterate over the upper triangle to transpose the matrix.
    for r in range(n - 1):
        for c in range(1 + r, n):
            tmp = a[r][c]
            a[r][c] = a[c][r]
            a[c][r] = tmp
    
    # Reverse each row.
    for r in range(n):
        a[r] = a[r][::-1]
    
    return a

# TESTS
def test_solution():
    a = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

    assert solution(a) == [[7, 4, 1],
                           [8, 5, 2],
                           [9, 6, 3]]

    print("Tests completed.")

# MAIN
if __name__ == "__main__":
    test_solution()
