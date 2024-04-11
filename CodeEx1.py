def sorted_squared(array):
    if array!=[]:
      i = 0
      for n in array:
        array[i] = n**2
        i += 1
      array.sort()
      print(array)
      return array
    print([])
    return []

sorted_squared([0,3,4])
sorted_squared([0,-3,4])
sorted_squared([-12,3,4])
sorted_squared([])

