class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        if len(nums)==0:
            return i
        for j in range(len(nums)-1):
            if nums[j]!=nums[j+1]:
                i+=1
                nums[i]=nums[j+1]            
        return i+1

    def removeDuplicatesP1(self,nums):
        