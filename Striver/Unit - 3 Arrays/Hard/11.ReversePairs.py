from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        res = [0]

        def merge(nums):
            
            n = len(nums)

            mid = n // 2

            if n == 1: return nums

            arrLeft = merge(nums[:mid])
            arrRight = merge(nums[mid:])

            nLeft, nRight =  mid, n - mid

            i, j = 0,0

            while i < nLeft:
                while j < nRight and arrLeft[i] > 2 * arrRight[j]: j += 1
                res[0] += j
                i += 1

            i, j = 0,0
            sortedArr = []

            while i < nLeft and j < nRight:
                if arrLeft[i] < arrRight[j]:
                    sortedArr.append(arrLeft[i])
                    i += 1
                else:
                    sortedArr.append(arrRight[j])
                    j += 1

            sortedArr.extend(arrLeft[i:])
            sortedArr.extend(arrRight[j:])

            return sortedArr
        
        merge(nums)

        return res[0]
def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    # k = int(input("Enter the number: "))
    print(sol.reversePairs(array))
    # sol.sortColors(array)
    # for i in array:
    #     print(i, end=" ")

if __name__ == "__main__":
    main()