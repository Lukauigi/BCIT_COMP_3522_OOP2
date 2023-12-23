"""
This module depicts how threads dont have any effect on CPU bound code.
"""
import time
import concurrent.futures


COUNT = 50000000


def countdown(n):
    while n > 0:
        n -= 1


def main():
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.submit(countdown, COUNT//3) # 10/3 = 3.3333. 10//3 = 3
        executor.submit(countdown, COUNT//3)
        executor.submit(countdown, COUNT//3)
    duration = time.time() - start
    print(f"Counting down to {COUNT} took {duration: .2f} seconds")


if __name__ == '__main__':
    main()