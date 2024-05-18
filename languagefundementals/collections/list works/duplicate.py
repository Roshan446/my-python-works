arr = [4,9,5,6,4,9,5]

# arr.sort()
# print(arr)
# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         ithelement = arr[i]                         <<<-------- not efficent
#         jthelement = arr[j]
#         if ithelement == jthelement:
#             print(ithelement)




arr.sort()
i = 0
while(i<len(arr)-1):
    j= i+1
    jthelement = arr[j]
    ithelement = arr[i]
    diff = arr[j] - arr[i]
    if diff == 0:
        print(ithelement)
    i +=1    