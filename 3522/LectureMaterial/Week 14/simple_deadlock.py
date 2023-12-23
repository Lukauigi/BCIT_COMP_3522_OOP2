"""
This module depicts a simple DEADLOCK example
Soldiers need both a sword and shield before they are considered fully equipped
In this code:
Soldier 1 takes a shared sword lock
Soldier 2 takes a shared shield lock
Soldier 1 now needs a shield lock, and soldier 2 needs a sword lock
Each soldier is holding a lock the other needs. This is a deadlock, where the program
can not continue because each thread holds onto a lock the other thread needs

SOLUTION:
The program can continue if the lock release code is uncommented, freeing up the lock that each
respective soldier needs
"""

import threading
import time

sword_lock = threading.Lock()
shield_lock = threading.Lock()

def equip_1():
    print("Soldier 1 ready to equip")
    sword_lock.acquire() #soldier 1 acquires a sword, but soldier 2 will need this in the future

    print("Soldier 1 got sword, sleeping")
    time.sleep(2)
    sword_lock.release()
    shield_lock.acquire() #soldier 1 waits for soldier 2 to release their shield

    print("Soldier 1 got shield")
    print("Soldier 1 fully equipped")
    shield_lock.release()

def equip_2():
    print("Soldier 2 ready to equip")
    shield_lock.acquire() #soldier 2 acquires a shield, but soldier 1 will need this in the future

    print("Soldier 2 got shield, sleeping")
    time.sleep(2)
    shield_lock.release()
    sword_lock.acquire() #soldier 2 waits for soldier 1 to release their sword

    print("Soldier 2 got shield")
    print("Soldier 2 fully equipped")
    sword_lock.release()

if __name__ == "__main__":
    start = time.time()
    print("--Start threads--")

    soldier_thread_1 = threading.Thread(target=equip_1)
    soldier_thread_2 = threading.Thread(target=equip_2)

    soldier_thread_1.start()
    soldier_thread_2.start()

    soldier_thread_1.join()
    soldier_thread_2.join()
    print("Both soldiers equipped")

    print(time.time() - start)
