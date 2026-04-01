from sys import stdin
from collections import defaultdict

input = stdin.read
data = input().split()
t = int(data[0])
idx = 1
results = []

for _ in range(t):
    n = int(data[idx]); idx += 1
    arr = list(map(int, data[idx:idx+n])); idx += n
    
    freq = defaultdict(int)
    for i in range(n):
        # B[i] = arr[i] - (i+1) because we use 1-based indexing for i
        freq[arr[i] - (i+1)] += 1
    
    ans = 0
    for val in freq.values():
        ans += val * (val - 1) // 2
    
    results.append(ans)

print("\n".join(map(str, results)))