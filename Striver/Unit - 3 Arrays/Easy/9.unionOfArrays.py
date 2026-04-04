from typing import List

class Solution:

    #brute force approach 
    def unionArray(self, nums1: List[int], nums2:list[int]) -> List[int]:


        union = []
        i , j= 0 ,0 

        while i < len(nums1) and j < len(nums2):

            if nums1[i] < nums2[j]:
                if len(union) == 0 or union[-1] != nums1[i]:
                    union.append(nums1[i])
                i+=1
            elif nums1[i] > nums2[j]:
                if len(union) == 0 or union[-1] != nums2[j]:
                    union.append(nums2[j])
                j+=1
            else:  # nums1[i] == nums2[j]
                if not union or union[-1] != nums1[i]:
                    union.append(nums1[i])
                i += 1
                j += 1

        while i < len(nums1):
            if union[-1] != nums1[i]:
                union.append(nums1[i])
            i +=1 
        while j < len(nums2):
            if union.append(nums2[j]):
                union.append(nums2[j])
            j +=1 
        
        return union
            
def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    nums = list(map(int, input("Enter number for second array: ").split()))
                
    print(sol.unionArray(array,nums))
    

if __name__ == "__main__":
    main()