def palindrome_number(x):
    n = ''.join(filter(str.sialnum, s.lower()))
    return n == n[::-1]