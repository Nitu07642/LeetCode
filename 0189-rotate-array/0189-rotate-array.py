class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        start=nums[0]
        end=nums[-1]
        def reverse(start:int,end:int)->None:
            while start<end:
                nums[start],nums[end]=nums[end],nums[start] 
                start+=1
                end-=1
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)  