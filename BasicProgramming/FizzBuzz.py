import random

def fizz_buzz():
    n = int(input())
    lst = [int(i) for i in input().split()]
    for j  in range (len(lst)):
        for i in range(1,lst[j]):
            if i%15==0:
                print("FizzBuzz")
                continue
            elif i%5==0:
                print("Buzz")
                continue
            elif i % 3==0:
                print ("Fizz")
                continue
            else:
                print (i)
                continue


if __name__ == '__main__':
    fizz_buzz()