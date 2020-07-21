Space Complexity

Rules of Thumb:
    - Most primitives (booleans, numbers, undefined, None) are constant space.
    - Strings require O(n) space (where n is the string length)
    - Reference types are generally O(n), where n is the lenth (for arrays) or number of keys (for objects)


Ex. def sum(arr):
    total = 0
    i = 0
    for num in arr:
        total += arr[i]
    return total

Focusing on the space complexity, the variables total and i are not being increased in size. Eventhough new values are being added to the variables, that DOES NOT affect the space but ,rather the runtime. Therefore, the space complexity is O(1).


Ex. def double(arr):
    new_arr = []
    i = 0
    for num in arr:
        new_arr.append(2 * arr[i])
        i += 1
    return new_arr
    
For the function above, the new_arr will always be the size of the array arr. As a result, if arr has 50 values, new_arr will have a size of 50. Regardless, the size of new_arr depends on the size of arr, and the space complexity is O(n).
    
    








