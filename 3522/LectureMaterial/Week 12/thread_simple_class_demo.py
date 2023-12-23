import threading
import time


def thread_process(name):
    print(f"Thread process started by thread {name}")
    time.sleep(2)
    print("Thread finished executing")


def main():
    start_time = time.time()
    print("Main thread started")
    # instantiate thread objects and assign thread_process function to them
    t1 = threading.Thread(target=thread_process, args=("my_thread 1",))
    t2 = threading.Thread(target=thread_process, args=("my_thread 2",))
    print("Starting thread")

    #start running the threads simultaneously. They will execute their assigned target function
    t1.start()
    t2.start()

    #wait until threads are finished before continuing the main thread
    t1.join()
    t2.join()

    duration = time.time() - start_time
    print(f"Main finished in {duration} seconds") #takes about 2 seconds


if __name__ == '__main__':
    main()