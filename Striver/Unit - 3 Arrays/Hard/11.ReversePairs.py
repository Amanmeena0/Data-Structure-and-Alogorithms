from typing import List

class Solution:
    # Different mergbe approach
    def reversePairs(self, nums: List[int]) ->int:
        return self.mergeSort(nums, 0, len(nums) - 1)
    
    def mergeSort(self, nums: List[int], low:int, high:int):

        count = 0
        if low < high:

            mid = (low + high) // 2 

            count += self.mergeSort(nums, low, mid)
            count += self.mergeSort(nums, mid+ 1, high)
            count += self.merge(nums, low , mid, high)
        return count 
    
    def merge(self, nums: List[int], low:int, mid:int, high:int):

        count = 0

        j = mid + 1

        for i in range(low , mid + 1):
            
            while j <= high and nums[i] < 2* nums[j]:

                j += 1
            count += j - (mid + 1)

        temp= []
        left = low 
        right = mid + 1

        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1
            
        while left <= mid:
            temp.append(nums[left])
            left += 1

        while right <= high:
            temp.append(nums[right])
            right += 1

        for i in range(len(temp)):
            nums[low + i] = temp[i]

        return count


        return count    
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