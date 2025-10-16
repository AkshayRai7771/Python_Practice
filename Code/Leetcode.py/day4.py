#shoeinventory question

from collections import Counter

X = int(input())
size = list(map(int, input().split()))
N = int(input())  

a = Counter(size)
print(a)

earned = 0

for _ in range(N):
    size1, price = map(int, input().split())
    print(size1,price)
    if a[size1] > 0:
        earned += price
        a[size1] -= 1  

print(earned)