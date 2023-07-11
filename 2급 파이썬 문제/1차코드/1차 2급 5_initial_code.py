def solution(arr):
    arr2=[]
    for i in range(len(arr)-1,-1,-1):
        arr2.append(arr[i])
    return arr2

#The following is code to output testcase.
arr = [1, 4, 2, 3]
ret = solution(arr)

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")