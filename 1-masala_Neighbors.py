def find_sign_neighbors(nums):
    result = []
    for i in range(len(nums) - 1):
        if nums[i] * nums[i + 1] > 0:
            result.append(f"{nums[i]} {nums[i + 1]}")
    return result

inputs = [
    [-1, 2, 3, -1, -2],
    [-1, 2, 3, -1, 4, 5, 6, 7]
]

for nums in inputs:
    output = find_sign_neighbors(nums)
    for pair in output:
        print(pair)
    print() 
