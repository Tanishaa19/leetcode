class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        ans = []

        for x in nums1:
            i = nums2.index(x)
            nge = -1

            for j in range(i + 1, len(nums2)):
                if nums2[j] > x:
                    nge = nums2[j]
                    break

            ans.append(nge)

        return ans