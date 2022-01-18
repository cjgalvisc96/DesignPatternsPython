from abc import ABC, abstractmethod


class ResearchGuideline(ABC):
    def templateMethod(self):
        self.step1()
        self.step2()
        self.step3()
        self.step4()

    def step1(self):
        pass

    def step2(self):
        pass

    @abstractmethod
    def step3(self):
        pass

    def step4(self):
        pass


class UniversityA(ResearchGuideline):
    def step2(self):
        print("Step 2 - Applied by UniversityA")

    def step3(self):
        print("Step 3 - Applied by UniversityA")


class UniversityB(ResearchGuideline):
    def step1(self):
        print("Step 1 - Applied by UniversityB")

    def step3(self):
        print("Step 3 - Applied by UniversityB")

    def step4(self):
        print("Step 4 - Applied by UniversityB")


class Client:
    def __init__(self, *, research_guideline: ResearchGuideline) -> None:
        self.research_guideline = research_guideline

    def execute(self) -> None:
        self.research_guideline.templateMethod()


if __name__ == "__main__":
    print("UniversityA:")
    client = Client(research_guideline=UniversityA())
    client.execute()

    print("UniversityB:")
    client = Client(research_guideline=UniversityB())
    client.execute()
