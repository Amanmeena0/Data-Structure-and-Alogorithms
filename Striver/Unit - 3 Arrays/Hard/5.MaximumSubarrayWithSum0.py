from typing import List


class Solution:
    def maxlen(self,arr:List[int])->int:
        N = len(arr)
        positives = []
        negatives = []

        for num in arr:
            if num >= 0:
                positives.append(num)
            else:
                num < 0:
                negatives.append(num)
        


        total_sum = sum(positives)
        count = len(positives)
        return

def main():
    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))

    print(sol.maxlen(array))

    
if __name__ == "__main__":
    main()