# Code created by Romain Fouilland for problem:
# https://www.codechef.com/ZCOPRAC/problems/ZCO15001

# Dynamic programming on input list C of N numbers
# a[i, j] = min nb of cuts to have a sequence of palindromes from C[i: i+j included]
# For all i, | a[i, 0] = 1
#            | a[i, j+1] = | 1 if C[i: i+j+1 included] is a palindrome
#                          | min on 0<=k<=j of (a[i, k] + a[i+k+1, j-k])
# Return a[0, N-1]
# Complexity = O(N^3)


from numpy import ones


def is_palindrome(l):
    for i in range(len(l) // 2):
        if l[i] != l[-1-i]:
            return False
    return True


n = int(input())
numbers = list(map(int, str.split(input())))
a = ones((n, n))

for j in range(n-1):
    for i in range(n):
        if not is_palindrome(numbers[i: i+(j+1)+1]):
            if i + j + 1 < n:
                a[i, j + 1] = min([a[i, k] + a[i+k+1, j-k] for k in range(j+1)])
            else:
                # We reached the end of the table -> the right part of the cut is smaller
                a[i, j + 1] = min([a[i, k] + a[i+k+1, (n-1-i)-k] for k in range(n-i-1)])

print(int(a[0, n-1]))
