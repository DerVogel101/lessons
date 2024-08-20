from functools import wraps, cache
import time


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} ran in {end - start} seconds')
        return result
    return wrapper


@timer
def some_function():
    time.sleep(1)
    print('Function ran')


some_function()  # Output: Function ran
print(some_function.__name__)


@lambda x: x(1, 2)
def add(a, b):
    return a + b


print(add)  # Output: 3
