#You may use import as below.
#import math

def solution(shirt_size):
    dit={'XS':0,'S':0,'M':0,'L':0,'XL':0,'XXL':0}
    for i in shirt_size:
        if i in dit:
            dit[i]+=1
        else:
            dit[i]=1
    answer = []
    for j in dit:
        answer.append(dit[j])

    return answer

#The following is code to output testcase.
shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size);

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")