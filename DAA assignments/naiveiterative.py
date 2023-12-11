def is_palindrome(s):
    return s == s[::-1]

def longest_palindromic_subsequence(s):
    n = len(s)
    longest = ""
    
    
    for i in range(n):
        for j in range(i, n):
            if is_palindrome(s[i:j+1]):
                if len(s[i:j+1]) > len(longest):
                    longest = s[i:j+1]
    return longest
x=input("enter string:")
ans=longest_palindromic_subsequence(x)
print(ans)
