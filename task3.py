from random import randint

num = randint(0, 1000)
count = 10

while count > 0:
    guess = int(input("Угадайте число от 0 до 1000: "))
    count -= 1

    if guess == num:
        print("Вы угадали! Число:", num)
        break
    elif guess < num:
        print("Загаданное число больше, осталось попыток:", count)
    else:
        print("Загаданное число меньше, осталось попыток:", count)

if count == 0:
    print("Вы проиграли. Было загадано число:", num)
