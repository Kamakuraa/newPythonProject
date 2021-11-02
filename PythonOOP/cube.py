import threading


class Cube:

    def __init__(self, side):
        self.side = side

    def cube_volume(self, side):
        print("Volume of cube is: {}".format(side * side * side))

    def side_sum(self, side):
        print("Sum of sides is: {}".format(side * 12))

    if __name__ == "__main__":
        thread1 = threading.Thread(target=cube_volume, args=(120,))
        thread2 = threading.Thread(target=side_sum, args=(50,))

        thread2.start()

        thread1.start()

        thread2.join()
        thread1.join()

        print("is Done!")
