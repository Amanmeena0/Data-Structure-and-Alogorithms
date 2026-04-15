t = int(input())

for _ in range(t):
    N, M = map(int, input().split())


    decrease_in_degree = N - M

    print(decrease_in_degree*N)