def maxSubArrayGreedy(nums):
    if not nums:
        return 0

    if len(nums) == 1:
        return nums

    curr_sum = max_sum = nums[0]

    for i in range(len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(max_sum, curr_sum)

    return max_sum
