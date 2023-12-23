import threading
import time

class SiteDownloadThread(threading.Thread):
    """
    This thread is responsible for simulating a time intensive task.
    """

    # keeps track of the next unique id
    id = 0

    @classmethod
    def increment_id(cls):
        """
        Increments the unique id and returns it. Should be used to provide
        each thread a unique id.
        :return:
        """
        cls.id += 1
        return cls.id

    def __init__(self):
        super().__init__()
        self.id = self.increment_id()

    def run(self):
        """
        Executes the thread so that it can perform something intensive.
        Automatically called when .start() is called on this object
        """
        print(f"Thread process started by thread {self.id}")
        time.sleep(2)
        print("Thread finished executing")

def main():
    start_time = time.time()
    print("Main thread started")
    #instantiate threads
    t1 = SiteDownloadThread()
    t2 = SiteDownloadThread()
    print("Starting thread")

    # start running the threads simultaneously
    t1.start()
    t2.start()

    # wait until threads are finished before continuing the main thread
    t1.join()
    t2.join()

    duration = time.time() - start_time
    print(f"Main finished in {duration} seconds") #takes about 2 seconds


if __name__ == '__main__':
    main()