import threading
import logging
import time


def worker():
    logging.debug("Worker running!")


logging.basicConfig(level=logging.DEBUG, format="(%(threadName)-12s) %(message)s")


def main():
    # Timer thread will call the function after that amount of time.
    t1 = threading.Timer(0.5, worker)
    t2 = threading.Timer(1, worker)

    t1.start()
    # t1 is not a daemon thread so it will be joined implicitly.
    t2.start()

    logging.debug("Wait before cancelling %s", t2.name)
    time.sleep(0.3)
    logging.debug("Cancelling %s", t2.name)
    t2.cancel()  # t2 is canceled before it's called.
    logging.debug("%s canceled!", t2.name)
    logging.debug("Done")


if __name__ == "__main__":
    main()
