from typing import Any


class SinglentonMeta(type):
    _instances = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwds)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singlenton(metaclass=SinglentonMeta):
    def some_business_logic(self):
        pass


if __name__ == "__main__":
    s1 = Singlenton()
    s2 = Singlenton()
    if id(s1) == id(s2):
        print("Singlenton works, bothvariables contain the same instance.")
    else:
        print("Singlenton failed, variables contain diferrent instances.")
