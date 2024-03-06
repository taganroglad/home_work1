number = int(input('Введите число от 1 до 100 000: '))

if number < 1 or number > 100000:
    print('Число должно быть от 1 до 100 000')
else:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f'{number} - простое число')
    else:
        print(f'{number} - составное число')
