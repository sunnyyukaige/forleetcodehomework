class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        for i in range(len(nums)-k):
            nums.append(nums[0])
            nums.pop(0)      
        return nums

    def rotateP1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        nums[::]=nums[-k:]+nums[:-k]
        return nums