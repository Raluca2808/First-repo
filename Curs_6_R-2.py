from Curs_6_Raluca import car


class service:
    listCar = []
    nrCars = 0
    price = 0

    def __init__(self):
        pass

    def setListCar(self, listCar):
        self.listCar = listCar

    def getNrCars(self):
        self.nrCars = len(self.listCar)
        return self.nrCars

    def setPrice(self, price):
        self.price = price

    def calculate_price(self):
        for x in self.listCar:
            if x.model == 'logan':
                print('Pretul este 3000 lei')
                self.setPrice(3000)
            elif x.model == 'sandero':
                print('Pretul este 4000 lei')
                self.setPrice(4000)
            else:
                print('pretul este 2500 lei')
                self.setPrice(2500)

car1 = car('logan', 'negru')
car2 = car('sandero', 'rosu')
car3 = car('duster', 'alb')
car4 = car('logan', 'alb')

service1 = service()
service1.setListCar([car1, car2, car3, car4])
print(service1.getNrCars())
service1.setListCar([car1, car2, car3, car4, car4])
print(service1.getNrCars())
service1.calculate_price()
