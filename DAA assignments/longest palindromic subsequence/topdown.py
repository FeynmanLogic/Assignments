def longest_palindromic_subsequence_helper(s, i, j, memo):
    if i == j:
        return s[i]
    if (i, j) in memo:
        return memo[(i, j)]
    if s[i] == s[j]:
        memo[(i, j)] = s[i] + longest_palindromic_subsequence_helper(s, i+1, j-1, memo) + s[j]
    else:
        left = longest_palindromic_subsequence_helper(s, i, j-1, memo)
        right = longest_palindromic_subsequence_helper(s, i+1, j, memo)
        if len(left) > len(right):
            memo[(i, j)] = left
        else:
            memo[(i, j)] = right
    return memo[(i, j)]

def longest_palindromic_subsequence(s):
    memo = {}
    return longest_palindromic_subsequence_helper(s, 0, len(s)-1, memo)
s=input("enter sting:")
ans=longest_palindromic_subsequence(s)
print(ans)