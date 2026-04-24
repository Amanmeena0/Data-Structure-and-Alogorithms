from typing import List


class Solution:
    def maxlen1(self,arr:List[int])->int:
        n = len(arr)
        max_ele = 0
        for i in range(n):
            total_sum = 0
            for j in range(i, n):

                total_sum += arr[j]
                if total_sum == 0:
                    max_ele = max(max_ele, j - i + 1)

        return max_ele
    
    #using prefixSum 
    def maxLen(self,arr: List[int])->int:

        max_size = 0
        prefix_sum = 0
        freq = {}
        freq[0] = -1

        for i in range(len(arr)):
            prefix_sum += arr[i]

            if prefix_sum not in freq:
                freq[prefix_sum] = i
            
            curr_size = i - freq[prefix_sum] 

            max_size = max(max_size, curr_size)

        return max_size

def main():
    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))

    print(sol.maxLen(array))

    
if __name__ == "__main__":
    main()
