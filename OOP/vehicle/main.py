import importantimport


class Vehicle:
    def __init__(self, max_speed: float | int = None) -> None:
        self.__max_speed = max_speed if type(max_speed) in [float, int] else None

    def set_max_speed(self, max_speed: float | int) -> None:
        self.__max_speed = max_speed if type(max_speed) in [float, int] else None

    def get_max_speed(self) -> float | int:
        return self.__max_speed


class Bike(Vehicle):
    def __init__(self, diameter_wheel: float | int, bike_sex: str) -> None:
        super().__init__()
        self.__diameter_wheel = diameter_wheel if type(diameter_wheel) in [float, int] else None
        self.__bike_sex = bike_sex if type(bike_sex) == str else None

    def set_diameter_wheel(self, diameter_wheel: float | int) -> None:
        self.__diameter_wheel = diameter_wheel if type(diameter_wheel) in [float, int] else None

    def get_diameter_wheel(self) -> float | int:
        return self.__diameter_wheel

    def get_sex(self) -> str:
        return self.__bike_sex


class WomanBike(Bike):
    def __init__(self, diameter_wheel: float | int) -> None:
        super().__init__(diameter_wheel, "Woman")


class ManBike(Bike):
    def __init__(self, diameter_wheel: float | int) -> None:
        super().__init__(diameter_wheel, "Man")


class OtherBike(Bike):
    def __init__(self, diameter_wheel: float | int, type_bike: str) -> None:
        super().__init__(diameter_wheel, type_bike)


class KW(Vehicle):
    def __init__(self, max_speed: float | int, max_load: float | int, max_volume: float | int) -> None:
        max_speed = max_speed if type(max_speed) in [float, int] else None
        super().__init__(max_speed=max_speed)
        self.__max_load = max_load if type(max_load) in [float, int] else None
        self.__max_volume = max_volume if type(max_volume) in [float, int] else None

    def set_max_load(self, max_load: float | int) -> None:
        self.__max_load = max_load if type(max_load) in [float, int] else None

    def get_max_load(self) -> float | int:
        return self.__max_load

    def set_max_volume(self, max_volume: float | int) -> None:
        self.__max_volume = max_volume if type(max_volume) in [float, int] else None

    def get_max_volume(self) -> float | int:
        return self.__max_volume


class PKW(KW):
    def __init__(self, max_speed: float | int, max_load: float | int, max_volume: float | int, seats: int) -> None:
        super().__init__(max_speed=max_speed, max_load=max_load, max_volume=max_volume)
        self.__seats = seats if type(seats) == int else None

    def set_seats(self, seats: int) -> None:
        self.__seats = seats if type(seats) == int else None

    def get_seats(self) -> int:
        return self.__seats


class LKW(KW):
    def __init__(self, max_speed: float | int, max_load: float | int, max_volume: float | int, trailer: bool) -> None:
        super().__init__(max_speed=max_speed, max_load=max_load, max_volume=max_volume)
        self.__trailer = trailer if type(trailer) == bool else None

    def set_trailer(self, trailer: bool) -> None:
        self.__trailer = trailer if type(trailer) == bool else None

    def get_trailer(self) -> bool:
        return self.__trailer


if __name__ == "__main__":
    print(...)


