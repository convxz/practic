def max_score(N, M, field):
    dp = [[[-1, -1] for _ in range(M)] for _ in range(N)]

    # Инициализация dp[i][j][0]
    for i in range(N):
        for j in range(M):
            if field[i][j] == '0':
                dp[i][j][0] = 0
            elif field[i][j] == 'A':
                if i > 0:
                    dp[i][j][0] = 1 + dp[i-1][j][0]
                else:
                    dp[i][j][0] = 1
            elif field[i][j] == 'B':
                if i > 0:
                   dp[i][j][0] = dp[i-1][j][0]

    # Заполнение dp[i][j][1]
    for i in range(N):
        for j in range(M):
            if field[i][j] == '0':
                if j > 0:
                    dp[i][j][1] = dp[i][j-1][0]
                else:
                    dp[i][j][1] = 0
            elif field[i][j] == 'A':
                if i > 0 and j > 0:
                    dp[i][j][1] = 1 + max(dp[i][j-1][0], dp[i-1][j][1])
                elif i > 0:
                    dp[i][j][1] = 1 + dp[i-1][j][1]
                elif j > 0:
                    dp[i][j][1] = 1 + dp[i][j-1][0]
                else:
                    dp[i][j][1] = 1
            elif field[i][j] == 'B':
                if i > 0 and j > 0:
                    dp[i][j][1] = max(dp[i][j-1][0], dp[i-1][j][1])
                elif i > 0:
                    dp[i][j][1] = dp[i-1][j][1]
                elif j > 0:
                    dp[i][j][1] = dp[i][j-1][0]
                else:
                    dp[i][j][1] = 0

    max_score = 0
    for i in range(N):
        for j in range(M):
            max_score = max(max_score, dp[i][j][0], dp[i][j][1])

    return max_score

# Чтение входных данных
N, M = 3, 3
field = [[0, "B", 0], ["B", 0, "B"], [0, "B", 0]]
# for _ in range(N):
#     row = input()
#     field.append(row)

# Вызов функции и вывод результата
result = max_score(N, M, field)
print(result)
