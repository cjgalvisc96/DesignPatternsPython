from typing import Any, Union


class IDeluxeRide:
    def give_deluxe_ride(self) -> None:
        pass


class IPremiumRide:
    def give_premium_ride(self) -> None:
        pass


class CarDeluxeRide(IDeluxeRide):
    def give_deluxe_ride(self) -> None:
        print("Deluxe car ride")


class BikeDeluxeRide(IDeluxeRide):
    def give_deluxe_ride(self) -> None:
        print("Deluxe bike ride")


class CarPremiumRide(IPremiumRide):
    def give_deluxe_ride(self) -> None:
        print("Premium car ride")


class BikePremiumRide(IPremiumRide):
    def give_deluxe_ride(self) -> None:
        print("Premium bike ride")


class IRideFactory:
    @staticmethod
    def get_ride(*, category: str) -> Any:
        pass


class Car(IRideFactory):
    @staticmethod
    def get_ride(*, category: str) -> Union[CarPremiumRide, CarDeluxeRide, Exception]:
        if category == "premium":
            return CarPremiumRide()
        if category == "delux":
            return CarDeluxeRide()
        raise Exception(f"{category} is invalid Car category")


class Bike(IRideFactory):
    @staticmethod
    def get_ride(*, category: str) -> Union[BikePremiumRide, BikeDeluxeRide, Exception]:
        if category == "premium":
            return BikePremiumRide()
        if category == "deluxe":
            return BikeDeluxeRide()
        raise Exception(f"{category} is invalid Bike category")


class TransportFactory:
    @staticmethod
    def get_transport(*, _type: str, category: str) -> Union[Car, Bike, Exception]:
        if _type == "car":
            return Car().get_ride(category=category)
        if _type == "bike":
            return Bike().get_ride(category=category)
        raise Exception(f"{_type} is invalid Transport type")


if __name__ == "__main__":
    transport_type_to_create = "bike"
    transport_category = "deluxe"
    trasport = TransportFactory.get_transport(
        _type=transport_type_to_create, category=transport_category
    )
    trasport.give_deluxe_ride()
