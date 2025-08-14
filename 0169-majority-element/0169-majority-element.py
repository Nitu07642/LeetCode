class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        majority=None
        for i in nums:
            if count==0:
                majority=i
            if i==majority:
                count+=1
            else:
                count-=1
        return majority                