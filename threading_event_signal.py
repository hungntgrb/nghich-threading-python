import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format="(%(threadName)-12s) %(message)s")


def task1(e):
    """Wait for event to continue"""
    logging.debug("task1 started")
    event_is_set = e.wait()
    logging.debug("event set: %s", event_is_set)
    logging.debug("task1 finished!")


def task2(e, t):
    """Wait for t seconds then timeout"""
    logging.debug("task2 started")
    event_is_set = e.wait(t)
    logging.debug("event set: %s", event_is_set)
    if event_is_set:
        logging.debug("Processing event")
        logging.debug("task2 finished")
    else:
        logging.debug("Timeout! worker was not called! Doing other work.")


def main():
    event1 = threading.Event()

    t1 = threading.Thread(name="block", target=task1, args=(event1,))
    t1.start()

    t2 = threading.Thread(name="non-block", target=task2, args=(event1, 1))
    t2.start()

    logging.debug("Waiting before setting event1")
    time.sleep(0.6)
    event1.set()
    logging.debug("event1 set!")


if __name__ == "__main__":
    main()
