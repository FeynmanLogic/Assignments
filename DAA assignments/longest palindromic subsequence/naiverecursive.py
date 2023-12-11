def is_palindrome(s):
    return s == s[::-1]

def longest_palindromic_subsequence_helper(s, i, j):
    if i == j:
        return s[i]
    if is_palindrome(s[i:j+1]):
        return s[i:j+1]
    left = longest_palindromic_subsequence_helper(s, i, j-1)
    right = longest_palindromic_subsequence_helper(s, i+1, j)
    if len(left) > len(right):
        return left
    else:
        return right

def longest_palindromic_subsequence(s):
    return longest_palindromic_subsequence_helper(s, 0, len(s)-1)
