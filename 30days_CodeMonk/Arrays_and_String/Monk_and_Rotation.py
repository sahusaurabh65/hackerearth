def monk_and_rotation():

    for i in range(int(input())):
      n,k=map(int,input().split())
      k = k % n
      ar = list(map(int, input().split()))
      ar=(ar[(n-k):n]+ar[:(n-k)])
      s=""
      for i in ar:
        if i!=",":
          s+=str(i)+" "
      print(s)


if __name__ == '__main__':
    monk_and_rotation()
