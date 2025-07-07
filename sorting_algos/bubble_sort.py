import random

def bubble_sort(nums: list[int]) -> list[int]:
    len_nums = len(nums)
    for i in range(len_nums):
        for j in range(len_nums - 1 -i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

# def bubble_sort(nums: list[int]) -> list[int]:
#     flag = len(nums)
#     swap = True
#     while swap:
#         check = 0
#         for i in range(flag-1):
#             if nums[i] > nums[i+1]:
#                 nums[i], nums[i+1] = nums[i+1], nums[i]
#                 check = 1
#         flag -= 1
#         swap = True if check == 1 else False
#     return nums

if __name__ == '__main__':
    nums = [random.randint(100, 1000) for i in range(10)]
    print(nums)
    print(bubble_sort(nums))