import threading


class Cub:


    def __init__(self, lenght, width, height):
        self.lenght = lenght
        self.width = width
        self.height = height

    def volume(self):
         return self.lenght * self.width * self.height

    def calclenght(self):
         return ((self.lenght * 12))


# def main():
#     cub = Cub(3, 4, 5)
#     print("Volume = ", cub.volume())
#     print("Total lenght = ", cub.calclenght())

    if __name__ == "__main__":
        thread2 = threading.Thread(target=volume, args=(50,))
        thread2.start()

        thread2.join()

        print("is Done!")