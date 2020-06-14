class SeatArrangement:
    def __init__(self):
        num = int(input('numbers: '))
        self.num = num

    def SeatArrangement_main(self):
        for n in range(self.num):
            numbers = int(input())
            numbers_mod = numbers % 6
            seat = numbers % 12
            vals1 = { 1:11, 2:9, 3:7, 4: 5, 5: 3, 6: 1,
                      12:-11, 11:-9, 10:-7, 9:-5, 8:-3, 7:-1, 0:-11}
            if True:
                ad = vals1[seat]
                result  = (numbers + ad)
                if numbers_mod == 0 or numbers_mod == 1:
                    print (result,"WS")
                elif numbers_mod == 2 or numbers_mod== 5 :
                    print (result, "MS")
                elif numbers_mod == 3 or numbers_mod == 4 :
                    print (result,"AS")

if __name__ == '__main__':
    test = SeatArrangement()
    test.SeatArrangement_main()



