class FindProduct:
    def __init__(self):
        self.numbers = 1
        num = int(input('numbers: '))
        self.num = num

    def FindProduct_main(self):
        si_num = [int(i) for i in input().split()]
        numbers =self.numbers
        for i in si_num:
            numbers  = (numbers * int(i)) % ((10 ** 9)+7)
        print(numbers)

if __name__ == '__main__':
    test = FindProduct()
    test.FindProduct_main()