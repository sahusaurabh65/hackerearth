lst = []
N = int(input())
A = list(map(int, input().split()))
sum_A = sum(A)
for j in A:
    if (sum_A-j) % 7 == 0:
        lst.append(j)
if len (lst)==0:
    print("-1")
else:
    print(A.index(min(lst)))