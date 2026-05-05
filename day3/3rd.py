# Assignment 2

# Trapping Rain Water:
# Given an array arr[] of size n consisting of non-negative integers,
# where each element represents the height of a bar in an elevation map and the width of each bar is 1,
# determine the total amount of water that can be trapped between the bars after it rains.

def trap(arr):
    left = 0
    right = len(arr) - 1
    left_max = 0
    right_max = 0
    water = 0

    while left <= right:
        if arr[left] < arr[right]:
            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                water += left_max - arr[left]
            left += 1
        else:
            if arr[right] >= right_max:
                right_max = arr[right]
            else:
                water += right_max - arr[right]
            right -= 1

    return water