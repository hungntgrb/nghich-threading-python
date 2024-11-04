import threading
import random
import time
import logging


def worker():
    duration = random.randint(3, 9) / 10
    logging.debug("Sleeping %.2fs", duration)
    time.sleep(duration)
    logging.debug("Ending")


logging.basicConfig(level=logging.DEBUG, format="(%(threadName)-20s) %(message)s")


def main():
    for i in range(3):
        t = threading.Thread(target=worker, daemon=True)
        t.start()

    main_thread = threading.main_thread()

    for thr in threading.enumerate():
        # Joining the current-thread causes a deadlock situation
        # Therefore it must be skipped
        if thr is main_thread:
            continue
        logging.debug("Joining %s", thr.name)
        thr.join()


if __name__ == "__main__":
    main()
