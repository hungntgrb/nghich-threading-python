import threading
import logging
import time


logging.basicConfig(
    level=logging.DEBUG, format="[%(levelname)s] (%(threadName)-20s) %(message)s"
)


def worker():
    logging.debug("Starting")
    time.sleep(0.2)
    logging.debug("Exiting")


def my_service():
    logging.debug("Starting")
    time.sleep(0.5)
    logging.debug("Exiting")


def main():
    w1 = threading.Thread(name="worker1", target=worker)
    # Unnamed Thread will use default-name
    unnamed = threading.Thread(target=worker)
    s1 = threading.Thread(name="my_service1", target=my_service)

    w1.start()
    s1.start()
    unnamed.start()


if __name__ == "__main__":
    main()
