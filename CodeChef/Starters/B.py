# Read number of test cases
T = int(input())

for _ in range(T):
    N = int(input())
    
    A = list(map(int, input().split()))
    
    max_temp = max(A)
    min_temp = min(A)
    
    count = 0
    for temp in A:
        if temp != max_temp and temp != min_temp:
            count += 1
    
    print(count)