def longest_palindromic_subsequence(s):
    n = len(s)
    # create an n x n table to store the lengths of palindromic subsequences
    L = [[0] * n for _ in range(n)]
    # fill in the diagonal with 1's
    for i in range(n):
        L[i][i] = 1
    # fill in the table bottom-up
    for cl in range(2, n+1):
        for i in range(n-cl+1):
            j = i+cl-1
            if s[i] == s[j] and cl == 2:
                L[i][j] = 2
            elif s[i] == s[j]:
                L[i][j] = L[i+1][j-1] + 2
            else:
                L[i][j] = max(L[i+1][j], L[i][j-1])
    # construct the longest palindromic subsequence from the table
    longest = ""
    i, j = 0, n-1
    while i <= j:
        if s[i] == s[j]:
            longest += s[i]
            i += 1
            j -= 1
        elif L[i+1][j] > L[i][j-1]:
            i += 1
        else:
            j -= 1
    return longest
s='madam'
ans=longest_palindromic_subsequence(s)
print(ans)