"""
This module depicts how to create threads using the Thread class
"""

import threading
import time

def thread_function(thread_id):
    print(f"Thread {thread_id} starting")
    time.sleep(2) #simulate an IO operation that takes 1 second
    print(f"Thread {thread_id} finishing")

if __name__ == "__main__":
    threads = []
    start = time.time()
    print("--Start threads--")

    for thread_id in range(0,3):
        x = threading.Thread(target=thread_function, args=(thread_id,))
        x.start()
        threads.append(x)

    print("--Join threads--")

    for thread in threads:
        thread.join()
    print(time.time() - start)
