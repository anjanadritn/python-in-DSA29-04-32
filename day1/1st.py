# arr=[34,56,78,12,34]
# print(arr)
# print(arr[3])

#product of Smallest Pair
 
# def psp(arr,d):
#     if len(arr) < 2:
#         return -1
#     arr.sort()
#     if arr[0]+arr[1]<=d:
#         return arr[0]*arr[1]
#     else:
#         return 0
# print(psp([78,34,56,12,38],50))
# print(psp([78,34],90))
# print(psp([78,34],112))
# print(psp([78,34],111))

# Rat count house
# arr = [2, 3, 1, 4, 5, 6]
# rat = 4
# units = 4

# def steal(rat, units, arr):
#     if len(arr) == 0:
#         return -1

#     total_food = rat * units
#     current = 0

#     for i in range(len(arr)):
#         current += arr[i]

#         if current >= total_food:
#             return i + 1   # number of houses used

#     return 0   # not enough food

# print(steal(rat, units, arr))


def bss(arr):
    l=len(arr)
    for i in range(l):
        for j in range(i+1,l):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
                return arr
print(bss([78,34,56,12,38]))


        



    
