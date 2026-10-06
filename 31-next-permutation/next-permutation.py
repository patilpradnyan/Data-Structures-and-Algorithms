class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None
        """

        # Step 1: pivot/sus dhoondo
        left = len(nums) - 2

        while left >= 0 and nums[left] >= nums[left + 1]:
            left -= 1

        # Step 2: agar sus mila
        if left >= 0:
            right = len(nums) - 1

            while nums[right] <= nums[left]:
                right -= 1

            # dono ki vibe swap
            nums[left], nums[right] = nums[right], nums[left]

        # Step 3: remaining part ko reverse karo
        right = len(nums) - 1

        while left + 1 < right:
            nums[left + 1], nums[right] = nums[right], nums[left + 1]
            left += 1
            right -= 1