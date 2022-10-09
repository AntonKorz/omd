def max_div3_sum(numbers: list) -> int:
    n = len(numbers)
    M = [[0 for j in range(0, n)] for i in range(0, 3)]
    for j in range(0, n):
        lst = [0, 0, 0]
        for i in range(0, 3):
            M[i][j] = M[i][j - 1]
            lst[i] = M[i][j]


        for i in range(0, 3):
            k = (M[i][j - 1] + numbers[j]) % 3
            lst[k] = max(M[i][j - 1] + numbers[j], M[k][j])

        M[0][j] = lst[0]
        M[1][j] = lst[1]
        M[2][j] = lst[2]

    return M[0][n - 1]


def solution():
    numbers = [int(x) for x in input().split()]
    result = max_div3_sum(numbers)
    print(result)


solution()


def max_div3_sum(numbers: list) -> int:
    n = len(numbers)
    M = [[0 for j in range(0, 3)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, 3):
            if i == 0:
                ost = numbers[i] % 3
                M[i][ost] = max(M[i][ost], numbers[i])
            else:
                ost = (M[i - 1][j] + numbers[i]) % 3
                M[i][ost] = max(M[i][ost], M[i - 1][j] + numbers[i])
                M[i][j] = max(M[i][j], M[i - 1][j])
    return M[n - 1][0]