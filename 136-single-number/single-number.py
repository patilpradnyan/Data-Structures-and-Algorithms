class Solution(object):
    def singleNumber(self, nums):
        solo = 0

        for vibe in nums:
            solo ^= vibe

        return solo