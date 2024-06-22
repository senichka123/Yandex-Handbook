N = int(input())

massive = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']

for i in range(N):
    print(massive[i % 5])