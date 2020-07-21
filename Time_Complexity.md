Big 0 Notation

As the size of input grows (in a function), how much longer does it take to run the function? (General Overview)

Ex. def sum_all_1(n):  # O(1)
    return n * (n + 1) / 2
    
The function sum_all_1 above has the same number of operations, no matter the size of input (always 3 operations). Therefore, it will run at a constant time. In other words, it has a time complexity of O(1). (graph is constant)

Ex. def sum_all_2(n):  # O(n)
    count = 0
    for num in range (1, n+1):
        count += num
    return count

The function sum_all_2 above has to add and assign to count n times (n operations!). As the size of input grows, n is roughly directly proportional to the time it takes to run the function. Therefore, it has a time complexity of O(n). (graph is linear)

What if n is a nested list?

Ex. def sum_list(n):  # O(n^2)
    count = 0
    for l in n:  # O(n)
        for num in l:  # O(n)
            count += num
    return count


The function sum_list includes a double for loop to access the numbers in each list for n. As a result, as n grows, the time grows exponentially (n^2) and the graph is quadratic. (O(n^2))

* O(n) operation inside of an O(n) operation is O(n*n) or 0(n^2)