# # arr = list(map(int, input().split()))
# arr = [1, 3, 2, 1, 3]
# hash_arr = [0] * 13   # renamed to avoid confusion with built-in 'hash'

# for num in arr:
#     hash_arr[num] += 1

# q = int(input())

# for _ in range(q):
#     number = int(input())
#     print(hash_arr[number])


string = input().strip()

hash_arr = [0]*26

for c in string:
    hash_arr[ord(c) - ord('a')] += 1

q = int(input())

for _ in range(q):
    char = input().strip()
    print(hash_arr[ord(char) - ord('a')])