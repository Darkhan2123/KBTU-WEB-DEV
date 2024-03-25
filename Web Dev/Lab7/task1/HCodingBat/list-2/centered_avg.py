def centered_average(nums):
    # Sort the list to easily find the smallest and largest elements
    nums.sort()

    # Remove the smallest and largest elements from the list
    nums = nums[1:-1]

    # Calculate the sum of the remaining elements
    total = sum(nums)

    # Calculate the centered average
    average = total // len(nums)

    return average