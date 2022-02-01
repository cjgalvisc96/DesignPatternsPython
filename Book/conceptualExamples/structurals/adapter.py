class Target:
    def request(self) -> str:
        return "Target: the default target's behavior."


class Adaptee:
    def specific_request(self) -> str:
        return ".ettpadA eht fo roivaheb laiceps"


class Adapter(Target, Adaptee):
    def request(self) -> str:
        return f"Adapter: (TRANSLATE) {self.specific_request()[::-1]}"


def client_code(*, target: "Target") -> None:
    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target=target)
    print()

    adaptee = Adaptee()
    print(
        "Client: The adaptee class has a weired interface. "
        "See, I don't understand it:"
    )
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter()
    client_code(target=adapter)
