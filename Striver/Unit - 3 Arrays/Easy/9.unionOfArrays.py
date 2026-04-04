from typing import List

class Solution:

    #brute force approach 
    def unionArray(self, nums1: List[int], nums2:list[int]) -> List[int]:


        Union = []
        i , j= 0 ,0 

        while i < len(nums1) and j < len(nums2):

            if nums1[i] < nums2[j]:
                Union.insert(nums1[i])
                i+=1
            elif nums1[i] > nums2[j]:
                Union.insert(nums2[j])
                j+=1
            elif nums1[i] == nums2[j]:
                Union.nums1[i]
                i += 1
                j += 1
        
        


        return Union
            
def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    nums = list(map(int, input("Enter number for second array: ").split()))
                
    print(sol.unionArray(array,nums))
    

if __name__ == "__main__":
    main()