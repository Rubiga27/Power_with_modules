def power_modules(A,B,C):
    result=1
    for i in range(B):
        result=(result*A)%C
    return result
A,B,C=map(int,input().split())
result=power_modules(A,B,C)
print(result)


"""

input:1
A=2 B=3 C=3
output=2

input:2
A=5 B=2 C=4
output=1
"""