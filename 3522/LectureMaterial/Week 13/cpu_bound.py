"""
This module depicts CPU Bound code.
"""
import time
import threading
import concurrent.futures


COUNT = 50000000


def countdown(n):
    while n > 0:
        n -= 1


def main():
    start = time.time()
    countdown(COUNT)
    duration = time.time() - start
    print(f"Counting down to {COUNT} took {duration: .2f} seconds")


if __name__ == '__main__':
    main()