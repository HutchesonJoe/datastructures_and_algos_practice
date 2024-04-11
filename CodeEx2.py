def monotonic_array(array):
    if len(array)==0:
        return True
    elif array[0] <= array[len(array)-1]:
        for i in range(len(array)-1):
            if array[i] > array[i + 1]:
                return False
    else:
        for i in range(len(array)-1):
            if array[i] < array[i+1]:
                return False
    return True

print(monotonic_array([9,8,7,0]))
print(monotonic_array([-9,8,17,0]))
print(monotonic_array([]))
print(monotonic_array([1,2,3,4]))
