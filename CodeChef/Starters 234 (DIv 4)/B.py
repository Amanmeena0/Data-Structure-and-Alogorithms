t = int(input())

for _ in range(t):
    N, M = map(int, input().split())

    # brute force approach
    # decrease_in_degree = 0
    # for i in range(N, M, -1):
    #     decrease_in_degree  += i

    # print(decrease_in_degree)

    # optimized approach


    total_time = (N * (N + 1) // 2 ) - (M * (M+1) // 2)

    print(total_time)