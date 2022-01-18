from abc import ABC


class Memento(ABC):
    def __init__(self, *, file: object, content: str) -> None:
        self.file = file
        self.content = content


class FileWriterUtility:
    def __init__(self, *, file: object) -> None:
        self.file = file
        self.content = ""

    def write(self, *, string: str) -> None:
        self.content += string

    def save(self) -> Memento:
        return Memento(file=self.file, content=self.content)

    def undo(self, memento: Memento) -> None:
        self.file = memento.file
        self.content = memento.content


class FileWriterCaretaker(ABC):
    def save(self, *, writer: FileWriterUtility) -> None:
        self.obj = writer.save()

    def undo(self, *, writer: FileWriterUtility) -> None:
        writer.undo(memento=self.obj)


if __name__ == "__main__":
    caretaker = FileWriterCaretaker()
    writer = FileWriterUtility(file="test.txt")

    writer.write(string="First vision of GeeksforGeeks\n")
    print(f"{writer.content}\n\n")

    caretaker.save(writer=writer)

    writer.write(string="Second vision of GeeksforGeeks\n")
    print(f"{writer.content}\n\n")

    caretaker.undo(writer=writer)
    print(f"{writer.content}\n\n")
