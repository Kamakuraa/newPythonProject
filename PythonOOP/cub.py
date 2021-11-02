import multiprocessing


class Cube:

    def __init__(self, lat):
        self.lat = lat

    def calcul_volum(self):
        return self.lat ** 3

    def calcul_suma_laturi(self):
        return self.lat * 12

    if __name__ == "__main__":
        t1 = multiprocessing.Process(print(calcul_volum(10, )))

        t1.start()
        
