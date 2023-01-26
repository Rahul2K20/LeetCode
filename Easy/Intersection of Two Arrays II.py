class Solution(object):
    def intersect(self, nums1, nums2):
        count1 = {}
        count2 = {}
        for num in nums1:
            if num not in count1:
                count1[num] = 1
            else:
                count1[num] += 1
        for num in nums2:
            if num not in count2:
                count2[num] = 1
            else:
                count2[num] += 1
        intersection = []
        for num in count1:
            if num in count2:
                intersection += [num] * min(count1[num], count2[num])
        return intersection