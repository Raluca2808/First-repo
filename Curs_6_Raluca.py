class car:
    make = 'dacia'
    model = None
    year = 2022
    color = None

    def __init__(self, model, color):
        self.model = model
        self.color = color

    def get(self):
        print(self.color)
        print(self.make)
        print(self.year)
        print(self.model)

    def accelerate(self):
        print('vrum vrum!')

    def stop(self):
        print('STOP')


# car1 = car('logan', 'negru')
# car2 = car('duster', 'rosu')
# print(car1.model)
# print(car2.model)
# car1.get()
# car1.accelerate()
# car2.stop()
