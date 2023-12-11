def edit_distance(s1, s2):
    def helper(i, j):
        if i == 0:
            return j
        elif j == 0:
            return i
        elif s1[i-1] == s2[j-1]:
            return helper(i-1, j-1)
        else:
            return 1 + min(helper(i-1, j), helper(i, j-1), helper(i-1, j-1))
    return helper(len(s1), len(s2))
