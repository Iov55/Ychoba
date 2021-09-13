b=int(input("Введите число: "))
while b<=0 or b>=0:
    if b==0:
        print("Число ровно нулю:", b)
        break
    elif b>=0:
        print("Положительное число:", b)
        break
    elif b<=0:
        print("Отрицательное число:", b)
        break
    else:
        print("eror")
3