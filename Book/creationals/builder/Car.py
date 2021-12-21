class Director:
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_car(self):
        car = Car()
        # Step1 -> goes the body
        body = self.__builder.get_body()
        car.set_body(body)

        # Step2 -> goes the engine
        engine = self.__builder.get_engine()
        car.set_engine(engine)

        # Step2 -> goes the wheels
        number_of_wheels = 0
        while number_of_wheels < 4:
            wheel = self.__builder().get_wheel()
            car.attach_wheel(wheel)
            number_of_wheels += 1

        return car


class Car:
    def __init__(self) -> None:
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def set_body(self, body):
        self.__body = body

    def attach_wheel(self, wheel):
        self.__wheels.append(wheel)

    def set_engine(self, engine):
        self.__engine = engine

    def specification(self):
        print(
            f"Body: {self.__body.shape}"
            f"\nEngine_horsepower: {self.__engine.horsepower}"
            f"\nTire_size: {self.__wheels[0].size}"
        )


class Builder:
    @staticmethod
    def get_wheel():
        pass

    @staticmethod
    def get_engine():
        pass

    @staticmethod
    def get_body():
        pass


class JeppBuilder(Builder):
    @staticmethod
    def get_wheel():
        wheel = Wheel()
        wheel.size = 22
        return wheel

    @staticmethod
    def get_engine():
        engine = Engine()
        engine.horsepower = 400
        return engine

    @staticmethod
    def get_body():
        body = Body()
        body.shape = "SUV"
        return body


class Wheel:
    size = None


class Engine:
    horsepower = None


class Body:
    shape = None


if __name__ == "__main__":
    jeep_builder = JeppBuilder()
    director = Director()
    print("JEEP")
    director.set_builder(JeppBuilder)
    jeep = director.get_car()
    jeep.specification()
