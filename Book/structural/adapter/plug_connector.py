class USAPlugConnectorInterface:
    def give_electricity(self):
        pass


class USAPlugConnector(USAPlugConnectorInterface):
    def give_electricity(self):
        print("This is a USA Plug")


class USAElectricalSocket:
    def plug_in(self, usa_plug):
        usa_plug.give_electricity()


class UKPlugConnectorInterface:
    def provide_electricity(self):
        pass


class UKElectricalSocket:
    def plug_in(self, uk_plug):
        print("This is a UK electrical socket")
        uk_plug.provide_electricity()


class USAtoUKPlugAdapter(UKPlugConnectorInterface):
    def __init__(self, usa_plug) -> None:
        self.usa_plug = usa_plug

    def provide_electricity(self):
        self.usa_plug.give_electricity()


if __name__ == "__main__":
    usa_plug = USAPlugConnector()
    uk_electrical_socket = UKElectricalSocket()
    uk_adapter = USAtoUKPlugAdapter(usa_plug)
    uk_electrical_socket.plug_in(uk_adapter)
