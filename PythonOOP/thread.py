import threading


def calculate_cube(num):
    print("Cube: {}".format(num * num))


def calculate_square(num):
    print("Square: {}".format(num * num))


if __name__ == "__main__":
    thread2 = threading.Thread(target=calculate_square, args=(50,))
    thread1 = threading.Thread(target=calculate_cube, args=(50,))

    thread2.start()
    thread1.start()

    thread1.join()
    thread2.join()

    print("is Done!")
