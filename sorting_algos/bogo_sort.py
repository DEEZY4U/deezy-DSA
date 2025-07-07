import random

def in_order(nums: list[int])-> bool:
    return all(nums[i] <= nums[i+1] for i in range(len(nums)-1))
    # for i in range(len(nums)-1):
    #     if nums[i] > nums[i-1]:
    #         return False
    # return True

def bogo_sort(nums: list[int])->list[int]:
    print(in_order(nums))
    while not in_order(nums):
        random.shuffle(nums)
    return nums

if __name__ == '__main__':
    nums = [random.randint(100, 1000) for i in range(10)]
    print(bogo_sort(nums))