import threading
import time

def print_epoch(name_of_thread, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count+=1
        print(name_of_thread, "----------",time.time())

def print_Cube(thread,num):
    print("Cube = {}".format(num*num*num))

def print_Square(thread, num):
    print("Square = {}".format(num*num))

if __name__ == '__main__':
    #creating an instance of the Thread Class
    #target= the function print_epoch, args = (name_of_thread, delay) [arguments from the print_epoch function]
    t1 = threading.Thread(target=print_epoch, args=("Thread 1", 1))
    t2 = threading.Thread(target=print_epoch, args=("Thread 2", 2))
    t3 = threading.Thread(target=print_Square, args=("Thread 3", 2))
    t4 = threading.Thread(target=print_Cube, args=("Thread 4", 2))

    #Initiate the threads
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    #join threads back to main
    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print("All threads Complete")