# gas station

# def journey(gas,cost):
#     g=0
#     s=0
#     ind=0
#     for i in range(len(gas)):
#         g=g+gas[i]-cost[i]
#         if (g<0):
#             ind=i+1
#             g=0
#     return ind
# g=[7,1,3,3]
# c=[6,3,1,2]
# print(journey(g,c))

# gas station
# leet code 134
def gas_station(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    
    g = 0
    startindex = 0
    
    for i in range(len(gas)):
        g += gas[i] - cost[i]
        
        if g < 0:
            g = 0
            startindex = i + 1
    
    return startindex
(gas_station([1,2,3,4,5], [3,4,5,1,2]))


    