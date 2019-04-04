from module import *

a = 2
while True:
    print("Menu")
    print("---------")
    print("1: add")
    print("2: sub")
    print("3: multiply")
    print("4: divide")
    print("5: stop")
    a = int(input())
    
    if a == 5:
        break

    if a > 5:
        print("제대로 입력하세요")
        continue

    first = int(input("num1: "))
    second = int(input("num2: "))
    cal = Fourcal(first,second)
    
    if a == 1:
        print(cal.add())
    
    elif a == 2:
        print(cal.sub())

    elif a == 3:
        print(cal.mul())

    elif a == 4:
        if second == 0:
            print("문과세요?ㅡㅡ 사실 저도 문과에요 ㅠㅠ")
        else:
            print(cal.div())
