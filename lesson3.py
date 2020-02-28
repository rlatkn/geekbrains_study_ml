""" Task 1 """


def func_1(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print('На ноль делить нельзя')


print(func_1(int(input('Введите число 1: ')), int(input('Введите число 2: '))))


""" Task 2 """


def func_2(name, surname, date, city, email, phone):
    print(f'name: {name}')
    print(f'surname: {surname}')
    print(f'date: {date}')
    print(f'city: {city}')
    print(f'email: {email}')
    print(f'phone: {phone}')


func_2(name='Roman', surname='Latkin', date='28.12.1991', city='Bali', email='roman@mail.ru', phone='+7911111111')


""" Task 3 """


def func_3(one, two, three):
    arr = [one, two, three]
    first_max = max(arr)
    arr.remove(first_max)
    second_max = max(arr)
    arr.remove(second_max)

    return first_max + second_max


print(func_3(3, 2, 10))


""" Task 4 """


def func_4(num, degree):
    return num ** degree


print(func_4(2, 4))


def func_4_2(num, degree):
    final_num = num
    for r in range(1, degree):
        print('final_num', final_num)
        final_num = final_num * num

    return final_num


print(func_4_2(2, 2))
print(func_4_2(3, 3))
print(func_4_2(5, 3))


""" Task 5 """


def func_5():
    total_sum = 0
    while True:
        arr = input('Type numbers throw the space: ').split(' ')
        is_exit = False

        for a in arr:
            try:
                total_sum += int(a)
            except ValueError:
                is_exit = True
                break

        print(total_sum)
        if is_exit:
            break


func_5()


""" Task 6 """


def int_func(string):
    return str(string).capitalize()


print(int_func('qwerty'))
print(' '.join((list(map(int_func, 'qwerty qwerty qwerty'.split())))))