from collections import Counter
secret = "8701"
guess  = "0718"
s, g = Counter(secret), Counter(guess)
a = sum(i == j for i , j in zip(secret, guess))
return "%sA%sB" %(a, sum((s & g).values()) - a)

for i , j in zip(secret, guess)
    print i
