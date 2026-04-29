from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(nums,target, is_searching_left):

            low = 0
            high = len(nums) -1
            idx = -1

            while low <= high:

                mid = (low + high) // 2

                if nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:

                    idx = mid

                    if is_searching_left:
                        high = mid - 1
                    else:
                        low = mid + 1

            return idx
    
        left = binary_search(nums, target, True)
        right = binary_search(nums, target, False)


        return [left, right]

                        

                

        return [-1,-1]
def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    k = int(input("Enter the number: "))
    print(sol.search(array,k))
    # sol.sortColors(array)
    # for i in array:
    #     print(i, end=" ")

if __name__ == "__main__":
    main()