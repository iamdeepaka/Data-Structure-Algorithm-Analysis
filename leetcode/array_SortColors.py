# Time: O(N)
# Space: O(1)

def sortColors(nums):
    # base case
    if len(nums) == 0:
        return None

    if len(nums) == 1:
        return nums

    p0 = curr = 0
    p2 = len(nums) - 1

    while curr <= p2:
        if nums[curr] == 0:
            nums[p0], nums[curr] = nums[curr], nums[p0]
            p0 += 1
            curr += 1
        elif nums[curr] == 2:
            nums[curr], nums[p2] = nums[p2], nums[curr]
            p2 -= 1
        else:
            curr += 1
