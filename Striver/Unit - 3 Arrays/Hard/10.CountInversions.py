from typing import List

class Solution:
    # 1D - Array
    # brute force approach
    # def numberOfInversions1(self, nums: list[int]) -> int:
        
    #     Inversion = 0
    #     n = len(nums)
    #     for i in range(i):

    #         for j in range(i + 1):

    #             if nums[j] > nums[i]:

    #                 Inversion += 1
 
    #     return Inversion
    
    # 1D - Array 
    # Merge Sort Based - Optimal Approach
    def merge(self, arr, low , mid , high):
        temp = []

        left = low 
        right = mid + 1

        cnt = 0

        while left <= mid and right <= high:

            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                cnt += (mid - left + 1)
                right +=1 

        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1
        
        for i in range(low, high + 1):
            arr[i] = temp[i - low]

        return cnt

    def mergeSort(self, arr, low , high):
        cnt = 0

        if low >= high:
            return cnt 
        
        mid = (low + high) // 2

        cnt += self.mergeSort(arr, low, mid)

        cnt += self.mergeSort(arr, mid + 1, high)

        cnt += self.merge(arr, low, mid, high)

        return cnt
    
    def numberOfInversions(self, nums: list[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)
        
def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    # k = int(input("Enter the number: "))
    print(sol.numberOfInversions(array))
    # sol.sortColors(array)
    # for i in array:
    #     print(i, end=" ")

if __name__ == "__main__":
    main()