import threading
import logging


logging.basicConfig(level=logging.DEBUG, format="(%(threadName)-12s) %(message)s")


class MyThread(threading.Thread):
    # Override run() method of Thread
    def run(self):
        logging.debug("Running!")


class MyThreadWithArgs(threading.Thread):
    def __init__(self, *pargs, **kargs):
        args = kargs.pop("args")
        kwargs = kargs.pop("kwargs")
        super().__init__(*pargs, **kargs)
        self.args = args
        self.kwargs = kwargs

    def run(self):
        logging.debug("Running with %s and %s", self.args, self.kwargs)


def main():
    for i in range(5):
        # t = MyThread()
        t = MyThreadWithArgs(args=(i, f"Kri{i}"), kwargs={"q": "Q", "w": "W"})
        t.start()


if __name__ == "__main__":
    main()
