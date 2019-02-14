def checkio(matrix):
    N = len(matrix)
    def seq_len(x, y, dx, dy, num):
        if 0 <= x < N and 0 <= y < N and matrix[y][x] == num:
            return 1 + seq_len(x + dx, y + dy, dx, dy, num)
        else:
            return 0
    DIR = [(0,1), (1,-1), (1,0), (1,1)]
    for y in range(N):
        for x in range(N-3):
            for dx, dy in DIR:
                if seq_len(x, y, dx, dy, matrix[y][x]) >= 4:
                    return True
    return False
