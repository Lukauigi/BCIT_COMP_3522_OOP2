"""
This module depicts how to create a custom thread by inheriting from
the Thread class.
"""
import threading
import time

class MyThreadClass(threading.Thread):
    def __init__(self, thread_id):
        super().__init__()
        self.thread_id = thread_id

    def run(self):
        print(f"Thread {self.thread_id} starting")
        time.sleep(2)
        print(f"Thread {self.thread_id} finishing")

start_time = time.time()
threads = [MyThreadClass(i) for i in range(3)]

print("--Start threads--")
for thread in threads:
    thread.start()

print("--Join threads--")
for thread in threads:
    thread.join()
duration = time.time() - start_time
print(f"Duration in {duration} seconds")
