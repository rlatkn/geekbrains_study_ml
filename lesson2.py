# 1

# list1 = [1, '2', 3.3, (1, 2), {1: 1, 2: 2}, [1, 2, 3]]
#
# for i in list1:
#     print(i, type(i))

# 2 Не понял
# 3 Слишком просто
# 4
# str1 = input('Введите строку: ')
# arr1 = str1.split(' ')
#
# print(enumerate(arr1, 1))
# for i, a in enumerate(arr1, 1):
#     print(i, a[:10])

# 5
# rating = []
# while True:
#     num = int(input('Введите число: '))
#     if rating.count == 0:
#         rating.append(num)
#         continue
# 
#     if num in rating:
#         rating.insert(rating.index(num), num)
# 
#     else:
#         rating.insert(0, num)
# 
#     print('rating', rating)

# 6
items = [
(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
(2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}), 
(3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
]
analytic = {}

for i in items:
    for key, value in i[1].items():
        if key not in analytic.keys():
            analytic[key] = set()

        analytic[key].add(value)

print(analytic)
