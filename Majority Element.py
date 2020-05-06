class Solution:
    def majorityElement(self, nums):
        majority = len(nums) // 2 + 1
        counter = {}
        for number in nums:
            count = counter.get(number, 0) + 1
            if count == majority:
                return number
            counter[number] = count
