def wiggleMaxLength(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    up = [1] * len(nums)
    down = [1] * len(nums)
    if len(nums) == 0:
        return 0
    up[0] = down[0] = 1
    for i in range(1, len(nums)):
        print(i, nums[i], nums[i - 1])
        if nums[i] > nums[i - 1]:
            up[i] = down[i - 1] + 1
            down[i] = down[i - 1]
        elif nums[i] < nums[i - 1]:
            up[i] = up[i - 1]
            down[i] = up[i - 1] + 1
        else:
            up[i] = up[i - 1]
            down[i] = down[i - 1]
        # print(i, up[i], down[i])
    return max(up[len(nums) - 1], down[len(nums) - 1])


wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8])
