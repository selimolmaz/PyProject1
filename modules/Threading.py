import threading
import time

# the function for doing two things in same time
def run_in_thread(func):
    def wrapper(*args, **kwargs):
        t = threading.Thread(target=func, args=args, kwargs=kwargs)
        t.start()
    return wrapper


