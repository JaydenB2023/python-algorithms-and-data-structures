## Applied Algorithms: 35290
## Programming Assignment 3
## Jayden Brown

def lcs(X, Y):
    m = len(X)
    n = len(Y)

    # Create the dynamic programming table
    dp = []

    for i in range(m + 1):
        row = [0] * (n + 1)
        dp.append(row)

    # Fill the dynamic programming table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Work backwards through the table to find the subsequence
    i = m
    j = n
    subsequence = []

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            subsequence.append(X[i - 1])
            i -= 1
            j -= 1

        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1

        else:
            j -= 1

    # Elements were found backwards
    subsequence.reverse()

    return subsequence


# Test 1
X = ["A", "B", "C", "B", "D", "A", "B"]
Y = ["B", "D", "C", "A", "B", "A"]

result = lcs(X, Y)
print("Test 1:", result)


# Test 2
X = [1, 0, 0, 1, 0, 1, 0, 1]
Y = [0, 1, 0, 1, 1, 0, 1, 1, 0]

result = lcs(X, Y)
print("Test 2:", result)