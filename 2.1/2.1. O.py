N = int(input())
M = int(input())
T = int(input())

unit_time_min = N * 60 + M + T
N_new = unit_time_min // 60 % 24
M_new = unit_time_min % 60
print(f'{N_new:0>2}:{M_new:0>2}')
