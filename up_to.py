# two functions. What are their time complexities?


def log_atleast_5(n):
    up_to = max(5, n)
    for num in range(1, up_to+1):  # linear time
        print(num)

# Above, as n grows/ approaches infinity, time grows roughly in proportion to n.
# There for it is O(n)


def log_atmost_5(n):
    up_to = min(5, n)
    for num in range(1, up_to+1):
        print(num)

# Look at the big picture! Even though when n is less than five the time grows inproportion to n, as n approches infinity, the loop will only run 5 times. Therefore, it has a time complexity of O(1). (simplify O(5))


log_atleast_5(3)  # up to 5
log_atleast_5(8)  # up to 8
log_atmost_5(4)  # up to 4
log_atmost_5(18)  # up to five



