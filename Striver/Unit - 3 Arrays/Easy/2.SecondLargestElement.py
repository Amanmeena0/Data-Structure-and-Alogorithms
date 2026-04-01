class Solutuon:
    # Basic sorting approch
    def SecondLargestElement1(self,nums, n):
        
        nums.sort()
        second = 0
        for i in range(n - 2, -1 ,- 1):
            if nums[i] != nums[n-1]:
                return nums[i]
            
        return -1

    # Two Pass Approch
    def SecondLargestElement2(self,nums, n):
        
        largest = -1
        secondlargest = -1

        for i in range(n):
            if nums[i] > largest:
                largest = nums[i]

        for i in range(n):
            if nums[i] > secondlargest and nums[i] != largest:
                secondlargest = nums[i]
        
        return secondlargest


    # One Pass  Approch 
    def SecondLargestElement3(self,nums, n):
        largest = -1
        secondLargest = -1

        for i in range(n):

            if nums[i] > largest:
                secondLargest = largest
                largest = nums[i]

            elif nums[i] < largest and nums[i] > secondLargest:
                secondLargest = nums[i]

        return secondLargest


def main():

    sol = Solutuon()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    n = len(array)
    print(sol.SecondLargestElement3(array, n))

if __name__ == "__main__":
    main()


# class Solutuon:
#     def SecondLargestElement(self,nums, n):
        
        
        

#         return 
# def main():

#     sol = Solutuon()
#     array = list(map(int, input("Enter numbers separated by spaces: ").split()))
#     n = len(array)
#     print(sol.laSecondLargestElementgestElement(array, n))

# if __name__ == "__main__":
#     main()

