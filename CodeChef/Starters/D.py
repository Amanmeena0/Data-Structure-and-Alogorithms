def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    A = list(map(int, data[2:2+N]))
    
    max_A = max(A)
    
    # Binary search for maximum D
    low, high = 0, max_A
    ans = 0
    
    while low <= high:
        mid = (low + high) // 2
        
        if mid == 0:
            # D=0 always possible
            total_people = 10**18  # big enough to ensure possible
        else:
            total_people = 0
            for units in A:
                total_people += units // mid
        
        if total_people >= M:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    
    print(ans)

if __name__ == "__main__":
    solve()