t = int(input())
for _ in range(t):
    N = int(input())
    
    zeros = N // 2 + N % 2
    ones = N // 2 

    print('0' * zeros + '1' + ones) 
    