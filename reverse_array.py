# reverse an array 
# method 1
array = [1,2,3,4,5,6,7,8,9,10,11]

def reverse(A):
    N = len(A)
    print( N )
    for i in range( N // 2 ):
        k = N - i - 1
        A[i] , A[k] = A[k] , A[i]
    return A

print(reverse(array))


print("===========================")


# method 2
array2 = [1,2,3,4,5,6,7,8,9,10,11]

def reverse2(A):
    temp_list = []
    length = len(A)
    for i in range(length-1, -1 ,-1):
        temp_list.append(A[i])
    return temp_list

print(reverse2(array2))