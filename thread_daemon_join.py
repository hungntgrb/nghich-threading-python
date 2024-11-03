"""
Daemon-threads: You can let them run and forget about them.
When the main-program ends, daemon-threads will automatically be terminated.
Non-daemon-threads will run to finish before main-program exits.
"""

import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG, format="(%(threadName)-12s) %(message)s")


def daemon():
    logging.debug("Start")
    logging.debug("Sleep 4s")
    time.sleep(4)
    logging.debug("End")


def non_daemon():
    logging.debug("Start")
    logging.debug("Sleep 2s")
    time.sleep(2)
    logging.debug("End")


def main():
    t_daemon = threading.Thread(name="daemon", target=daemon, daemon=True)
    t_non_daemon = threading.Thread(name="non_daemon", target=non_daemon)

    t_daemon.start()
    t_non_daemon.start()

    # .join(timeout)
    t_daemon.join(3)  # After 3s this thread will exit no matter what.
    t_non_daemon.join()
    print("t_daemon.is_alive() ", t_daemon.is_alive())


if __name__ == "__main__":
    main()
