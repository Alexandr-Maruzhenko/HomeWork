class Car:
    brand: str
    number: str
    color: str
    count_passenger_seats: int
    is_baby_seat: bool

    def __init__(self, brand, number, color, count_passenger_seats, is_baby_seat, is_busy=False) -> None:
        self.brand = brand
        self.number = number
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = is_busy

    def __str__(self) -> str:
        return (f"Автомобиль {self.brand}, "
                f"государственный номер {self.number}, "
                f"цвет {self.color}, "
                f"количество пассажиров {self.count_passenger_seats}, "
                f"{'не ' if self.is_baby_seat is False else ''}возможна перевозка детей, "
                f"{'свободен.' if self.is_busy is False else 'занят.'}")


class Taxi:
    cars: list

    def __init__(self, cars) -> None:
        self.cars = cars

    def find_car(self, count_passenger, is_baby):
        for car in self.cars:
            if (car.count_passenger_seats >= count_passenger) and (car.is_baby_seat == is_baby | True) and (
                    car.is_busy is False):
                car.is_busy = True
                return car
            else:
                return None


lexus = Car("Lexus", "2050АС-7", "чёрный", 4, True)
lada = Car("Lada Vesta", "8533АН-7", "белый", "4", False)
# print(lexus)
# print(lada)
taxi = Taxi([lexus, lada])
result = taxi.find_car(4, True)
print(result)
