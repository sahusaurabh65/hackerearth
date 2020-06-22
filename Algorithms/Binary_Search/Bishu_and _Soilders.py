# def maint():
#     n = int(input())
#     for i in range(n):
#         a = sorted(list(map(int, input().split())))
#         q = int(input())
#         q = q - 1
#         while q:
#             count = 0
#             sum_ = 0
#             r = int(input())
#             for j in range(n-1):
#                 if a[j]<= r:
#                     count = count + 1
#                     sum_ += sum_ + a[j]
#             q = q-1
#
#             print (sum_)
# if __name__ == '__main__':
#     maint()
#
#
#
#
#
#




# def binary_search(a,key ):
#     low = 0
#     high = len(a)-1
#     while low <= high :
#         mid = (low + high )/2
#         if (a[mid]==key):
#             ans  = mid + 1
#             low  = mid + 1
#         elif a[mid] > key:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return ans
#
# def bishu_soilders():
#     n = int(input('numbers: '))
#     for i in range (n):
#         a = sorted(list(map(int, input().split())))
#         q = int(input('numbers2: '))
#
#         while(q-1 > 0):
#             m  = int(input('numbers3: '))
#             print(m)
#             if a[n-1]<m:
#                 ans = m
#             elif (m < [0]):
#                 print ("0 0")
#                 continue
#             else:
#                 ans = binary_search(a ,key)
#             for i in range(ans-1):
#                 sum =+ a[i]
#             print (ans+ " "+sum)
#
#
# if __name__ == '__main__':
#     bishu_soilders()


