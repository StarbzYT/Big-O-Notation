# timer for slower adding func
from functools import wraps
from time import time


def speed_test(fn):
    @wraps(fn)  # decorator
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Executing {fn.__name__}")  # @wraps will ensure that we get the correct __name__
        print(f"Time elapsed: {end_time - start_time}")  # return result
        return result
    return wrapper


@speed_test
def sum_slower(n):  # uses for loop
    count = 0
    for num in range(1, n+1):
        count += num
    return count


@speed_test
def sum_faster(n):  # no for loop
    return n * (n + 1) / 2  # special quicker formula

# call decorators


print(sum_slower(10000000))
print(sum_faster(10000000))
# notice how the times are always different




