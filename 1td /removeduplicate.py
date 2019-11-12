import unittest
class Solution:
    def removeDuplicates(self, nums):
        i=0
        for j in range(len(nums)-1):
            if nums[j]!=nums[j+1]:
                i+=1
                nums[i]=nums[j+1]            
        return i+1 if nums else 0

    def removeDuplicatesP1(self,nums):
        for i in range(len(nums),0,-1):
            if nums[i]==nums[i-1]:
                nums.pop(i)
        return len(nums)

    