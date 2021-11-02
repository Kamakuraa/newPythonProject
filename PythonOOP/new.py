import threading


class Cube:

    def __init__(self, lat):
        self.lat = lat

    def calculVolum(self):
        return self.lat ** 3

    if __name__ == "__main__":
        t1 = threading.Thread(target=calculVolum, args=(5,) )

        t1.start()
        t1.join()

        print("is done")
