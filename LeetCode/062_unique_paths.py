def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    if m == 0 or n == 0:
        return 0
    if m == 1 or n == 1:
        return 1
    array = [[0 for col in range(m)] for row in range(n)] 
    for j in range(m):
        array[0][j] = 1
    for i in range(n):
        array[i][0] = 1
    for i in range(n-1):
        i += 1
        for j in range(m-1):
            j += 1
            array[i][j] = array[i-1][j] + array[i][j-1]
    return array[n-1][m-1]

if __name__ == "__main__":
    print(uniquePaths(3,2))