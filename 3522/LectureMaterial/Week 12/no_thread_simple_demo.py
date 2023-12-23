import threading
import time


def thread_process(name):
    print(f"Thread process started by thread {name}")
    time.sleep(2)
    print("Thread finished executing")


def main():
    start_time = time.time()
    print("Main thread started")

    #No threading occurs. Simply calling thread_process function one after the other
    thread_process("no threading 1")
    thread_process("no threading 2")

    duration = time.time() - start_time
    print(f"Main finished in {duration} seconds") #takes about 4 seconds


if __name__ == '__main__':
    main()