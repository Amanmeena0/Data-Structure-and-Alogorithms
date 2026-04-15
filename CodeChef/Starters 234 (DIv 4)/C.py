def maximum_subsequence(Array):

    positives = []
    negatives = []

    for num in Array:

        if num >= 0:
            positives.append(num)
        else:
            negatives.append(num)

    total_sum = sum(positives)
    count = len(positives)

    negatives.sort(reverse=True)

    for num in negatives:
        if total_sum + num >= 0:
            total_sum += num
            count += 1
        else:
            break

    return count

def maximum_subsequence(arr):

    arr.sort(reversed=True)

    total = 0
    count = 0

    for num in arr:

        if total + num >= 0:
            total =+ num 
            count += 1
        else:
            break

    return count




t = int(input())
for _ in range(t):
    N = int(input())
    Array = list(map(int, input().split()))

    print(maximum_subsequence(Array))