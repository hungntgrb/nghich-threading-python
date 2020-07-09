import threading
import time


def timeit(f, args=None):
    """Execute a function and report the time it took."""
    t0 = time.time()
    if args:
        f(args)
    else:
        f()
    t1 = time.time()
    print(display(f"TOOK ({t1 - t0:6f}) secs.", 46))


def afunc(i):
    print(f'Start afunc({i})...')
    time.sleep(i)
    print(f'\tEnd afunc({i})!')


def main1():
    for i in [3, 2, 1]:
        afunc(i)


def main2(threads_):
    for thr in threads_:
        thr.start()
    for thr in threads_:
        thr.join()


def space_around(aStr):
    return " " + aStr + " "


def display(aStr, length):
    return space_around(aStr).center(length, '-')


def main():
    print("""\
#############################################
#                                           #
#     Play a bit with Python Threading      #
#         Writer: Nguyen Thanh Hung         #
#                                           #
#############################################
""")

    threads = [threading.Thread(target=afunc, args=(i,)) for i in [3, 2, 1]]

    print(display("WITHOUT threading", 46))
    timeit(main1)
    print()
    print(display("WITH threading", 46))
    timeit(main2, threads)
    print()


if __name__ == '__main__':
    main()
