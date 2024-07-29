#link to problem https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for number in nums[::-1]:
            if number == val:
                nums.remove(val)
        k = len(nums)
        return k,nums

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        counter_index = 1
        for index in range(1, len(nums)):
            if nums[index] != nums[counter_index - 1]:
                nums[counter_index] = nums[index]
                counter_index += 1

        return counter_index

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = {}

        for index, number in enumerate(nums):
            if counter.get(number) is None:
                counter[number] = 1
            else:
                counter[number] += 1

        counter = sorted(counter.items(),
                         key=lambda item: item[1],
                         reverse=True)
        return counter[0][0]