# container with most water
# def maxwater(arr):
#     left = 0
#     right = len(arr) - 1
#     res = 0

#     while left < right:
#         tres = min(arr[left], arr[right]) * (right - left)
#         res = max(res, tres)

#         if arr[left] < arr[right]:
#             left += 1
#         else:
#             right -= 1

#     return res

# print(maxwater([6,1,2,3,5]))


def spiral(arr):
    res = []

    t = 0                      # top row
    b = len(arr) - 1           # bottom row
    l = 0                      # left column
    r = len(arr[0]) - 1        # right column

    while t <= b and l <= r:

        # 1. left → right
        for j in range(l, r + 1):
            res.append(arr[t][j])
        t += 1

        # 2. top → bottom
        for i in range(t, b + 1):
            res.append(arr[i][r])
        r -= 1

        # 3. right → left
        if t <= b:
            for j in range(r, l - 1, -1):
                res.append(arr[b][j])
            b -= 1

        # 4. bottom → top
        if l <= r:
            for i in range(b, t - 1, -1):
                res.append(arr[i][l])
            l += 1

    return res


print(spiral([[1,2,3],[4,5,6],[7,8,9]]))
    