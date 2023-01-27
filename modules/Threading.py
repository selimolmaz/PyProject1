import threading
import time
# the function for doing two things in same time
def threads_multiple(function1, function2):
    # Create two threads
    t1 = threading.Thread(target=function1)
    t2 = threading.Thread(target=function2)

    # Start the threads
    t1.start()
    t2.start()

    # Wait for both threads to finish
    t1.join()
    t2.join()

    return print("Both threads finished.")

def thread_single(function):
    t = threading.Thread(target=function)
    t.start()
    t.join()
    return print("single thread finished.")
