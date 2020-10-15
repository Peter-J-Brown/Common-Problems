
list = [1,4,6,78,2,87,3,23,6,8,2,87,9,125,3,12,15,18,26,13]


#finds two numbers that sum to a given value

'''
def two_sum(nums, target):
    nums.sort()
    result = []
    i = 0
    p1 = nums[i]
    p2 = nums[len(nums) - i - 1]
    if p1 + p2 = target:
        return result
    if p1 + p2 != target:
        i =+ 1

'''

# finds all combinations of any size that sum to the target
def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        print("The sum of: ", partial, "= ", target)
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n])


# finds four numbers that sum to a given value
def four_sum(nums, target):
    nums.sort()
    result = []
    for i in range(len(nums) - 3):
        if i and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 2):
            if j != i + 1 and nums[j] == nums[j - 1]:
                continue
            sum = target - nums[i] - nums[j]
            left, right = j + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == sum:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] > sum:
                    right -= 1
                else:
                    left += 1
    return result

#print(four_sum(list, 28))

print(subset_sum(list, 21))