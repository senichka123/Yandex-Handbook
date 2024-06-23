N = int(input())    # количество продуктов

products = set()

for _ in range(N):
    products.add(input())

M = int(input())    # количество блюд

dishes = {}
for _ in range(M):
    title = input()
    dishes[title] = set()
    K = int(input())    # количество ингредиентов для блюда
    for _ in range(K):
        dishes[title].add(input())

is_cook_smth = 0
for key in sorted(dishes):
    if dishes[key] <= products:
        is_cook_smth = 1
        print(key)

if is_cook_smth == 0:
    print('Готовить нечего')