'''
TRANSLATED FROM SPANISH TO ENGLISH WITH GOOGLE TRANSLATOR

You have a digital clock with 7 segment LEDs. One day, upon waking from a science fiction dream, you wonder: how many segments have been turned ON AFTER X seconds, from the 00:00: 00 position? Consider that, in every second, all the LEDs turn off and then the corresponding ones light up at the current moment. The program will ask how many seconds have elapsed and you will indicate how many LEDs were lit.


'''


import time


def findLEDS(sec, res):
    OnLed = 0
    for x in range(0, sec+1):
        ActualSecond = time.strftime('%H:%M:%S', time.gmtime(x))
        i = 0
        while(i < len(ActualSecond)):
            if(ActualSecond[i] == '1'):
                OnLed = 2
            elif(ActualSecond[i] == '2' or ActualSecond[i] == '3' or ActualSecond[i] == '5'):
                OnLed = 5
            elif(ActualSecond[i] == '4'):
                OnLed = 4
            elif(ActualSecond[i] == '6' or ActualSecond[i] == '9' or ActualSecond[i] == '0'):
                OnLed = 6
            elif(ActualSecond[i] == '7'):
                OnLed = 3
            elif(ActualSecond[i] == '8'):
                OnLed = 7
            elif(ActualSecond[i] == ':'):
                OnLed = 0
            res += OnLed
            i += 1
    return res


def main():
    res = 0
    check = False
    while (check == False):
        try:
            cantSec = int(input("Cuantos segundos pasaron: "))
            check = True
        except:
            print("No son segundos")
    res = findLEDS(cantSec, res)
    print("Leds encendidos:", res)


main()
