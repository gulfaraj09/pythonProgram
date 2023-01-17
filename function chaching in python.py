import time
from functools import lru_cache


@lru_cache(maxsize=3)
def some_work(n):
    # Some task taking n seconds
    time.sleep(n)
    return n


if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    some_work(2)
    some_work(5)
    print("done....Calling again")
    some_work(3)
    print("Called again")

