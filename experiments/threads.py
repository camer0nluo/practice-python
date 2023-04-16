import threading
import time
import random


def execute_thread(thread_num):
    print(
        f'Thread {thread_num} sleeps at {time.strftime("%H:%M:%S", time.gmtime())}.'
    )

    sleep_time = random.randint(1, 5)

    time.sleep(sleep_time)

    print(
        f'Thread {thread_num} stops sleeping at {time.strftime("%H:%M:%S", time.gmtime())}.'
    )


def main():
    for i in range(10):
        thread = threading.Thread(target=execute_thread, args=(i, ))
        # thread.daemon = True
        thread.start()
        # thread.join()

    print("Active threads: ", threading.active_count())
    print("thread objects: ", threading.enumerate())

if __name__ == '__main__':
    main()
