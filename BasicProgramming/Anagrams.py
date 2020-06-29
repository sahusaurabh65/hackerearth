test_case =  int (input(""))
for i in range(test_case):
    str1 = list(input(''))
    str2 = list(input(''))
    for j in str1[:]:
        if j in str2:
            str1.remove(j)
            str2.remove(j)
    print (len(str1)+len(str2))

