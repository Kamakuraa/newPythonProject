import threading


class cuboid:
    x: float
    y: float
    z: float

    def __init__(
            self,
            x: float,
            y: float,
            z: float
    ):
        self.x = x
        self.y = y
        self.z = z

    def getVolume(
            self,
            output,
            index: int
    ) -> None:
        output[index] = self.x * self.y * self.z

    def getSideLength(
            self,
            output,
            index: int
    ) -> None:
        output[index] = self.x * 4 + self.y * 4 + self.z * 4


sizes = [
    [
        1,
        2,
        3
    ],
    [
        4,
        5,
        6
    ]
]

output = []

for i in range(
        0,
        len(sizes)
):
    output.append(
        [None, None]
    )

    cuboi = cuboid(
        *sizes[i]
    )

    thread1 = threading.Thread(
        target=cuboi.getVolume,
        args=(
            output[i],
            0
        )
    )

thread2 = threading.Thread(
    target=cuboi.getSideLength,
    args=(
        output[i],
        1
    )
)

thread2.start()
thread2.join()

thread1.start()
thread1.join()

print(
    "Volume of Cuboid #%s: %s" % (i, output[i][0])
)
print(
    "Length of Cuboid #%s: %s" % (i, output[i][1])
)
