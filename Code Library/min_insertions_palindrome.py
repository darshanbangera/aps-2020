from lcs import lcs

s = "HELLO"
x = lcs(s,s[::-1])
print(len(s)-x)
