class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==1:
            return True
        count=0    
        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                count +=1
        return count<= 1