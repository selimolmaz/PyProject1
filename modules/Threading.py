import threading
import time

def print_numbers():
    for i in range(10):
        print(i)
        time.sleep(0.5)

def print_letters():
    for letter in "abcdefghij":
        print(letter)
        time.sleep(0.5)

# Create two threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start the threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print("Both threads finished.")
