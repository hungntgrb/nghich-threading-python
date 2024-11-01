import threading


def sayHi(name):
    print("> Hi %s!" % name)


def main():
    threads = []

    for i in range(5):
        t = threading.Thread(target=sayHi, args=(f"Doraemon {i}",))
        threads.append(t)
        t.start()


if __name__ == "__main__":
    main()
