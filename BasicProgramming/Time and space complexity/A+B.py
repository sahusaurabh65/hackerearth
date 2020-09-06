# def round(n, n1):
#     # Smaller multiple
#     a = (n // 10) * 10
#
#     # Larger multiple
#     b = a + 10
#
#     # Return of closest of two
#     return (b if n - a >= b - n else a)
#
#
# def round2(n, n1):
#     # Smaller multiple
#     a = (n // 10) * 10
#
#     # Larger multiple
#     b = a + 10
#
#     # Return of closest of two
#     return (b if n - a >= b - n else a)
#
# # driver code
# n = 240300
# n1 = 10^n
ans = 240000
# # print(round(n, n1))
# print(round2(n,n1))
import re
dict = {1: ":)" ,2: ":-)"}
for i,j in dict.items():
    print (i,j)
    mystr = "hi!howare is you 1 :) "
    match = re.search((r'\b ":)" \b'), mystr)
    print(match)

