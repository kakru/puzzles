def deletion_distance(str1, str2):
    len1, len2 = len(str1), len(str2)
    if len1 == 0: return len2
    elif len2 == 0: return len1
    dp = [[0]*(len2+1) for _ in range(len1+1)]
    for i in range(len1+1):
        for j in range(len2+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
    return dp[len1][len2]


print(deletion_distance("dog", "frog"))