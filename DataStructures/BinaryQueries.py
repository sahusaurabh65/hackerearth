def binary_queries():
    arr = [int(i) for i in input().split()]
    print (arr)
    for i in range(arr[0]):
        numbers = list(map(int,input().split()))
        print (numbers)
    while (arr[1]):
        x = int(input())
        if x==0:
            l,r = int(input()),int(input())
            if arr[r-1] == 0:
                print ("EVEN","\n")
            else:
                print("ODD", "\n")
        else:
            pos = int(input())
            if arr[pos-1] == 1:
                arr[pos - 1] = 0
            else :
                arr[pos - 1] = 1


if __name__ == '__main__':
    binary_queries()
