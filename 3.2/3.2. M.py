N = int(input())

can_cook = set()

for _ in range(N):
    dish = input()
    can_cook.add(dish)

cooked = set()

M = int(input())
for _ in range(M):
    K = int(input())
    for _ in range(K):
        dish = input()
        if dish not in cooked:
            cooked.add(dish)

if can_cook == cooked:
    print('Готовить нечего')
else:
    for each in sorted(can_cook - cooked):
        print(each)