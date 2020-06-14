
def cost_ballon():
    for x in range(1,int(input())+1):
        result=[]
        p = list(map(int,input().split()))    # [9,6]

        if x >= 1 and x%2 == 0:
            p.reverse()

        for st in range(int(input())):
            flag = list(map(int,input().split()))  # [1,1]
            result.append(p[0] * flag[0])
            result.append(p[1] * flag[1])

        print(sum(result))

if __name__ == '__main__':
    cost_ballon()
