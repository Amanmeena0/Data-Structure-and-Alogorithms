N, K = map(int, input().split())

cost_without_bribe = (100 * N)

cost_with_bribe = K + (50 * N)


print( min(cost_with_bribe, cost_without_bribe))
